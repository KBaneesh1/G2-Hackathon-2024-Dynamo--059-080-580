# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Set up the WebDriver
# driver = webdriver.Chrome()
# product_rate=[]

# # Navigate to the website
# driver.get("https://www.getapp.com/project-management-planning-software/a/jira/")

# # Find the elements containing the rating
# # This XPath is based on the structure you provided. Adjust it if necessary.
# items = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/span/a/div')
# print(items)
# # Iterate over each item and extract the rating
# for item in items:
#     # Use a relative XPath to find the <span> within the current item
#     element = item.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/span/a/div/span')
#     # Extract the text content of the element
#     rating = element.text
#     product_rate.append(rating)
#     #print(rating)

# # Close the browser
# print(product_rate)
# driver.quit()






from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
options = ChromeOptions()
options.headless = False  # Set to True if you don't want the browser GUI to show
driver = Chrome(options=options)
# Load the JSON file
with open('prod_links2.json', 'r') as file:
    data = json.load(file)

# Extract the links
links = data['links']

# # Set up the WebDriver
# driver = webdriver.Chrome()
product_rate = []

# Iterate over each link
for link in links:
    # Navigate to the website
    driver.get(link)

    # Find the elements containing the rating
    # This XPath is based on the structure you provided. Adjust it if necessary.
    items = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/span/a/div')
    
    # Iterate over each item and extract the rating
    for item in items:
        # Use a relative XPath to find the <span> within the current item
        element = item.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/span/a/div/span')
        # Extract the text content of the element
        rating = element.text
        product_rate.append(rating)

# Close the browser
print(product_rate)
# Write the list p to a JSON file
with open('prod_ratings.json', 'w') as json_file:
    json.dump(product_rate, json_file)
driver.quit()
