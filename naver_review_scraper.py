from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


# Selenium setup
webdriver_service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI of chrome does not appear
chrome_options.binary_location = "C:/Users/YourUsername/AppData/Local/Naver/Naver Whale/Application/whale.exe"
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Driver setup
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL to the Naver product page
NAVER_STORE_URL = "https://smartstore.naver.com/effortoflife/products/5440789725"

# Get the webpage
driver.get(NAVER_STORE_URL)

# Ensure all dynamic content is loaded
driver.implicitly_wait(10)
