import requests
from bs4 import BeautifulSoup
import random
import time
header_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_18_3) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/82.0.412.92 Safari/539.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.12; rv:87.0) Gecko/20170102 Firefox/78.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.32 (KHTML, like Gecko) Chrome/82.0.12.17 Safari/535.42'
]

user_agent = random.choice(header_list)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Referer": "https://google.com/",
    "User-Agent": user_agent,
}
query = 'dry cleaners'
res = requests.get(f'https://www.google.com/search?q=dry+cleaners+arlington+va', headers=headers)
# print(res.status_code)
soup = BeautifulSoup(res.content, 'html.parser')
more_businesses_link = soup.find('a', class_='CHn7Qb') if soup.find('a', class_='CHn7Qb') else soup.find('a', class_='jRKCUd')
# print(soup.title)
# print(more_businesses_link)

results = []
if more_businesses_link is None:
    pass
else:
    more_businesses_link = more_businesses_link.get('href') 
    response = requests.get(more_businesses_link, headers=headers)
    souper = BeautifulSoup(response.content, 'html.parser')
    div_tags = souper.find_all('div', attrs={'jscontroller': 'xkZ6Lb'})  
    for tag in div_tags:
        contacts = tag.find_all('div', class_='zuotBc')
        business_name = tag.find('div', class_='rgnuSb').text if tag.find('div', 'rgnuSb') else ''
        website = tag.find('a', attrs={'aria-label': 'Website'})
        website = website.get('href') if website else ''
        phone = tag.find('a', attrs={'aria-label': 'Call'})
        phone = phone.get('data-phone-number') if phone else ''
        print(f'Business:{business_name}  ------  Website : {website}   ----   Phone : {phone}')
        results.append({
            'Business': business_name,
            'Website': website,
            'Phone Number': phone
        })
        time.sleep(1)
print(results)