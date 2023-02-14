from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_wc_page = response.text

soup = BeautifulSoup(yc_wc_page, "html.parser")

article_tag = soup.find(name="a", class_="titleline")
print(article_tag)