from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

product_rate = []
count = 1

def func():
    pass

# Set up the WebDriver
options = ChromeOptions()
options.headless = False  # Set to True if you don't want the browser GUI to show
driver = Chrome(options=options)

# Navigate to the website
total = 42
p = {"links":[]}
prod_link=''
try:
    while True:
        if count <= total:
            driver.get(f"https://www.getapp.com/project-management-planning-software/project-management/page-{count}/")

            prod_links = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div')
            prod_links = prod_links[1:25]
            print(len(prod_link))
            for idx, prod in enumerate(prod_links):
                print("inside for")
                product = prod.find_element(By.XPATH, ".//div[1]/div/a")
                prod_link = product.get_attribute("href")
                prod_name = product.text
                print(prod_name)    
                # func()
                p["links"].append(prod_link)

            count += 1
        else:
            break

except Exception as e:
    print(f"Error {e}")
print(p)
driver.quit()

# Write the list p to a JSON file
with open('prod_links.json', 'w') as json_file:
    json.dump(p, json_file)
