from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_driver_path = Service("/Users/lacv/Development/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)


driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "date": event_names[n].text
        }
    
print(events)
driver.close()
driver.quit()