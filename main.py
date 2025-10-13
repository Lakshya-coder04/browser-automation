from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

USERNAME= os.getenv("USERNAME")
PASSWORD= os.getenv("PASSWORD")

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument("--disable-autofill")
chrome_options.add_argument("--disable-save-password-bubble")

# instance of Service, Options that we imported 
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

username_field.clear()
username_field.send_keys("lba442")
password_field.send_keys(PASSWORD)


input("PRESS ENTER TO CLOSE THE BROWSER")
driver.quit()