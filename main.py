from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os


# --- Load environment variables ---
load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


class WebAutomation:
    def __init__(self):
        """Initialize the Chrome WebDriver with options."""
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Set the download path to the current working directory
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # Set up ChromeDriver
        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        """Log into the demo site."""
        self.driver.get('https://demoqa.com/login')

        # Wait for fields and fill them
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName'))
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        )
        login_button = self.driver.find_element(By.ID, 'login')

        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        """Navigate to Text Box section and fill the form."""
        driver = self.driver

        # Click on “Elements” card
        elements_card = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))
        )
        elements_card.click()

        # Click on “Text Box” in the left menu
        text_box_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-0'))
        )
        text_box_menu.click()

        # Fill in the text box form
        fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = driver.find_element(By.ID, 'userEmail')
        current_address_field = driver.find_element(By.ID, 'currentAddress')
        permanent_address_field = driver.find_element(By.ID, 'permanentAddress')
        submit_button = driver.find_element(By.ID, 'submit')

        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        """Go to Upload and Download section and trigger download."""
        driver = self.driver

        # Click on Upload and Download section
        upload_download = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-7'))
        )
        upload_download.click()

        # Download file
        download_button = driver.find_element(By.ID, 'downloadButton')
        driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        """Close the browser safely."""
        input("Press ENTER to close the browser...")
        self.driver.quit()


if __name__ == "__main__":
    webautomation = WebAutomation()
    try:
        webautomation.login(USERNAME, PASSWORD)
        webautomation.fill_form("John Smith", "john@gmail.com", "Street 1", "Street 2")
        webautomation.download()
    finally:
        webautomation.close()
