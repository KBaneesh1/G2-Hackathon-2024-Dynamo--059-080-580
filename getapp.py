from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

product_rate = []
count = 1

options = ChromeOptions()
options.headless = False 
driver = Chrome(options=options)

total = 0
prod_link=''
r = 1
c = 1
cat = 2
col_flag = 0

with open(f'All_products.jsonl','a') as json_file:
    try:
        while True:
            count = 1
            try: 
                driver.get(f"https://www.getapp.com/browse/")
                browsing = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[1]/div/div[4]/div[{cat}]/div[2]/div[{r}]/a[{c}]').get_attribute("href")
                c += 1
                webi = driver.get(f"{browsing}/page-1/")
                try: 
                    total = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div[27]/p').text
                    total = total.split(" ")[-1]
                    print("total",total)
                    total = int(total)
                except:
                    total = 1
                
            except:
                if r == 1:
                    c = 1
                    r = 2
                    col_flag = 1
                    continue
                elif col_flag == 1:
                    c = 1
                    r = 1
                    cat += 1
                    col_flag = 0
                    continue
                else:
                    break                

            while True:
                if count <= total:
                    driver.get(f"{browsing}/page-{count}/")

                    prod_links = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div')
                    # prod_links = prod_links[1:25]
                    # print(len(prod_link))
                    for idx, prod in enumerate(prod_links):
                        # print("inside for")
                        try:
                            product = prod.find_element(By.XPATH, ".//div[1]/div/a")
                            website = prod.find_element(By.XPATH , ".//div[1]/div/div/div[1]/a")
                            prod_link = product.get_attribute("href")
                            prod_name = prod.find_element(By.XPATH, ".//div/div/div[1]/a/h2/span").text
                            # print(prod_name)    
                            # func()
                            record = {
                                "name":prod_name ,
                                "product_link":prod_link,
                            }
                            json.dump(record,json_file)
                        except:
                            continue
                    count += 1
                else:
                    print("done")
                    break

    except Exception as e:
        print(f"Error {e}")
# print(p)
driver.quit()