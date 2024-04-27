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
import json
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

# 1 Get all the by video tite link using id video-title-link
video_elements = contents.find_elements(By.ID, "video-title-link")

# 2 collect title and link for each youtube video
titles = []
links = []

for video in video_elements:

    # 3 Extract the video title
    video_title = video.get_attribute("title")

    # 4 append the video title
    titles.append(video_title)

    # 5 Extract the video link
    video_link = video.get_attribute("href")

    # 6 append the video link
    links.append(video_link)

# Create a dictionary with keys and corresponding lists
data = {"titles": titles, "links": links}

# Serialize the dictionary to JSON
json_data = json.dumps(data)

pprint(json_data)

driver.quit()
