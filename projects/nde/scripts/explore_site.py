import re
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://research.iands.org"
LIST_URL = (
    "https://research.iands.org/ndes/nde-stories/iands-nde-accounts.html?start={offset}"
)


@dataclass
class ListingEntry:
    title: str
    href: str
    date: str | None


def fetch_listing(offset: int) -> List[ListingEntry]:
    resp = requests.get(LIST_URL.format(offset=offset), timeout=60)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    entries: List[ListingEntry] = []
    records_table = soup.select_one("table")
    if records_table:
        for row in records_table.select("tr"):
            cells = row.find_all("td")
            if len(cells) != 2:
                continue
            title = cells[0].get_text(strip=True)
            date = cells[1].get_text(strip=True)
            link = cells[0].find("a")
            if not link:
                continue
            href = link.get("href", "").strip()
            if not href:
                continue
            if not href.startswith("http"):
                href = BASE_URL + href
            entries.append(ListingEntry(title=title, href=href, date=date))

    return entries


def fetch_article(url: str) -> dict:
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    title_el = (
        soup.select_one(".item-page h2")
        or soup.select_one(".item-page h1")
        or soup.select_one("article h1, article h2")
        or soup.select_one("h1, h2, h3")
    )
    title = title_el.get_text(strip=True) if title_el else ""

    date_text = None
    date_el = soup.select_one(
        ".contentpaneopen .createdate, .item-page .create, .item-page .createby"
    )
    if date_el:
        date_text = date_el.get_text(strip=True)
    else:
        # try to find textual date patterns near top
        match = re.search(r"\b\d{1,2}\s+\w+\s+\d{4}\b", soup.get_text(" "))
        if match:
            date_text = match.group(0)

    main_article = (
        soup.select_one(".item-page")
        or soup.select_one("article[itemprop='articleBody']")
        or soup.select_one("article")
    )
    paragraphs = []
    if main_article:
        for el in main_article.select("p"):
            text = el.get_text(" ", strip=True)
            if text:
                paragraphs.append(text)
    else:
        for el in soup.select("p"):
            text = el.get_text(" ", strip=True)
            if text:
                paragraphs.append(text)

    return {"title": title, "date": date_text, "content": "\n\n".join(paragraphs)}


def main() -> None:
    offsets = [0, 600]
    for offset in offsets:
        entries = fetch_listing(offset)
        print(f"Offset {offset} -> {len(entries)} entries")
        for entry in entries[:3]:
            print(f"  - {entry.title} ({entry.date}) -> {entry.href}")

    sample_url = entries[0].href if entries else None
    if sample_url:
        article = fetch_article(sample_url)
        print("Sample article:")
        for key, value in article.items():
            preview = (value[:200] + "...") if isinstance(value, str) and len(value) > 200 else value
            print(f"  {key}: {preview}")
        resp = requests.get(sample_url, timeout=60)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        headings = [
            (node.name, node.get_text(strip=True))
            for node in soup.select(".item-page h1, .item-page h2, .item-page h3")
        ]
        print(f"Sample headings ({len(headings)}):")
        for tag, text in headings[:5]:
            print(f"  {tag}: {text}")

    archive_url = (
        "https://research.iands.org/ndes/nde-stories/nde-accounts/476-archive-through-january-3-2005.html"
    )
    archive = fetch_article(archive_url)
    print("Archive page sample (first 500 chars):")
    print(archive["content"][:500])
    archive_resp = requests.get(archive_url, timeout=60)
    archive_resp.raise_for_status()
    archive_soup = BeautifulSoup(archive_resp.text, "lxml")
    archive_headings = [
        (node.name, node.get_text(strip=True))
        for node in archive_soup.select(".item-page h2, .item-page h3, .item-page h4, .item-page strong")
    ]
    print(f"Archive headings sample ({len(archive_headings)}):")
    for tag, text in archive_headings[:10]:
        print(f"  {tag}: {text}")


if __name__ == "__main__":
    main()
