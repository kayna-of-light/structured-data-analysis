"""
Reddit Mall World scraper.

Scrapes dream reports from r/TheMallWorld subreddit using Reddit's JSON API.

Usage:
    from shared.scrapers.mallworld_scraper import MallWorldScraper
    from pathlib import Path
    
    scraper = MallWorldScraper(output_dir=Path("data"))
    scraper.scrape_all()
    
    # Or scrape with limits
    scraper.scrape_all(max_posts=100)
    
CLI Usage:
    python -m shared.scrapers.mallworld_scraper --max-posts 500
"""

import argparse
import json
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

from .base import (
    BaseScraper,
    ScrapedCase,
    http_get,
    slugify,
    clean_text,
    logger,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

SUBREDDIT = "TheMallWorld"
REDDIT_JSON_BASE = f"https://www.reddit.com/r/{SUBREDDIT}"
PULLPUSH_BASE = "https://api.pullpush.io/reddit/search/submission"
REQUEST_DELAY = 2.0  # Reddit rate limits - be respectful
MIN_CONTENT_LENGTH = 100  # Minimum characters for text-only posts (image posts bypass this)
DEFAULT_MAX_POSTS = None  # No limit by default - capture everything
SUBREDDIT_CREATED = 1632355200  # Sep 23, 2021 (from screenshot)


# =============================================================================
# REDDIT API UTILITIES
# =============================================================================

def fetch_reddit_json(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Fetch JSON from Reddit's public API.
    
    Args:
        endpoint: Reddit endpoint (e.g., "/new.json")
        params: Query parameters
        
    Returns:
        Parsed JSON response
    """
    url = f"{REDDIT_JSON_BASE}{endpoint}"
    if params:
        url = f"{url}?{urlencode(params)}"
    
    # Reddit requires proper User-Agent
    import requests
    headers = {
        "User-Agent": "MallWorldResearch/1.0 (Academic research; contact: research@example.com)",
        "Accept": "application/json",
    }
    
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    time.sleep(REQUEST_DELAY)  # Respect rate limits
    
    return response.json()


def extract_image_urls(data: Dict[str, Any]) -> List[str]:
    """
    Extract image URLs from a Reddit post.
    
    Reddit stores images in multiple places:
    - `url` field for direct image links (i.redd.it)
    - `preview.images[].source.url` for preview images
    - `gallery_data` for multi-image posts
    - `media_metadata` for gallery image details
    
    Args:
        data: Reddit post data dict
        
    Returns:
        List of image URLs (i.redd.it preferred, empty if no images)
    """
    images: List[str] = []
    
    # Check if this is a direct image post (url points to i.redd.it)
    post_url = data.get("url", "")
    if "i.redd.it" in post_url:
        images.append(post_url)
    
    # Check for gallery posts (multiple images)
    if data.get("is_gallery") and data.get("media_metadata"):
        media_metadata = data.get("media_metadata", {})
        gallery_data = data.get("gallery_data", {}).get("items", [])
        
        for item in gallery_data:
            media_id = item.get("media_id")
            if media_id and media_id in media_metadata:
                media = media_metadata[media_id]
                # Get the source (full resolution) image
                if media.get("s", {}).get("u"):
                    # URL is HTML-encoded, decode it
                    img_url = media["s"]["u"].replace("&amp;", "&")
                    # Convert preview URL to i.redd.it if possible
                    if "preview.redd.it" in img_url:
                        # Extract the image ID and construct i.redd.it URL
                        # preview URLs look like: preview.redd.it/xxx.jpg?...
                        import re
                        match = re.search(r'preview\.redd\.it/([^?]+)', img_url)
                        if match:
                            img_url = f"https://i.redd.it/{match.group(1)}"
                    images.append(img_url)
    
    # Check preview images as fallback (single image posts sometimes only have this)
    if not images and data.get("preview", {}).get("images"):
        for img in data["preview"]["images"]:
            source = img.get("source", {})
            if source.get("url"):
                img_url = source["url"].replace("&amp;", "&")
                # Try to convert preview URL to i.redd.it
                if "preview.redd.it" in img_url:
                    import re
                    match = re.search(r'preview\.redd\.it/([^?]+)', img_url)
                    if match:
                        img_url = f"https://i.redd.it/{match.group(1)}"
                images.append(img_url)
    
    return images


def extract_post_data(post: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Extract relevant data from a Reddit post.
    
    Args:
        post: Reddit post data from API
        
    Returns:
        Extracted post data or None if not suitable
    """
    data = post.get("data", {})
    
    # Skip removed/deleted posts
    if data.get("removed_by_category") or data.get("selftext") in ["[removed]", "[deleted]"]:
        return None
    
    # Skip mod posts, announcements, etc.
    if data.get("stickied") or data.get("distinguished"):
        return None
    
    selftext = data.get("selftext", "").strip()
    
    # Extract image URLs
    image_urls = extract_image_urls(data)
    has_images = len(image_urls) > 0
    
    # For posts WITH images, allow shorter text (image is the content)
    # For text-only posts, require minimum content length
    if not has_images and len(selftext) < MIN_CONTENT_LENGTH:
        return None
    
    # Extract creation timestamp
    created_utc = data.get("created_utc", 0)
    created_date = datetime.fromtimestamp(created_utc, tz=timezone.utc).isoformat()
    
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
        "permalink": data.get("permalink", ""),
        "url": f"https://www.reddit.com{data.get('permalink', '')}",
        "link_flair_text": data.get("link_flair_text", ""),
        "image_urls": image_urls,
        "is_gallery": data.get("is_gallery", False),
        "post_hint": data.get("post_hint", ""),
    }


# =============================================================================
# SCRAPER CLASS
# =============================================================================

class MallWorldScraper(BaseScraper):
    """
    Scraper for r/TheMallWorld subreddit.
    
    Collects dream reports from the subreddit using Reddit's JSON API.
    Filters out short posts, removed content, and non-dream posts.
    """
    
    source_name = "mallworld"
    output_subdir = "mallworld"
    
    def __init__(self, output_dir: Path):
        """
        Initialize the Mall World scraper.
        
        Args:
            output_dir: Base output directory
        """
        super().__init__(output_dir)
        self.seen_ids: set = set()
        self._load_existing_ids()
    
    def _load_existing_ids(self) -> None:
        """Load IDs of already-scraped posts to avoid duplicates."""
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
        limit: int = 100
    ) -> tuple[List[Dict[str, Any]], Optional[str]]:
        """
        Scrape a single listing page from Reddit.
        
        Args:
            sort: Sort method ("new", "hot", "top")
            after: Pagination cursor
            limit: Number of posts per page (max 100)
            
        Returns:
            Tuple of (posts list, next after cursor)
        """
        params = {"limit": min(limit, 100)}
        if after:
            params["after"] = after
        
        endpoint = f"/{sort}.json"
        
        try:
            data = fetch_reddit_json(endpoint, params)
        except Exception as e:
            self.logger.error(f"Failed to fetch listing: {e}")
            return [], None
        
        listing = data.get("data", {})
        children = listing.get("children", [])
        next_after = listing.get("after")
        
        posts = []
        for child in children:
            post_data = extract_post_data(child)
            if post_data and post_data["id"] not in self.seen_ids:
                posts.append(post_data)
        
        return posts, next_after
    
    def post_to_case(self, post: Dict[str, Any]) -> ScrapedCase:
        """
        Convert Reddit post data to ScrapedCase.
        
        Args:
            post: Extracted post data
            
        Returns:
            ScrapedCase instance
        """
        return ScrapedCase(
            source=self.source_name,
            source_id=post["id"],
            url=post["url"],
            title=clean_text(post["title"]),
            content=clean_text(post["selftext"]) if post["selftext"] else "",
            date_published=post["created_date"],
            metadata={
                "author": post["author"],
                "score": post["score"],
                "upvote_ratio": post["upvote_ratio"],
                "num_comments": post["num_comments"],
                "flair": post.get("link_flair_text", ""),
                "image_urls": post.get("image_urls", []),
                "is_gallery": post.get("is_gallery", False),
                "post_hint": post.get("post_hint", ""),
            }
        )
    
    def scrape_all(
        self,
        max_posts: Optional[int] = DEFAULT_MAX_POSTS,
        sort: str = "new"
    ) -> List[ScrapedCase]:
        """
        Scrape all available posts from the subreddit.
        
        Args:
            max_posts: Maximum number of posts to scrape (None = no limit)
            sort: Sort method ("new", "hot", "top")
            
        Returns:
            List of scraped cases
        """
        limit_str = str(max_posts) if max_posts else "unlimited"
        self.logger.info(f"Starting scrape of r/{SUBREDDIT} (max: {limit_str}, sort: {sort})")
        
        cases: List[ScrapedCase] = []
        after = None
        total_fetched = 0
        
        while max_posts is None or len(cases) < max_posts:
            posts, after = self.scrape_listing(sort=sort, after=after)
            total_fetched += len(posts) + (100 - len(posts))  # Approximate
            
            for post in posts:
                if max_posts is not None and len(cases) >= max_posts:
                    break
                
                case = self.post_to_case(post)
                filepath = self.save_case(case)
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
        """
        Scrape top posts of all time.
        
        Args:
            max_posts: Maximum number of posts
            
        Returns:
            List of scraped cases
        """
        self.logger.info(f"Scraping top posts of all time (max: {max_posts})")
        
        cases: List[ScrapedCase] = []
        after = None
        
        while len(cases) < max_posts:
            params = {"t": "all", "limit": 100}
            if after:
                params["after"] = after
            
            try:
                data = fetch_reddit_json("/top.json", params)
            except Exception as e:
                self.logger.error(f"Failed to fetch top posts: {e}")
                break
            
            listing = data.get("data", {})
            children = listing.get("children", [])
            after = listing.get("after")
            
            for child in children:
                if len(cases) >= max_posts:
                    break
                
                post_data = extract_post_data(child)
                if post_data and post_data["id"] not in self.seen_ids:
                    case = self.post_to_case(post_data)
                    self.save_case(case)
                    self.seen_ids.add(post_data["id"])
                    cases.append(case)
            
            if not after:
                break
        
        self.logger.info(f"Top posts scrape complete: {len(cases)} posts")
        return cases

    def scrape_pullpush_chunk(
        self,
        before: int,
        after_ts: int,
        size: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Fetch posts from PullPush (Pushshift alternative) for a time window.
        
        Args:
            before: Unix timestamp upper bound
            after_ts: Unix timestamp lower bound  
            size: Number of posts per request
            
        Returns:
            List of post data
        """
        import requests
        
        params = {
            "subreddit": SUBREDDIT,
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
            time.sleep(REQUEST_DELAY)
            data = response.json()
            return data.get("data", [])
        except Exception as e:
            self.logger.warning(f"PullPush request failed: {e}")
            return []
    
    def extract_pullpush_post(self, post: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract post data from PullPush format.
        
        Note: PullPush may not preserve all image metadata that Reddit's API has.
        We extract what's available but image URLs may be incomplete for historical posts.
        """
        selftext = post.get("selftext", "").strip()
        
        # Skip removed/deleted
        if selftext in ["[removed]", "[deleted]"]:
            return None
        
        # Extract image URLs (PullPush format - may differ from Reddit API)
        image_urls: List[str] = []
        post_url = post.get("url", "")
        if "i.redd.it" in post_url:
            image_urls.append(post_url)
        
        # Check for gallery
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
                            match = re.search(r'preview\.redd\.it/([^?]+)', img_url)
                            if match:
                                img_url = f"https://i.redd.it/{match.group(1)}"
                        image_urls.append(img_url)
        
        has_images = len(image_urls) > 0
        
        # For posts WITH images, allow shorter text (image is the content)
        # For text-only posts, require minimum content length
        if not has_images and len(selftext) < MIN_CONTENT_LENGTH:
            return None
        
        created_utc = post.get("created_utc", 0)
        created_date = datetime.fromtimestamp(created_utc, tz=timezone.utc).isoformat()
        
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
            "permalink": post.get("permalink", ""),
            "url": f"https://www.reddit.com{post.get('permalink', '')}",
            "link_flair_text": post.get("link_flair_text", ""),
            "image_urls": image_urls,
            "is_gallery": is_gallery,
            "post_hint": post.get("post_hint", ""),
        }
    
    def scrape_historical(self, chunk_days: int = 30) -> List[ScrapedCase]:
        """
        Scrape complete historical data using PullPush API.
        
        Iterates backwards through time in chunks to get all posts
        since the subreddit was created.
        
        Args:
            chunk_days: Size of each time chunk in days
            
        Returns:
            List of scraped cases
        """
        import math
        
        now = int(datetime.now(timezone.utc).timestamp())
        chunk_seconds = chunk_days * 24 * 60 * 60
        
        self.logger.info(f"Starting historical scrape from subreddit creation to now")
        self.logger.info(f"Using {chunk_days}-day chunks, this may take a while...")
        
        cases: List[ScrapedCase] = []
        current_before = now
        total_chunks = math.ceil((now - SUBREDDIT_CREATED) / chunk_seconds)
        chunk_num = 0
        empty_chunks = 0
        
        while current_before > SUBREDDIT_CREATED:
            chunk_num += 1
            current_after = max(current_before - chunk_seconds, SUBREDDIT_CREATED)
            
            self.logger.info(
                f"Chunk {chunk_num}/{total_chunks}: "
                f"{datetime.fromtimestamp(current_after).strftime('%Y-%m-%d')} to "
                f"{datetime.fromtimestamp(current_before).strftime('%Y-%m-%d')}"
            )
            
            # Fetch all posts in this chunk (may need multiple requests)
            chunk_posts = []
            inner_before = current_before
            
            while True:
                posts = self.scrape_pullpush_chunk(
                    before=inner_before,
                    after_ts=current_after,
                    size=100
                )
                
                if not posts:
                    break
                
                chunk_posts.extend(posts)
                
                # Get timestamp of oldest post for pagination
                oldest = min(p.get("created_utc", 0) for p in posts)
                if oldest <= current_after or oldest >= inner_before:
                    break
                inner_before = oldest
            
            # Process posts from this chunk
            chunk_saved = 0
            for post in chunk_posts:
                post_id = post.get("id", "")
                if post_id in self.seen_ids:
                    continue
                
                post_data = self.extract_pullpush_post(post)
                if post_data:
                    case = self.post_to_case(post_data)
                    self.save_case(case)
                    self.seen_ids.add(post_id)
                    cases.append(case)
                    chunk_saved += 1
            
            if chunk_saved > 0:
                self.logger.info(f"  Saved {chunk_saved} new posts from this chunk")
                empty_chunks = 0
            else:
                empty_chunks += 1
            
            # Move to next chunk
            current_before = current_after
            
            # If we've had many empty chunks in a row, we're probably done
            if empty_chunks > 5:
                self.logger.info("Multiple empty chunks, likely reached start of subreddit")
                break
        
        self.logger.info(f"Historical scrape complete: {len(cases)} new posts saved")
        return cases


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    """Command-line entry point."""
    parser = argparse.ArgumentParser(
        description="Scrape dream reports from r/TheMallWorld"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent / "data",
        help="Output directory for scraped data"
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=DEFAULT_MAX_POSTS,
        help=f"Maximum posts to scrape (default: {DEFAULT_MAX_POSTS})"
    )
    parser.add_argument(
        "--sort",
        choices=["new", "hot", "top"],
        default="new",
        help="Sort method (default: new)"
    )
    parser.add_argument(
        "--include-top",
        action="store_true",
        help="Also scrape top posts of all time"
    )
    parser.add_argument(
        "--historical",
        action="store_true",
        help="Use PullPush API to scrape complete historical data"
    )
    parser.add_argument(
        "--chunk-days",
        type=int,
        default=30,
        help="Days per chunk for historical scrape (default: 30)"
    )
    
    args = parser.parse_args()
    
    scraper = MallWorldScraper(output_dir=args.output_dir)
    
    total_cases = []
    
    if args.historical:
        # Use PullPush for complete historical coverage
        cases = scraper.scrape_historical(chunk_days=args.chunk_days)
        total_cases.extend(cases)
    else:
        # Standard Reddit API scrape
        cases = scraper.scrape_all(max_posts=args.max_posts, sort=args.sort)
        total_cases.extend(cases)
        
        # Optionally also scrape top of all time
        if args.include_top:
            top_cases = scraper.scrape_top_all_time(max_posts=args.max_posts // 2)
            total_cases.extend(top_cases)
    
    print(f"\nScraping complete! Total posts saved: {len(total_cases)}")
    print(f"Output directory: {scraper.output_dir}")
    print(f"Total posts in directory: {len(list(scraper.output_dir.glob('*.json')))}")


if __name__ == "__main__":
    main()
