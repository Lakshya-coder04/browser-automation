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


class WebAutomation:
    def __init__(self):
        # instance of Service, Options that we imported 
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        
        download_path = os.getcwd()
        prefs = { 'download.default_directory': download_path}  
        chrome_options.add_experimental_option('prefs', prefs)   
        
        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        
    def login(self, USERNAME, PASSWORD):
        #load the webpage
        self.driver.get('https://demoqa.com/login')

        # getting username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in the username and password , click login
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        self.driver.execute_script("arguments[0].click();", login_button) #executing javascript code


    def fill_form(self, fullname, email, current_address, permanent_address):
        # create automation instance and expose driver variable, then login before further actions
        automation = WebAutomation()
        driver = automation.driver
        automation.login()

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
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        driver.execute_script("arguments[0].click();", submit_button) 


        

    def download(self):
        # Locate the upload and download section and download  button
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button) 


    def close(self):
        input("PRESS ENTER TO CLOSE THE BROWSER")
        self.driver.quit()
    


if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login(USERNAME, PASSWORD)
    webautomation.fill_form("John Smith", "John@gmail.com", "Street 1", "Street 2")
    webautomation.download()
    webautomation.close()