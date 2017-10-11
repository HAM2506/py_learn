# -*- coding: utf-8 -*-

import requests, re
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

url = r'https://baike.baidu.com/item/NBA%E5%8E%86%E5%B9%B4%E5%B8%B8%E8%A7%84%E8%B5%9BMVP/15768016'

player = requests.get(url, verify = False).content

soup = BeautifulSoup(player, 'html.parser')

ol = soup.find_all('div', 'para')

f = open('nba.txt', 'w', encoding = 'utf-8')
for i in ol:
    time = i.get_text().split(' ')[0].split('—')[0]
    if re.match(r"\d+$", time) and int(time) >= 1996:
        for child in i.children:
            if isinstance(child, str):
                child = child.replace(' ', '')
                if not re.match(r'\[\d\]', child):
                    f.write(child + '\n')
            else:
                if not re.match(r'\[\d\]', child.get_text()) and child['class'] != 'sup-anchor':
                    f.write(child.get_text().replace(' ', '') + '\n')
f.close()