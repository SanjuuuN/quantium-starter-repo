from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver-win64\\chromedriver.exe")

# Open Chrome browser
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait for 5 seconds
time.sleep(5)

# Find the search box and type text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
