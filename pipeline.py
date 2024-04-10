# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # Set up the WebDriver
# driver = webdriver.Chrome()
# product_rate=[]
# count = 1

# def func():
#     pass
# # Navigate to the website

# total = 42
# try:
#     while True:
#         if(count<=total):
#             state1 = driver.get(f"https://www.getapp.com/project-management-planning-software/project-management/page-{count}/")
#             # time.sleep(1)
#                 # Wait for the repositories to be present
#                 # Find all repository links
#             prod_links = state1.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div')
#             prod_links = prod_links[1:]
#             for idx, prod in enumerate(prod_links):
#                 print("inside for")
#                 product = prod.find_element(By.XPATH, ".//div[1]/div/a")
#                 prod_link = product.get_attribute("href")
#                 prod_name = product.text
#                 print(prod_name)
#                 # product.click()
#                 new_url = f"https://www.getapp.com/project-management-planning-software/a/{(prod_name).lower()}"
#                 child_state = driver.get(new_url)
#                 WebDriverWait(driver, 2).until(EC.url_changes(driver.current_url))
#                 func()
                
            
#             count += 1
#         else:
#             break

# except Exception as e:
#     print(f"Error {e}")

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
p=[]
total = 42
try:
    while True:
        if(count<=total):
            state1 = driver.get(f"https://www.getapp.com/project-management-planning-software/project-management/page-{count}/")
            # time.sleep(1)
                # Wait for the repositories to be present
                # Find all repository links
            prod_links = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div')
            prod_links = prod_links[1:26]
            print(len(prod_links))
            for idx, prod in enumerate(prod_links):
                print("inside for")
                product = prod.find_element(By.XPATH, ".//div[1]/div/a")
                prod_link = product.get_attribute("href")
                prod_name = product.text
                print(prod_name)
                print(prod_link)
                p.append(prod_link)
                # # product.click()
                # #new_url = f"https://www.getapp.com/project-management-planning-software/a/{(prod_name).lower()}"
                # driver.get(prod_link)
                # items = driver.find_elements(By.XPATH, '//div[contains(@class, "Base_root__92vyB Base_small__ZNGz3")]')
                # # Iterate over each item and extract the rating
                # for item in items:
                #     # Use a relative XPath to find the <span> within the current item
                #     element = item.find_element(By.XPATH, './/span[@class="Typography Typography_root__FajAY Typography_tight-xxs__s2xSL Base_average__tzVJ4 RatingBase-average"]')
                #     # Extract the text content of the element
                #     rating = element.text
                #     product_rate.append(rating)
                #     print(rating)
                func()
                
            
            count += 1
            print(count)
        else:
            break

except Exception as e:
    print(f"Error {e}")
print(p)
