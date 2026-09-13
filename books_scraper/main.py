import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("books.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Title", "Price", "Availability"])

    for book in books:

        title = book.find("h3").find("a")["title"]

        price = book.find("p", class_="price_color").text.strip()

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        writer.writerow([title, price, availability])

print("Data successfully saved to books.csv")