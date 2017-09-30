# -*- coding: utf-8 -*-
# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
from PIL import Image

i5 = {'width': 640, 'height': 1136}

def changeSize(imgUrl, phone):
    img = Image.open(imgUrl)
    w, h = phone['width'], phone['height']
    #制造缩略
    img.thumbnail((w, h))
    saveImg(imgUrl, img)
    print(img.size)

def findJPG(url):
    for img in os.listdir(url):
        #如果是以jpg为后缀的文件
        if len(img.split('.')) == 2 and img.split('.')[1] == 'jpg':
            changeSize(url + img, i5)

def saveImg(imgUrl, img):
    #设置保存图片路径
    resultUrl = ''
    for i in range(len(imgUrl.split('/')) - 1):
        resultUrl += imgUrl.split('/')[i]
    resultUrl += '/result'
    if not os.path.isdir(resultUrl):
        os.mkdir(resultUrl)
    #保存图片
    img.save(resultUrl + '/' + imgUrl.split('/')[len(imgUrl.split('/')) - 1].split('.')[0] + '.jpg')

findJPG('0005/')