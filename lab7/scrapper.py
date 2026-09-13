"""
Extract news headlines and hyperlinks from Hacker News (https://news.ycombinator.com/)
using requests + BeautifulSoup.
 
Install dependencies first:
    pip install requests beautifulsoup4
"""
 
import requests
from bs4 import BeautifulSoup
 
 
def get_headlines(url="https://news.ycombinator.com/"):
    """
    Fetch the page and return a list of dicts:
    [{"rank": 1, "title": "...", "link": "...", "source": "..."}, ...]
    """
    headers = {
        # A normal User-Agent avoids some sites blocking bare script requests.
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
 
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # raise an error for bad status codes (4xx/5xx)
 
    soup = BeautifulSoup(response.text, "html.parser")
 
    headlines = []
 
    # On Hacker News, each story row has the class "athing".
    # The title + link live inside a <span class="titleline"><a>...</a></span>
    story_rows = soup.find_all("tr", class_="athing")
 
    for row in story_rows:
        title_span = row.find("span", class_="titleline")
        if not title_span:
            continue
 
        link_tag = title_span.find("a")
        if not link_tag:
            continue
 
        title = link_tag.get_text(strip=True)
        link = link_tag.get("href", "")
 
        # Some links are relative (e.g. "item?id=123") for HN's own "Ask HN" posts
        if link.startswith("item?"):
            link = url.rstrip("/") + "/" + link
 
        # Try to grab the source domain shown in parentheses, e.g. "(github.com)"
        source_span = row.find("span", class_="sitestr")
        source = source_span.get_text(strip=True) if source_span else ""
 
        rank = row.get("id", "")  # HN uses the item id as the row id
 
        headlines.append({
            "rank": rank,
            "title": title,
            "link": link,
            "source": source
        })
 
    return headlines
 
 
def main():
    headlines = get_headlines()
 
    if not headlines:
        print("No headlines found. The page structure may have changed.")
        return
 
    print(f"Found {len(headlines)} headlines:\n")
    for i, item in enumerate(headlines, start=1):
        source = f" ({item['source']})" if item["source"] else ""
        print(f"{i}. {item['title']}{source}")
        print(f"   {item['link']}\n")
 
 
if __name__ == "__main__":
    main()
 