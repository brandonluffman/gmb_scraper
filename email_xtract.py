import requests
from bs4 import BeautifulSoup

# extracted_list = open('websites.txt', 'r').readlines()
# extract = [site.replace('\n', '') for site in extracted_list if site != '-\n']
# print(extract)
import re
import time
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

res = requests.get('http://www.newmemberscleaners.com/', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.title.text)

