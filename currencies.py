from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import pandas as pd
from WebDataExtractor import WebDataExtractor

extractor = WebDataExtractor("currencies_config.json") 
extractor.apply_config()


# Create a new instance of the Edge drive
# driver = webdriver.Edge()

# driver.maximize_window()
# driver.get("https://coinmarketcap.com/")

# scroll_pause_time = 5  # Adjust this time as needed
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load the page
#     time.sleep(scroll_pause_time)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# height = driver.execute_script("return document.body.scrollHeight")
# step_height = height * (25 / 100)
# last_height = 0
# new_height = height

# while last_height < new_height:
#     driver.execute_script(f"window.scrollBy(0, {step_height});")
#     time.sleep(2)
#     last_height += step_height
#     new_height = driver.execute_script("return document.body.scrollHeight")


# table = WebDriverWait(driver, 10).until(
# 	# EC.presence_of_element_located((By.CLASS_NAME, "cmc-table"))

#     #FIND BY XPATH
#     EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'cmc-table')]"))
# )
# headers = table.find_elements(By.TAG_NAME, "th")
# header_data = [header.text for header in headers]

# tobody = table.find_element(By.TAG_NAME, "tbody")
# rows = tobody.find_elements(By.TAG_NAME, "tr")
# body_data = []

# for row in rows:
#     row_data = []
#     cells = row.find_elements(By.TAG_NAME, "td")
#     for cell in cells:
#         row_data.append(cell.text)
#     body_data.append(row_data)

# table_data = {
#     "headers": header_data,
#     "body": body_data
# }

# with open("currencies_data.json", "w") as file:
#     json.dump(table_data, file, indent=4)

# print("Data saved to currencies_data.json")

# df = pd.DataFrame(table_data["body"], columns=table_data["headers"])
# df.to_excel("currencies_data.xlsx", index=False)

# time.sleep(10)
# driver.quit()