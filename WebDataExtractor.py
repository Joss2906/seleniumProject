from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import pandas as pd

class WebDataExtractor:
    def __init__(self, config_file="config.json"):
        self.driver = webdriver.Edge()
        self.config_file = config_file
        

    def driver_options(self):
        self.driver.maximize_window()

    def read_config(self):
        try:
            with open(self.config_file, encoding='utf-8') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            print("File not found")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON")
            return None
        
    def apply_config(self):
        self.driver_options()
        config = self.read_config()

        for page in config["CONFIG"]:
            self.load_page(page["URL"])
            data = None

            for action in page["ACTIONS"]:
                if action["ACTION"] == "findTable":
                    type = action["TYPE"]
                    if "ROW_TYPE" not in action:
                        row_type = ""
                    else:
                        row_type = action["ROW_TYPE"]
                    data = self.extract_table_data(action["XPATH"], action["TYPE"], row_type)
                elif action["ACTION"] == "scroll":
                    self.scroll_down(action["PAUSE"], action["VALUE"])
                elif action["ACTION"] == "click":
                    self.click(action["XPATH"])
                elif action["ACTION"] == "input":  
                    self.input(action["XPATH"], action["VALUE"])
                elif action["ACTION"] == "wait":
                    time.sleep(action["VALUE"])
                elif action["ACTION"] == "select":
                    pass
                elif action["ACTION"] == "export" and data != None:
                    self.export_data(data, action["FILENAME"], action["TYPE"])
                else:
                    print("Invalid action")
        
        self.close_driver()

    def load_page(self, url):
        self.driver.get(url)

    def click(self, xpath):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def input(self, xpath, value):
        input_field = self.driver.find_element(By.XPATH, xpath)
        input_field.send_keys(value)
        input_field.send_keys(Keys.RETURN)

    def scroll_down(self, pause_time=5, value=0):
        height = self.driver.execute_script("return document.body.scrollHeight")
        step_height = height * (value / 100)
        last_height = 0
        new_height = height

        while last_height < new_height:
            self.driver.execute_script(f"window.scrollBy(0, {step_height});")
            time.sleep(pause_time)
            last_height += step_height
            new_height = self.driver.execute_script("return document.body.scrollHeight")


    def extract_table_data(self, xpath, type, row_type="tr"):

        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        table_data = {}

        if type == "table":
            try:
                headers = table.find_elements(By.TAG_NAME, "th")
                header_data = [header.text for header in headers]
            except:
                header_data = []
            
            tbody = table.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            body_data = []
            
            for row in rows:
                row_data = []
                cells = row.find_elements(By.TAG_NAME, "td")
                for cell in cells:
                    row_data.append(cell.text)
                body_data.append(row_data)
            
            if (header_data == []):
                header_data = body_data[0]

            table_data = {
                "headers": header_data,
                "body": body_data
            }

        elif type == "div":
            if row_type == "a":
                rows = table.find_elements(By.XPATH, ".//a")
            elif row_type == "div":
                rows = table.find_elements(By.XPATH, ".//div")
            elif row_type == "li":
                rows = table.find_elements(By.XPATH, ".//li")
            else:
                print("Invalid row type")
                return None
            
            
            data = []

            for row in rows:
                row_data = []
                cells = row.find_elements(By.XPATH, ".//*")
                count = 0
                for cell in cells:
                    count = count +1
                    if cell.text == "":
                        row_data.append("-")
                    else:
                        row_data.append(cell.text)
                data.append(row_data)

            headers = [f"column{i+1}" for i in range(count)]

            table_data = {
                "headers": headers,
                "body": data
            }

        
        elif type == "list":
            pass
        else:
            print("Invalid type")

        return table_data
    
    def export_data(self, data, filename, type):
        if type == "json":
            self.save_to_json(data, filename)
        elif type == "excel":
            self.save_to_excel(data, filename)
        else:
            print("Invalid type")

    def save_to_json(self, data, filename):
        with open("JsonExport/"+filename, "w") as file:
            json.dump(data, file, indent=4)

    def save_to_excel(self, data, filename):
        df = pd.DataFrame(data["body"], columns=data["headers"])
        df.to_excel("ExcelExport/"+filename, index=False)

    def close_driver(self):
        self.driver.quit()