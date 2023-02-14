import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


product_url = "https://www.amazon.com.mx/Apple-MacBook-Pulgadas-n%C3%BAcleos-14-n%C3%BAcleos/dp/B09JR9GNJ9/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=CeIgG&content-id=amzn1.sym.77ee6ebd-83b3-45c0-be17-bf294a1da15d&pf_rd_p=77ee6ebd-83b3-45c0-be17-bf294a1da15d&pf_rd_r=QGXRQV02JSWZMTZW27MY&pd_rd_wg=UMvJX&pd_rd_r=d6e47c4c-2832-4f50-906c-ac0084fcdeb1&pd_rd_i=B09JR9GNJ9"
header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept-Language":"en-US,en;q=0.5",
    }

response = requests.get(product_url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())
price = soup.find(name='span', class_='a-offscreen').getText()
title = soup.find(id="producTitle").get_text().strip()
clean_price = price.split("$")[1]
clean_price = float(clean_price.replace(",", ""))
print(clean_price)
buy_price = 40000

if clean_price < buy_price:
    message = f"{title} is now {clean_price}"
    
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )