# -*- coding: utf-8 -*-
#  第 0009 题：一个HTML文件，找出里面的链接。

import requests, re

def findHref(url):
    #获取页面href部分
    reg = re.compile('href=[\S]+')
    data = requests.get(url)
    data.encoding = 'utf-8'
    content = reg.findall(data.text)
    print(content)

findHref('http://www.baidu.com')