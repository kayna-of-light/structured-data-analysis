"""
Radical Remission Project (RRP) Scraper for survivor narratives.

The Radical Remission Project (radicalremission.com) documents cases of
unexpected cancer recoveries, with testimonials organized around
Kelly Turner's "9 Key Healing Factors."

NOTE: This is a JavaScript-heavy dynamic site that may require browser
automation (Selenium/Playwright) for full content extraction.
"""

import json
import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

from scrapers.base import BaseScraper, ScrapedCase, http_get, clean_text, slugify, logger

# RRP Configuration
RRP_BASE_URL = "https://www.radicalremission.com"
RRP_STORIES_PATH = "/healing-stories/"
RRP_POST_PATTERN = r"/post/[^/]+"  # Individual stories are under /post/

# Patterns to identify actual healing/remission stories vs educational blog posts
# We want survivor stories, not general wellness articles
HEALING_STORY_INDICATORS = [
    "thriver",
    "cancer-free",
    "cancer free",
    "healed",
    "healing-story",
    "healing story",
    "featured healing",
    "survivor",
    "remission",
    "stage-i",
    "stage-ii", 
    "stage-iii",
    "stage-iv",
    "stage i",
    "stage ii",
    "stage iii",
    "stage iv",
    "diagnosed",
    "my-story",
    "my story",
]

# Patterns that indicate educational/blog posts (NOT healing stories)
BLOG_POST_INDICATORS = [
    "practices-for",
    "hidden-dangers",
    "power-of",
    "tips-for",
    "ways-to",
    "how-to",
    "what-is",
    "guide-to",
    "benefits-of",
    "netflix",
    "research-shows",
    "study-to-highlight",
]

# Kelly Turner's 9 Key Healing Factors
NINE_KEY_FACTORS = [
    "radically_changing_diet",
    "taking_control_of_health",
    "following_intuition",
    "using_herbs_supplements",
    "releasing_suppressed_emotions",
    "increasing_positive_emotions",
    "embracing_social_support",
    "deepening_spiritual_connection",
    "having_strong_reasons_for_living",
]


@dataclass
class RRPStory:
    """Parsed Radical Remission Project survivor story."""
    slug: str  # URL slug identifier
    name: str
    title: str
    diagnosis: str = ""
    story_text: str = ""
    healing_factors: List[str] = field(default_factory=list)
    image_url: Optional[str] = None
    source_url: str = ""
    date_posted: Optional[str] = None


