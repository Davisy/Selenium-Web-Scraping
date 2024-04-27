# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from pprint import pprint

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Setup Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Define the URL
url = "https://quotes.toscrape.com/login"


# load the web page
driver.get(url)

# set maximum time to load the web page in seconds
driver.implicitly_wait(10)

username_field = driver.find_element(By.XPATH, "//input[@name='username']")

# Enter username
username_field.send_keys("demo@example.com")

# Find the password field
password_field = driver.find_element(By.XPATH, "//input[@name='password']")

# Enter password
password_field.send_keys("secret1234")

# Submit the form
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

submit_button.click()

# Wait for the logout link to appear
try:
    logout_link = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logout')]"))
    )
    print("Login successful! Logout link was found.")
except:
    print("Login failed or logout link wasnot found.")


# Close the browser
driver.quit()
