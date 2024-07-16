from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd

# Create a new instance of the Edge driver
driver = webdriver.Edge()

driver.get("https://www.omdbapi.com/")

button = driver.find_element(By.CSS_SELECTOR, "a[href='#parameters']")
button.click()


section = driver.find_element(By.ID, "parameters")

table = section.find_element(By.XPATH, ".//div[2]/div/div/table")

data = []

headers = table.find_elements(By.TAG_NAME, "th")
header_data = [header.text for header in headers]

tobody = table.find_element(By.TAG_NAME, "tbody")
rows = tobody.find_elements(By.TAG_NAME, "tr")
body_data = []

for row in rows:
    row_data = []
    cells = row.find_elements(By.TAG_NAME, "td")
    
    for cell in cells:
        row_data.append(cell.text)
    body_data.append(row_data)

table_data = {
    "headers": header_data,
    "body": body_data
}

with open("omdbapi_data.json", "w") as file:
    json.dump(table_data, file, indent=4)

print("Data saved to table_data.json")

df = pd.DataFrame(table_data["body"], columns=table_data["headers"])
df.to_excel("omdbapi_data.xlsx", index=False)

time.sleep(10)
driver.quit()

