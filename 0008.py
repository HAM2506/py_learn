# -*- coding: utf-8 -*-
#  第 0008 题：一个HTML文件，找出里面的正文。

import requests, re

def findHTML(url):
    #获取页面html部分
    reg = re.compile(r'<html>[\s\S]*</html>')
    data = requests.get(url)
    data.encoding = 'utf-8'
    content = reg.findall(data.text)
    print(content)

findHTML('http://www.baidu.com')