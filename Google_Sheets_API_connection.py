import gspread
from google.oauth2.service_account import Credentials
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']

# Add your service account file
creds = Credentials.from_service_account_file('savvy-hull-341807-418f56eb2069.json', scopes=scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
sheet = client.open('NAVER_CROLLING')

# Get the first sheet of the Spreadsheet
worksheet = sheet.get_worksheet(0)

# Selenium setup
webdriver_service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI of chrome does not appear

# Driver setup
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL to the Naver product page
NAVER_STORE_URL = "https://smartstore.naver.com/effortoflife/products/5440789725"

# Get the webpage
driver.get(NAVER_STORE_URL)

# Ensure all dynamic content is loaded
driver.implicitly_wait(10)

# Parse the webpage with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all reviews
reviews = soup.find_all('span', class_='_3QDEeS6NLn')

# Iterate over the reviews and add them to the Google Sheet
for i, review in enumerate(reviews, start=1):
    worksheet.update_cell(i, 1, review.text)

# Close the driver
driver.quit()
