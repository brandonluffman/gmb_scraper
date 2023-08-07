import requests
from bs4 import BeautifulSoup 
import random

url = 'https://www.google.com/shopping/product/11415085711667766387?hl=en&q=apple+airpods+max&prds=eto:3963812343973418838_0;8191234564920633265_0;353421421838069624_0,pid:13998887421003899116,rsk:PC_7069147378898153804&sa=X&ved=0ahUKEwibv_jGx779AhUXEFkFHcCeBlkQ9pwGCBk'
# header_list = [
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_18_3) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/82.0.412.92 Safari/539.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.12; rv:87.0) Gecko/20170102 Firefox/78.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.32 (KHTML, like Gecko) Chrome/82.0.12.17 Safari/535.42'
# ]

# user_agent = random.choice(header_list)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Referer": "https://google.com/",
    "User-Agent": user_agent,
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

div_elements = soup.find_all("div", class_="UAVKwf")

for div_element in div_elements:
    a_element = div_element.find("a", class_="UxuaJe")
    if a_element:
        href_value = a_element.get("href")
        print(href_value)
    