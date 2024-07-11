from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

# Create a new instance of the Firefox driver
driver = webdriver.Edge()

driver.get("https://www.omdbapi.com/")

#click button
button = driver.find_element(By.CSS_SELECTOR, "a[href='#parameters']")
button.click()

#find section
section = driver.find_element(By.ID, "parameters")
#find table 
table = section.find_element(By.XPATH, ".//div[2]/div/div/table")

data = []
#get headers
headers = table.find_elements(By.TAG_NAME, "th")
header_data = [header.text for header in headers]


#get rows from tbody
tobody = table.find_element(By.TAG_NAME, "tbody")
rows = tobody.find_elements(By.TAG_NAME, "tr")
body_data = []
#loop through rows
for row in rows:
    row_data = []
    #get cells
    cells = row.find_elements(By.TAG_NAME, "td")
    #loop through cells
    for cell in cells:
        row_data.append(cell.text)
        # print(cell.text)
    body_data.append(row_data)

table_data = {
    "headers": header_data,
    "body": body_data
}

with open("table_data.json", "w") as file:
    json.dump(table_data, file, indent=4)

print("Data saved to table_data.json")


#wait for 2 seconds
time.sleep(10)

#close the browser
driver.quit()

