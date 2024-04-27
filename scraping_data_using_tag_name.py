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
url = "https://www.youtube.com/@TraversyMedia/videos"

# load the web page
driver.get(url)

# set maximum time to load the web page in seconds
driver.implicitly_wait(10)

# collect data that are withing the id of contents
contents = driver.find_element(By.ID, "contents")

# 1 find the element with the specific ID you want to scrape
meta_data_elements = contents.find_elements(By.ID, "metadata-line")

# 2 collect data from span tag
meta_data = []

for element in meta_data_elements:
    # 3 collect span HTML element
    span_tags = element.find_elements(By.TAG_NAME, "span")

    # 4 collect span data
    span_data = []
    for span in span_tags:
        # 5 extract data for each span HMTL element.
        span_data.append(span.text)
    # 6 append span data to the list
    meta_data.append(span_data)

# print out the scraped data.
pprint(meta_data)

driver.quit()
