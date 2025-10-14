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

# instance of Service, Options that we imported 
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

#load the webpage
driver.get('https://demoqa.com/login')

# getting username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in the username and password , click login
username_field.send_keys("lba442")
password_field.send_keys(PASSWORD)
driver.execute_script("arguments[0].click();", login_button) #executing javascript code


#locate the elements dropdown and text box 
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))

elements.click()  

text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()


# locate the form fields 
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))

email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))

current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))

permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentA')))

login_button = driver.find_element(By.ID, 'login')

# Fill in the form fields 

input("PRESS ENTER TO CLOSE THE BROWSER")
driver.quit()