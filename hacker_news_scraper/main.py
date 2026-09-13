import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select(".titleline a")

print("HACKER NEWS HEADLINES")
print("=" * 60)

for i, article in enumerate(articles, 1):
    headline = article.get_text(strip=True)
    link = article.get("href")

    print(f"\n{i}. {headline}")
    print(f"   Link: {link}")