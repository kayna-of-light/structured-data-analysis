"""Reddit subreddit scraper.

Scrapes posts from a specified subreddit using Reddit's public JSON endpoints.

This module is intentionally generic: the target subreddit and the output dataset
directory (and ScrapedCase.source) are provided at runtime.

Usage:
    from shared.scrapers.reddit_scraper import RedditScraper
    from pathlib import Path

    scraper = RedditScraper(output_dir=Path("data"), subreddit="TheMallWorld")
    scraper.scrape_all()

CLI Usage:
    python -m shared.scrapers.reddit_scraper --subreddit TheMallWorld --dataset mallworld
    python -m shared.scrapers.reddit_scraper --subreddit TheMallWorld --historical --chunk-days 30
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

from .base import BaseScraper, ScrapedCase, clean_text, get_session


REDDIT_BASE = "https://www.reddit.com"
PULLPUSH_BASE = "https://api.pullpush.io/reddit/search/submission"
DEFAULT_REQUEST_DELAY = 2.0  # Reddit rate limits - be respectful


def _fetch_reddit_json(
    subreddit: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    request_delay: float = DEFAULT_REQUEST_DELAY,
) -> Dict[str, Any]:
    """Fetch JSON from Reddit's public API for a subreddit endpoint."""

    url = f"{REDDIT_BASE}/r/{subreddit}{endpoint}"
    if params:
        url = f"{url}?{urlencode(params)}"

    session = get_session()
    headers = {
        "User-Agent": "MallWorldResearch/1.0 (Academic research)",
        "Accept": "application/json",
    }
    response = session.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    time.sleep(request_delay)
    return response.json()


def get_subreddit_created_utc(
    subreddit: str,
    request_delay: float = DEFAULT_REQUEST_DELAY,
) -> Optional[int]:
    """Fetch the subreddit's creation timestamp (UTC seconds) from Reddit.

    Reddit exposes this via /r/{subreddit}/about.json -> data.created_utc.
    Returns None if unavailable (e.g., network failure, 403, etc.).
    """

    try:
        about = _fetch_reddit_json(subreddit, "/about.json", request_delay=request_delay)
        created = about.get("data", {}).get("created_utc")
        if created is None:
            return None
        return int(created)
    except Exception:
        return None


def extract_image_urls(data: Dict[str, Any]) -> List[str]:
    """Extract image URLs from a Reddit post."""

    images: List[str] = []

    post_url = data.get("url", "")
    if "i.redd.it" in post_url:
        images.append(post_url)

    if data.get("is_gallery") and data.get("media_metadata"):
        media_metadata = data.get("media_metadata", {})
        gallery_items = data.get("gallery_data", {}).get("items", [])

        for item in gallery_items:
            media_id = item.get("media_id")
            if not media_id or media_id not in media_metadata:
                continue
            media = media_metadata[media_id]
            if media.get("s", {}).get("u"):
                img_url = media["s"]["u"].replace("&amp;", "&")
                if "preview.redd.it" in img_url:
                    import re

                    match = re.search(r"preview\.redd\.it/([^?]+)", img_url)
                    if match:
                        img_url = f"https://i.redd.it/{match.group(1)}"
                images.append(img_url)

    if not images and data.get("preview", {}).get("images"):
        for img in data["preview"]["images"]:
            source = img.get("source", {})
            if not source.get("url"):
                continue
            img_url = source["url"].replace("&amp;", "&")
            if "preview.redd.it" in img_url:
                import re

                match = re.search(r"preview\.redd\.it/([^?]+)", img_url)
                if match:
                    img_url = f"https://i.redd.it/{match.group(1)}"
            images.append(img_url)

    return images


def extract_post_data(
    post: Dict[str, Any],
    min_content_length: int,
) -> Optional[Dict[str, Any]]:
    """Extract relevant data from a Reddit listing child."""

    data = post.get("data", {})

    if data.get("removed_by_category") or data.get("selftext") in ["[removed]", "[deleted]"]:
        return None

    if data.get("stickied") or data.get("distinguished"):
        return None

    selftext = (data.get("selftext") or "").strip()
    image_urls = extract_image_urls(data)
    has_images = len(image_urls) > 0

    if not has_images and len(selftext) < min_content_length:
        return None

    created_utc = int(data.get("created_utc", 0) or 0)
    created_date = datetime.fromtimestamp(created_utc, tz=timezone.utc).isoformat()
    permalink = data.get("permalink", "")

    return {
        "id": data.get("id", ""),
        "title": data.get("title", "Untitled"),
        "selftext": selftext,
        "author": data.get("author", "[deleted]"),
        "created_utc": created_utc,
        "created_date": created_date,
        "score": data.get("score", 0),
        "upvote_ratio": data.get("upvote_ratio", 0),
        "num_comments": data.get("num_comments", 0),
        "permalink": permalink,
        "url": f"{REDDIT_BASE}{permalink}",
        "link_flair_text": data.get("link_flair_text", ""),
        "image_urls": image_urls,
        "is_gallery": data.get("is_gallery", False),
        "post_hint": data.get("post_hint", ""),
    }


