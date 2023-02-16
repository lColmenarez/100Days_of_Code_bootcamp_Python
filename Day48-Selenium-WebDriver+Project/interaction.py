from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("/Users/lacv/Development/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(articles.get_attribute("innerHTML"))