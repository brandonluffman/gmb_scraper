from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.google.com/shopping/product/11415085711667766387?hl=en&q=apple+airpods+max&prds=eto:3963812343973418838_0;8191234564920633265_0;353421421838069624_0,pid:13998887421003899116,rsk:PC_7069147378898153804&sa=X&ved=0ahUKEwibv_jGx779AhUXEFkFHcCeBlkQ9pwGCBk'
driver = webdriver.Chrome()
driver.get(url)

div_elements = driver.find_elements(By.CSS_SELECTOR, "div.UAVKwf")

for div_element in div_elements:
    a_element = div_element.find_element(By.CSS_SELECTOR, "a.UxuaJe")
    href_value = a_element.get_attribute("href")
    
    print("href:", href_value)
    print("---------")

driver.quit()
