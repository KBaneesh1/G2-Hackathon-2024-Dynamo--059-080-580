from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up the WebDriver
driver = webdriver.Chrome()
product_rate=[]
count = 1

def func():
    pass
# Navigate to the website

total = 42
try:
    while True:
        if(count<=total):
            state1 = driver.get(f"https://www.getapp.com/project-management-planning-software/project-management/page-{count}/")
            # time.sleep(1)
                # Wait for the repositories to be present
                # Find all repository links
            prod_links = state1.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div')
            prod_links = prod_links[1:]
            for idx, prod in enumerate(prod_links):
                print("inside for")
                product = prod.find_element(By.XPATH, ".//div[1]/div/a")
                prod_link = product.get_attribute("href")
                prod_name = product.text
                print(prod_name)
                # product.click()
                new_url = f"https://www.getapp.com/project-management-planning-software/a/{(prod_name).lower()}"
                child_state = driver.get(new_url)
                WebDriverWait(driver, 2).until(EC.url_changes(driver.current_url))
                func()
                
            
            count += 1
        else:
            break

except Exception as e:
    print(f"Error {e}")