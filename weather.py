from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd

driver = webdriver.Edge()

driver.get("https://www.accuweather.com/en/mx/torre%C3%B3n/242475/weather-forecast/242475?city=torre%C3%B3n")

table = driver.find_element(By.CLASS_NAME, "daily-list-body")

data = []

rows = table.find_elements(By.CLASS_NAME, "daily-list-item")

for row in rows:
	row_data = []
	date = row.find_element(By.CLASS_NAME, "date").find_element(By.XPATH, ".//p[2]")
	row_data.append(date.text)

	temp = row.find_element(By.CLASS_NAME, "temp-phrase-wrapper").find_element(By.CLASS_NAME, "temp")
	high_temp = temp.find_element(By.CLASS_NAME, "temp-hi")
	row_data.append(high_temp.text)

	low_temp = temp.find_element(By.CLASS_NAME, "temp-lo")
	row_data.append(low_temp.text)

	description = row.find_element(By.CLASS_NAME, "phrase").find_element(By.CLASS_NAME, "no-wrap")
	row_data.append(description.text)

	precipitation = row.find_element(By.CLASS_NAME, "precip")
	row_data.append(precipitation.text)

	# print(row_data)
	data.append(row_data)

table_data = {
	"headers": ["Date", "High Temp", "Low Temp", "Description", "Precipitation"],
	"body": data
}

with open("weather.json", "w") as file:
    json.dump(table_data, file, indent=4)
    
print("Data saved to weather.json.json")

df = pd.DataFrame(table_data["body"], columns=table_data["headers"])
df.to_excel("weather_data.xlsx", index=False)


time.sleep(10)
driver.quit()


