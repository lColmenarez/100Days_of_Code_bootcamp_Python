import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "/Users/lacv/Development/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com")
time.sleep(3)

driver.close()