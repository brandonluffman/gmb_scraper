from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
driver = webdriver.Chrome()
#London Victoria & Albert Museum URL
url = 'https://www.google.com/search?q=dry+cleaners'
driver.get(url)

# Define the maximum number of pages to iterate through
max_pages = 2

more_businesses_link = driver.find_element(By.XPATH, "//div[@class='S8ee5 CwbYXd wHYlTd']")
if more_businesses_link:
    more_businesses_link.click()
results = []
website_links = []
for page_num in range(max_pages):
    div_tags = driver.find_elements(By.XPATH, "//div[@jscontroller='xkZ6Lb']")
    print(len(div_tags))
    for tag in div_tags:
        business_name = tag.find_element(By.CLASS_NAME,'rgnuSb').text
        try:
            if tag.find_element(By.CSS_SELECTOR, "[aria-label='Website']"):
                website = tag.find_element(By.CSS_SELECTOR, "[aria-label='Website']").get_attribute('href')
            else:
                website = 'google.com'
        except:
           website = '-'
        try:
            if tag.find_element(By.CSS_SELECTOR, "[aria-label='Call']"):
                phone = tag.find_element(By.CSS_SELECTOR, "[aria-label='Call']").get_attribute('data-phone-number') 
            else:
                phone = '-'
        except:
            print('No Phone')
            phone = '888'
        print(f'Business: {business_name} ------ Website: {website} ---- Phone: {phone}')
        results.append({
            'Business': business_name,
            'Website': website,
            'Phone Number': phone
        })
        website_links.append(website)
        time.sleep(1)
    wait = WebDriverWait(driver, 10)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next >']")))
    next_button.click()
    time.sleep(2)
    print(driver.title)
           
else:
    print('No Button Found')

driver.quit()
with open('contacts.json', 'w') as f:
    for result in results:
        f.write(json.dumps(result))

with open('websites.txt', 'a') as f:
    for website in website_links:
        f.write(website)
        f.write(f'\n')