class RedditScraper(BaseScraper):
    """Scraper for a single subreddit."""

    source_name = "reddit"
    output_subdir = "reddit"

    def __init__(
        self,
        output_dir: Path,
        subreddit: str,
        dataset: Optional[str] = None,
        request_delay: float = DEFAULT_REQUEST_DELAY,
        min_content_length: int = 100,
    ) -> None:
        super().__init__(output_dir)

        self.subreddit = subreddit
        self.dataset = dataset or subreddit.lower()
        self.request_delay = request_delay
        self.min_content_length = min_content_length

        # Override BaseScraper output directory to point at the dataset name.
        self.output_dir = output_dir / self.dataset
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.seen_ids: set[str] = set()
        self._load_existing_ids()

    def _load_existing_ids(self) -> None:
        for filepath in self.output_dir.glob("*.json"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "source_id" in data:
                        self.seen_ids.add(data["source_id"])
            except (json.JSONDecodeError, IOError):
                continue

        if self.seen_ids:
            self.logger.info(f"Found {len(self.seen_ids)} existing posts")

    def scrape_listing(
        self,
        sort: str = "new",
        after: Optional[str] = None,
        limit: int = 100,
    ) -> tuple[List[Dict[str, Any]], Optional[str]]:
        params: Dict[str, Any] = {"limit": min(limit, 100)}
        if after:
            params["after"] = after

        try:
            data = _fetch_reddit_json(
                self.subreddit,
                f"/{sort}.json",
                params=params,
                request_delay=self.request_delay,
            )
        except Exception as exc:
            self.logger.error(f"Failed to fetch listing: {exc}")
            return [], None

        listing = data.get("data", {})
        children = listing.get("children", [])
        next_after = listing.get("after")

        posts: List[Dict[str, Any]] = []
        for child in children:
            post_data = extract_post_data(child, min_content_length=self.min_content_length)
            if post_data and post_data["id"] not in self.seen_ids:
                posts.append(post_data)

        return posts, next_after

    def post_to_case(self, post: Dict[str, Any]) -> ScrapedCase:
        return ScrapedCase(
            source=self.dataset,
            source_id=post["id"],
            url=post["url"],
            title=clean_text(post["title"]),
            content=clean_text(post["selftext"]) if post["selftext"] else "",
            date_published=post["created_date"],
            metadata={
                "subreddit": self.subreddit,
                "author": post["author"],
                "score": post["score"],
                "upvote_ratio": post["upvote_ratio"],
                "num_comments": post["num_comments"],
                "flair": post.get("link_flair_text", ""),
                "image_urls": post.get("image_urls", []),
                "is_gallery": post.get("is_gallery", False),
                "post_hint": post.get("post_hint", ""),
            },
        )

    def scrape_all(self, max_posts: Optional[int] = None, sort: str = "new") -> List[ScrapedCase]:
        limit_str = str(max_posts) if max_posts else "unlimited"
        self.logger.info(
            f"Starting scrape of r/{self.subreddit} (dataset: {self.dataset}, max: {limit_str}, sort: {sort})"
        )

        cases: List[ScrapedCase] = []
        after: Optional[str] = None

        while max_posts is None or len(cases) < max_posts:
            posts, after = self.scrape_listing(sort=sort, after=after)

            for post in posts:
                if max_posts is not None and len(cases) >= max_posts:
                    break

                case = self.post_to_case(post)
                self.save_case(case)
                self.seen_ids.add(post["id"])
                cases.append(case)

                self.logger.info(f"Saved: {post['id']} - {post['title'][:50]}...")

            if not after:
                self.logger.info("Reached end of available posts")
                break

            self.logger.info(f"Progress: {len(cases)} posts saved, fetching more...")

        self.logger.info(f"Scraping complete: {len(cases)} new posts saved")
        return cases

    def scrape_top_all_time(self, max_posts: int = 500) -> List[ScrapedCase]:
        self.logger.info(f"Scraping top posts of all time (max: {max_posts})")

        cases: List[ScrapedCase] = []
        after: Optional[str] = None

        while len(cases) < max_posts:
            params: Dict[str, Any] = {"t": "all", "limit": 100}
            if after:
                params["after"] = after

            try:
                data = _fetch_reddit_json(
                    self.subreddit,
                    "/top.json",
                    params=params,
                    request_delay=self.request_delay,
                )
            except Exception as exc:
                self.logger.error(f"Failed to fetch top posts: {exc}")
                break

            listing = data.get("data", {})
            children = listing.get("children", [])
            after = listing.get("after")

            for child in children:
                if len(cases) >= max_posts:
                    break

                post_data = extract_post_data(child, min_content_length=self.min_content_length)
                if post_data and post_data["id"] not in self.seen_ids:
                    case = self.post_to_case(post_data)
                    self.save_case(case)
                    self.seen_ids.add(post_data["id"])
                    cases.append(case)

            if not after:
                break

        self.logger.info(f"Top posts scrape complete: {len(cases)} posts")
        return cases

    def scrape_pullpush_chunk(self, before: int, after_ts: int, size: int = 100) -> List[Dict[str, Any]]:
        import requests

        params = {
            "subreddit": self.subreddit,
            "before": before,
            "after": after_ts,
            "size": size,
            "sort": "desc",
            "sort_type": "created_utc",
        }

        headers = {
            "User-Agent": "MallWorldResearch/1.0 (Academic research)",
        }

        try:
            response = requests.get(PULLPUSH_BASE, params=params, headers=headers, timeout=60)
            response.raise_for_status()
            time.sleep(self.request_delay)
            data = response.json()
            return data.get("data", [])
        except Exception as exc:
            self.logger.warning(f"PullPush request failed: {exc}")
            return []

    def extract_pullpush_post(self, post: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract post data from PullPush format.

        Note: PullPush may not preserve all image metadata that Reddit's API has.
        """

        selftext = (post.get("selftext") or "").strip()
        if selftext in ["[removed]", "[deleted]"]:
            return None

        image_urls: List[str] = []
        post_url = post.get("url", "")
        if "i.redd.it" in post_url:
            image_urls.append(post_url)

        is_gallery = post.get("is_gallery", False)
        if is_gallery and post.get("media_metadata"):
            media_metadata = post.get("media_metadata", {})
            gallery_data = post.get("gallery_data", {}).get("items", [])
            for item in gallery_data:
                media_id = item.get("media_id")
                if media_id and media_id in media_metadata:
                    media = media_metadata[media_id]
                    if media.get("s", {}).get("u"):
                        import re

                        img_url = media["s"]["u"].replace("&amp;", "&")
                        if "preview.redd.it" in img_url:
                            match = re.search(r"preview\.redd\.it/([^?]+)", img_url)
                            if match:
                                img_url = f"https://i.redd.it/{match.group(1)}"
                        image_urls.append(img_url)

        has_images = len(image_urls) > 0
        if not has_images and len(selftext) < self.min_content_length:
            return None

        created_utc = int(post.get("created_utc", 0) or 0)
        created_date = datetime.fromtimestamp(created_utc, tz=timezone.utc).isoformat()
        permalink = post.get("permalink", "")

        return {
            "id": post.get("id", ""),
            "title": post.get("title", "Untitled"),
            "selftext": selftext,
            "author": post.get("author", "[deleted]"),
            "created_utc": created_utc,
            "created_date": created_date,
            "score": post.get("score", 0),
            "upvote_ratio": post.get("upvote_ratio", 0),
            "num_comments": post.get("num_comments", 0),
            "permalink": permalink,
            "url": f"{REDDIT_BASE}{permalink}",
            "link_flair_text": post.get("link_flair_text", ""),
            "image_urls": image_urls,
            "is_gallery": is_gallery,
            "post_hint": post.get("post_hint", ""),
        }

    def scrape_historical(
        self,
        chunk_days: int = 30,
        subreddit_created_utc: Optional[int] = None,
    ) -> List[ScrapedCase]:
        """Scrape complete historical data.

        Strategy:
        1. Scrape recent posts from Reddit API (archive lags behind)
        2. Scrape historical posts from PullPush archive
        """

        import math

        all_cases: List[ScrapedCase] = []

        self.logger.info("Phase 1: Scraping recent posts from Reddit API...")
        reddit_cases = self.scrape_all(max_posts=None, sort="new")
        all_cases.extend(reddit_cases)
        self.logger.info(f"Phase 1 complete: {len(reddit_cases)} posts from Reddit API")

        self.logger.info("Phase 2: Scraping historical posts from PullPush archive...")

        now = int(datetime.now(timezone.utc).timestamp())
        chunk_seconds = chunk_days * 24 * 60 * 60

        created_utc = subreddit_created_utc
        if created_utc is None:
            created_utc = get_subreddit_created_utc(self.subreddit, request_delay=self.request_delay)

        if created_utc is None:
            self.logger.warning(
                "Could not fetch subreddit created date via Reddit API; "
                "defaulting to 0. Pass --subreddit-created-utc to override."
            )
            created_utc = 0

        self.logger.info(
            f"Using {chunk_days}-day chunks (subreddit created: {datetime.fromtimestamp(created_utc).date()}); "
            "this may take a while..."
        )

        archive_cases: List[ScrapedCase] = []
        current_before = now
        total_chunks = max(1, math.ceil((now - created_utc) / chunk_seconds))
        chunk_num = 0
        empty_chunks = 0

        while current_before > created_utc:
            chunk_num += 1
            current_after = max(current_before - chunk_seconds, created_utc)

            self.logger.info(
                f"Chunk {chunk_num}/{total_chunks}: "
                f"{datetime.fromtimestamp(current_after).strftime('%Y-%m-%d')} to "
                f"{datetime.fromtimestamp(current_before).strftime('%Y-%m-%d')}"
            )

            chunk_posts: List[Dict[str, Any]] = []
            inner_before = current_before

            while True:
                posts = self.scrape_pullpush_chunk(before=inner_before, after_ts=current_after, size=100)
                if not posts:
                    break
                chunk_posts.extend(posts)

                oldest = min(int(p.get("created_utc", 0) or 0) for p in posts)
                if oldest <= current_after or oldest >= inner_before:
                    break
                inner_before = oldest

            chunk_saved = 0
            for post in chunk_posts:
                post_id = post.get("id", "")
                if not post_id or post_id in self.seen_ids:
                    continue

                post_data = self.extract_pullpush_post(post)
                if post_data:
                    case = self.post_to_case(post_data)
                    self.save_case(case)
                    self.seen_ids.add(post_id)
                    archive_cases.append(case)
                    chunk_saved += 1

            if chunk_saved > 0:
                self.logger.info(f"  Saved {chunk_saved} new posts from this chunk")
                empty_chunks = 0
            else:
                empty_chunks += 1

            current_before = current_after

            if empty_chunks > 5:
                self.logger.info("Multiple empty chunks, likely reached start of subreddit")
                break

        all_cases.extend(archive_cases)
        self.logger.info(f"Phase 2 complete: {len(archive_cases)} posts from PullPush archive")
        self.logger.info(f"Total: {len(all_cases)} posts scraped")
        return all_cases


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape posts from a Reddit subreddit")

    parser.add_argument("--subreddit", required=True, help="Subreddit name (without r/)")
    parser.add_argument(
        "--dataset",
        default=None,
        help="Output dataset directory name (default: subreddit lowercased)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent / "data",
        help="Base output directory for scraped data",
    )
    parser.add_argument(
        "--min-content-length",
        type=int,
        default=100,
        help="Minimum characters for text-only posts (image posts bypass this)",
    )
    parser.add_argument(
        "--request-delay",
        type=float,
        default=DEFAULT_REQUEST_DELAY,
        help=f"Delay between requests in seconds (default: {DEFAULT_REQUEST_DELAY})",
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=None,
        help="Maximum posts to scrape (default: unlimited)",
    )
    parser.add_argument(
        "--sort",
        choices=["new", "hot", "top"],
        default="new",
        help="Sort method for Reddit API scrape (default: new)",
    )
    parser.add_argument(
        "--include-top",
        action="store_true",
        help="Also scrape top posts of all time",
    )
    parser.add_argument(
        "--historical",
        action="store_true",
        help="Use PullPush API to scrape complete historical data",
    )
    parser.add_argument(
        "--chunk-days",
        type=int,
        default=30,
        help="Days per chunk for historical scrape (default: 30)",
    )
    parser.add_argument(
        "--subreddit-created-utc",
        type=int,
        default=None,
        help="Override subreddit creation time (UTC seconds). If omitted, fetched via Reddit API.",
    )

    args = parser.parse_args()

    scraper = RedditScraper(
        output_dir=args.output_dir,
        subreddit=args.subreddit,
        dataset=args.dataset,
        request_delay=args.request_delay,
        min_content_length=args.min_content_length,
    )

    total_cases: List[ScrapedCase] = []
    if args.historical:
        cases = scraper.scrape_historical(chunk_days=args.chunk_days, subreddit_created_utc=args.subreddit_created_utc)
        total_cases.extend(cases)
    else:
        cases = scraper.scrape_all(max_posts=args.max_posts, sort=args.sort)
        total_cases.extend(cases)

        if args.include_top:
            top_cases = scraper.scrape_top_all_time(max_posts=max(1, (args.max_posts or 500) // 2))
            total_cases.extend(top_cases)

    print(f"\nScraping complete! Total posts saved: {len(total_cases)}")
    print(f"Output directory: {scraper.output_dir}")
    print(f"Total posts in directory: {len(list(scraper.output_dir.glob('*.json')))}")


if __name__ == "__main__":
    main()
