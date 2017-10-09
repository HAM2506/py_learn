# -*- coding:utf-8 -*-
#**第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageDraw, ImageFont

def setMessageNum(url, num):
    if isinstance(num, int):
        num = str(num)
    #设置字体
    font = ImageFont.truetype('0000/consola.ttf', 30)
    #打开图片
    img = Image.open(url)
    #画图
    draw = ImageDraw.Draw(img)
    #设置文字位置/内容/颜色/字体
    draw.text((img.size[0] - (len(num) * 15) - 15, 10), num, (255, 0, 0), font = font)
    #保存图片
    img.save('0000/message.jpg')

setMessageNum('0000/head.jpg', 6)