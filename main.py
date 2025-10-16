from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

class WebAutomation:
    def __init__(self):
        # instance of Service, Options that we imported 
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        download_path = os.getcwd()
        prefs = { 'download.default_directory': download_path}  
        chrome_options.add_experimental_option('prefs', prefs)
        
    def login(self):
        pass

    def fill_form(self):
        pass

    def download(self):
        pass
    
    def close(self):
        pass
    

# Load environment variables from .env file
load_dotenv()

USERNAME= os.getenv("USERNAME")
PASSWORD= os.getenv("PASSWORD")




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


# locate the form fields and submit button 
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))

email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))

current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))

permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))

submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form fields 
fullname_field.send_keys("JOhn SMith")
email_field.send_keys("John@gmail.com")
current_address_field.send_keys("John Street 100, New York, USA")
permanent_address_field.send_keys("John Street 100, New York, USA")
driver.execute_script("arguments[0].click();", submit_button) 

# Locate the upload and download section and download  button
upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()

download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button) 

input("PRESS ENTER TO CLOSE THE BROWSER")
driver.quit()