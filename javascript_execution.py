# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Setup Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Define the URL
url = "https://quotes.toscrape.com/"

# load the web page
driver.get(url)

# set maximum time to load the web page in seconds
driver.implicitly_wait(10)

# Execute JavaScript to collect all links
Javacript_code = "return Array.from(document.getElementsByTagName('a'), a => a.href);"
links = driver.execute_script(Javacript_code)

pprint(links)

# Close the WebDriver
driver.quit()