class RadicalRemissionScraper(BaseScraper):
    """
    Scrapes survivor stories from the Radical Remission Project.
    
    The site uses dynamic JavaScript rendering, so we attempt:
    1. First, try static scraping (may get partial content)
    2. If Selenium is available, use browser automation for full content
    """
    
    source_name = "rrp"
    output_subdir = "radical_remission"
    
    def __init__(self, output_dir: Path, use_selenium: bool = True):
        """
        Initialize RRP scraper.
        
        Args:
            output_dir: Base output directory
            use_selenium: Whether to use Selenium for dynamic content
        """
        super().__init__(output_dir)
        self.use_selenium = use_selenium and SELENIUM_AVAILABLE
        self.driver: Optional[Any] = None
        
        if use_selenium and not SELENIUM_AVAILABLE:
            self.logger.warning(
                "Selenium not available. Install with: pip install selenium\n"
                "Will attempt static scraping (may miss dynamic content)"
            )
    
    def _init_driver(self) -> None:
        """Initialize Selenium WebDriver."""
        if not SELENIUM_AVAILABLE:
            return
        
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"user-agent={http_get.__globals__['USER_AGENT']}")
        
        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(10)
        except Exception as e:
            self.logger.warning(f"Failed to init Chrome driver: {e}")
            self.driver = None
    
    def _quit_driver(self) -> None:
        """Clean up Selenium WebDriver."""
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def get_story_urls_static(self) -> List[str]:
        """
        Get survivor story URLs via static scraping.
        
        Returns:
            List of story URLs
        """
        urls: List[str] = []
        page = 1
        
        while True:
            # RRP uses pagination
            if page == 1:
                url = f"{RRP_BASE_URL}{RRP_STORIES_PATH}"
            else:
                url = f"{RRP_BASE_URL}{RRP_STORIES_PATH}page/{page}/"
            
            try:
                response = http_get(url)
            except Exception as e:
                self.logger.debug(f"End of pagination at page {page}: {e}")
                break
            
            soup = BeautifulSoup(response.text, "lxml")
            
            # Find story links - look for links to individual stories
            story_links = soup.find_all("a", href=re.compile(r"/healing-stories/[^/]+/?$"))
            
            if not story_links:
                break
            
            for link in story_links:
                href = link.get("href", "")
                if href and href not in urls and href != RRP_STORIES_PATH:
                    # Ensure full URL
                    if not href.startswith("http"):
                        href = f"{RRP_BASE_URL}{href}"
                    urls.append(href)
            
            self.logger.info(f"Page {page}: found {len(story_links)} story links")
            page += 1
            
            if page > 50:  # Safety limit
                break
        
        return list(set(urls))  # Deduplicate
    
    def get_story_urls_selenium(self) -> List[str]:
        """
        Get survivor story URLs using Selenium.
        
        Returns:
            List of story URLs
        """
        if not self.driver:
            self._init_driver()
        
        if not self.driver:
            return self.get_story_urls_static()
        
        urls: List[str] = []
        
        try:
            # Collect URLs from multiple pages
            max_pages = 20
            for page_num in range(1, max_pages + 1):
                if page_num == 1:
                    url = f"{RRP_BASE_URL}{RRP_STORIES_PATH}"
                else:
                    url = f"{RRP_BASE_URL}{RRP_STORIES_PATH}page/{page_num}"
                
                self.logger.info(f"Fetching page {page_num}: {url}")
                self.driver.get(url)
                time.sleep(3)  # Wait for JS to load
                
                # Scroll down to trigger lazy loading
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                
                # Get all links on this page
                links = self.driver.find_elements(By.TAG_NAME, 'a')
                page_urls = []
                
                for link in links:
                    href = link.get_attribute('href')
                    title = link.get_attribute('title') or link.text or ""
                    
                    if href and '/post/' in href:
                        # Filter: Check if this looks like a healing story vs blog post
                        url_lower = href.lower()
                        title_lower = title.lower()
                        combined = url_lower + " " + title_lower
                        
                        # Check for exclusion patterns first (blog posts)
                        is_blog_post = any(pat in url_lower for pat in BLOG_POST_INDICATORS)
                        
                        # Check for healing story indicators
                        is_healing_story = any(pat in combined for pat in HEALING_STORY_INDICATORS)
                        
                        if is_healing_story and not is_blog_post:
                            page_urls.append(href)
                            self.logger.debug(f"  ✓ Healing story: {href}")
                        elif not is_blog_post:
                            # Ambiguous - log for review but include with lower priority
                            self.logger.debug(f"  ? Ambiguous (included): {href}")
                            page_urls.append(href)
                        else:
                            self.logger.debug(f"  ✗ Blog post (excluded): {href}")
                
                if not page_urls:
                    self.logger.info(f"No more stories found on page {page_num}")
                    break
                
                urls.extend(page_urls)
                self.logger.info(f"Page {page_num}: found {len(page_urls)} story links")
            
        except Exception as e:
            self.logger.error(f"Selenium error getting URLs: {e}")
        
        unique_urls = list(set(urls))
        self.logger.info(f"Total unique story URLs: {len(unique_urls)}")
        return unique_urls
    
    def scrape_story_static(self, url: str) -> Optional[RRPStory]:
        """
        Scrape a single survivor story via static request.
        
        Args:
            url: Story URL
            
        Returns:
            Parsed story or None
        """
        try:
            response = http_get(url)
        except Exception as e:
            self.logger.warning(f"Failed to fetch {url}: {e}")
            return None
        
        soup = BeautifulSoup(response.text, "lxml")
        
        # Extract slug from URL
        slug_match = re.search(r"/survivor-stories/([^/]+)/?", url)
        slug = slug_match.group(1) if slug_match else slugify(url)
        
        story = RRPStory(slug=slug, name="", title="", source_url=url)
        
        # Extract title
        title_elem = soup.find("h1") or soup.find("title")
        if title_elem:
            story.title = clean_text(title_elem.get_text())
            # Name is often in the title
            story.name = story.title.split("-")[0].strip() if "-" in story.title else story.title
        
        # Extract main content
        content_selectors = [
            ".entry-content",
            ".post-content",
            "article",
            ".content",
            "#content",
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                story.story_text = clean_text(content.get_text())
                break
        
        # Try to extract diagnosis from content
        diagnosis_patterns = [
            r"diagnosed with\s+([^,\.]+)",
            r"(?:cancer|tumor|carcinoma|sarcoma|lymphoma|leukemia|melanoma)\s*(?:type|stage)?[:\s]*([^,\.]+)?",
            r"stage\s+(?:I|II|III|IV|[1-4])\s+([^,\.]+)",
        ]
        
        for pattern in diagnosis_patterns:
            match = re.search(pattern, story.story_text, re.IGNORECASE)
            if match:
                story.diagnosis = clean_text(match.group(1) if match.group(1) else match.group(0))
                break
        
        # Identify mentioned healing factors
        factor_keywords = {
            "radically_changing_diet": ["diet", "nutrition", "food", "eating", "vegan", "organic"],
            "taking_control_of_health": ["control", "research", "decision", "choice", "agency"],
            "following_intuition": ["intuition", "gut feeling", "inner voice", "instinct"],
            "using_herbs_supplements": ["herbs", "supplements", "vitamins", "natural remedies"],
            "releasing_suppressed_emotions": ["emotions", "trauma", "forgiveness", "anger", "grief", "release"],
            "increasing_positive_emotions": ["positive", "joy", "happiness", "gratitude", "love"],
            "embracing_social_support": ["support", "community", "family", "friends", "network"],
            "deepening_spiritual_connection": ["spiritual", "prayer", "meditation", "faith", "god", "divine"],
            "having_strong_reasons_for_living": ["purpose", "meaning", "reasons to live", "goals", "children"],
        }
        
        text_lower = story.story_text.lower()
        for factor, keywords in factor_keywords.items():
            if any(kw in text_lower for kw in keywords):
                story.healing_factors.append(factor)
        
        return story
    
    def scrape_story_selenium(self, url: str) -> Optional[RRPStory]:
        """
        Scrape a single survivor story using Selenium.
        
        Args:
            url: Story URL
            
        Returns:
            Parsed story or None
        """
        if not self.driver:
            return self.scrape_story_static(url)
        
        try:
            self.driver.get(url)
            time.sleep(2)
            
            # Wait for content to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "article"))
            )
            
            # Get page source and parse with BeautifulSoup
            soup = BeautifulSoup(self.driver.page_source, "lxml")
            
            # Use same parsing logic as static
            slug_match = re.search(r"/survivor-stories/([^/]+)/?", url)
            slug = slug_match.group(1) if slug_match else slugify(url)
            
            story = RRPStory(slug=slug, name="", title="", source_url=url)
            
            title_elem = soup.find("h1")
            if title_elem:
                story.title = clean_text(title_elem.get_text())
                story.name = story.title.split("-")[0].strip() if "-" in story.title else story.title
            
            # Extract story content
            article = soup.find("article")
            if article:
                story.story_text = clean_text(article.get_text())
            
            return story
            
        except Exception as e:
            self.logger.warning(f"Selenium error on {url}: {e}")
            return None
    
    def story_to_case(self, story: RRPStory) -> ScrapedCase:
        """Convert RRPStory to standardized ScrapedCase."""
        return ScrapedCase(
            source="rrp",
            source_id=story.slug,
            url=story.source_url,
            title=story.title,
            date_published=story.date_posted,
            content=story.story_text,
            diagnosis=story.diagnosis,
            outcome="radical_remission",
            metadata={
                "name": story.name,
                "healing_factors": story.healing_factors,
                "image_url": story.image_url,
                "source_project": "Radical Remission Project",
            }
        )
    
    def scrape_all(self, max_stories: int = 500) -> List[ScrapedCase]:
        """
        Scrape all available survivor stories.
        
        Args:
            max_stories: Maximum number of stories to process
            
        Returns:
            List of scraped cases
        """
        cases: List[ScrapedCase] = []
        
        try:
            # Get story URLs
            if self.use_selenium:
                self._init_driver()
                urls = self.get_story_urls_selenium()
            else:
                urls = self.get_story_urls_static()
            
            self.logger.info(f"Found {len(urls)} story URLs")
            urls = urls[:max_stories]
            
            # Scrape each story
            for i, url in enumerate(urls):
                if i > 0 and i % 10 == 0:
                    self.logger.info(f"Progress: {i}/{len(urls)}")
                
                if self.use_selenium and self.driver:
                    story = self.scrape_story_selenium(url)
                else:
                    story = self.scrape_story_static(url)
                
                if story and story.story_text:
                    case = self.story_to_case(story)
                    self.save_case(case)
                    cases.append(case)
                
                time.sleep(1)  # Rate limiting
        
        finally:
            self._quit_driver()
        
        self.logger.info(f"Scraped {len(cases)} survivor stories from RRP")
        return cases


def main():
    """Run Radical Remission scraper from command line."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Scrape Radical Remission Project stories")
    parser.add_argument("--output", "-o", type=Path, default=Path("data"),
                        help="Output directory")
    parser.add_argument("--max", "-m", type=int, default=100,
                        help="Maximum stories to process")
    parser.add_argument("--no-selenium", action="store_true",
                        help="Disable Selenium, use static scraping only")
    
    args = parser.parse_args()
    
    scraper = RadicalRemissionScraper(args.output, use_selenium=not args.no_selenium)
    cases = scraper.scrape_all(max_stories=args.max)
    
    print(f"\nScraped {len(cases)} cases to {scraper.output_dir}")


if __name__ == "__main__":
    main()
