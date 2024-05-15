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
from selenium.webdriver.chrome.options import Options

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Setup Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Define the URL
url = "https://www.amazon.com/AmazonBasics-Matte-Keyboard-QWERTY-Layout/dp/B07WJ5D3H4/"

# load the web page
driver.get(url)

# set maximum time to load the web page in seconds
driver.implicitly_wait(10)

# collect data that are withing the id of contents
title_element = driver.find_element(By.ID, "productTitle")

# extract the title
title = title_element.text

# show the title of the product
print(title)

# Locate the outer span by using css selector
details_elements = driver.find_elements(By.CSS_SELECTOR, 'li.a-spacing-mini')

# Loop through all located details elements
for detail_element in details_elements:
    try:
        # Extract the detail from the inner span
        detail = detail_element.find_element(By.TAG_NAME, 'span')
        print(detail.text)
    except Exception as e:
        print("Could not extract detail:", e)


driver.quit()
