import requests, time
from bs4 import BeautifulSoup

raw_cookies = 'JSESSIONID=A1CFF2E53F42B1494FE879EDCEE91947; DISTRIBUTED_SESSION_ID0="{\"DISTRIBUTED_SESSION_ID\":\"A1CFF2E53F42B1494FE879EDCEE91947\",\"sidToken\":\"afc66585af2ceb9b1e6b930af3acf71d\"}"; access_token=TGT-61-LoQeYwgv0IDxkOpL1y2flWTqWyWqG0FbcyBDNgGVrtiH0kRQ3M; loginCustomerId=57cd17838649a6235afb811e; language=zh-CN; username=zhangyu; timeZone=8'
cookies = {}  
for line in raw_cookies.split(';'):  
    key,value = line.split('=', 1)#1代表只分一次，得到两个数据  
    cookies[key] = value

testurl = 'http://ops.ukelink.com/login'  
s = requests.get(testurl, cookies = cookies)

soup = BeautifulSoup(s.text, "html.parser")

for link in soup.find_all('script'):
    print(link.get('src'))
# print(soup.prettify())

i = 0
while i < 5:
    i+=1
    print(i)
    time.sleep(5)