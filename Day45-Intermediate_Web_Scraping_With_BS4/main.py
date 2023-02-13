from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

print(soup.a)

all_anchor_tags =  soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
    
heading = soup.find(name="h1", id="name")
company_url = soup.select_one("p a")
print(company_url)

headings = soup.select(".heading") 
print(headings)