import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pprint import pprint

import time

start_time = time.time()

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Setup Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Define the URL
url = "https://books.toscrape.com/"

# load the web page
driver.get(url)

# Initialize empty list to store scraped data
books_results = []


while True:
    # Extract data
    for selector in driver.find_elements(By.CSS_SELECTOR, "article.product_pod"):
        try:
            title_element = selector.find_element(By.CSS_SELECTOR, "h3 > a")
            title = title_element.get_attribute("title")
            price_element = selector.find_element(By.CSS_SELECTOR, ".price_color")
            price = price_element.text
            books_results.append({"title": title, "price": price})
        except NoSuchElementException:
            # Handle the case where either title or price element is not found
            print("Title or price element not found.")
            continue

    # Check for next page link
    try:
        next_page_link_element = driver.find_element(By.CSS_SELECTOR, "li.next a")
        next_page_link = next_page_link_element.get_attribute("href")
        if next_page_link == "https://books.toscrape.com/catalogue/page-50.html":
            print("Reached the last page. Scraping process terminated.")
            break
        else:
            driver.get(next_page_link)
    except NoSuchElementException:
        # Handle the case where the next page link element is not found
        print("Next page link element not found.")
        break

# Close WebDriver
driver.quit()

pprint(books_results)
