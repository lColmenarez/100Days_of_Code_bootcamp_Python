import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

product_url = "https://www.amazon.com.mx/Nothing-Phone-Interface-c%C3%A1mara-Pantalla/dp/B0B76JMCM9/ref=sr_1_2?keywords=nothing+phone&qid=1676494695&sprefix=nothing%2Caps%2C227&sr=8-2&ufe=app_do%3Aamzn1.fos.66c34496-0d28-4d73-a0a1-97a8d87ec0b2"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(product_url)
time.sleep(3)

price = driver.find_element(By.CLASS_NAME , "a-offscreen")
print(price.get_attribute("innerHTML"))

driver.close()
