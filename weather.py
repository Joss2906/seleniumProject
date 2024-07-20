from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import json
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from WebDataExtractor import WebDataExtractor

extractor = WebDataExtractor("config_weather.json")
extractor.apply_config()

# driver = webdriver.Edge()

# driver.get("https://www.accuweather.com/en/mx/torre%C3%B3n/242475/weather-forecast/242475?city=torre%C3%B3n")

# driver.get("https://www.accuweather.com/")
# search = driver.find_element(By.XPATH, "//form[contains(@class, 'search-form')]/input")
# search.send_keys("Torreón, COA MX")
# search.send_keys(Keys.RETURN)
# results = driver.find_element(By.XPATH, "//div[contains(@class, 'results-container')]")
# time.sleep(2)
# element = results.find_element(By.XPATH, "//p[(@class='search-bar-result__long-name' and text()='Torreón, COA MX']")
# element.click()
# results = WebDriverWait(driver, 10).until(
# 	EC.presence_of_element_located((By.CLASS_NAME, 'results-container'))
# )

# Locate the specific result with the long name "Torreón, COA MX" and click it
# result = results.find_element(By.XPATH, '//p[@class="search-bar-result__long-name" and text()="Torreón, COA MX"]')
# result = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//p[@class="search-bar-result__long-name" and text()="Torreón, COA MX"]'))
#     )
# # result.click()
# time.sleep(2)

# # table = driver.find_element(By.CLASS_NAME, "daily-list-body")
# table = driver.find_element(By.XPATH, "//div[@class='daily-list-body']")
# # print(table)
# #find all elements inside table
# rows = []

# rows = table.find_elements(By.XPATH, ".//a")
    
# if (len(rows) == 0):
# 	rows = table.find_elements(By.XPATH, ".//div")

# if (len(rows) == 0):
# 	rows = table.find_elements(By.XPATH, ".//li")
    
# # print(rows)
# headers = [f"column{i+1}" for i in range(len(rows))]
# data = []

# # rows = table.find_elements(By.CLASS_NAME, "daily-list-item")
# # rows = table.find_elements()

# for row in rows:
#     print("----------")
#     row_data = []
#     cells = row.find_elements(By.XPATH, ".//*")
	
    
	
#     for cell in cells:
#         row_data.append(cell.text)
#         print(cell.text)
#     data.append(row_data)




# 	# row_data = []
# 	# date = row.find_element(By.CLASS_NAME, "date").find_element(By.XPATH, ".//p[2]")
# 	# row_data.append(date.text)

# 	# temp = row.find_element(By.CLASS_NAME, "temp-phrase-wrapper").find_element(By.CLASS_NAME, "temp")
# 	# high_temp = temp.find_element(By.CLASS_NAME, "temp-hi")
# 	# row_data.append(high_temp.text)

# 	# low_temp = temp.find_element(By.CLASS_NAME, "temp-lo")
# 	# row_data.append(low_temp.text)

# 	# description = row.find_element(By.CLASS_NAME, "phrase").find_element(By.CLASS_NAME, "no-wrap")
# 	# row_data.append(description.text)

# 	# precipitation = row.find_element(By.CLASS_NAME, "precip")
# 	# row_data.append(precipitation.text)

# 	# # print(row_data)
# 	# data.append(row_data)

# table_data = {
# 	"headers": headers,
# 	"body": data
# }

# with open("weather.json", "w") as file:
#     json.dump(table_data, file, indent=4)
    
# print("Data saved to weather.json.json")

# # df = pd.DataFrame(table_data["body"], columns=table_data["headers"])
# # df.to_excel("weather_data.xlsx", index=False)


# time.sleep(10)
# driver.quit()


