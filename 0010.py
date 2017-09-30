# -*- coding: utf-8 -*-
#  第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageDraw, ImageFont
import random, string

def randomStr(leng):
    #生成大写字母和数字的组合
    str = string.ascii_uppercase + string.digits
    randomStrs = ''
    for i in range(leng):
        randomStrs += random.choice(str)
    return randomStrs

def randImgColor():
    return (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))

def randFontColor():
    return (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

def drawCodeImage():
    newImg = Image.new('RGB', (240, 60), (255, 255, 255))
    font = ImageFont.truetype('0010/font.ttf', 34)
    draw = ImageDraw.Draw(newImg)
    #设置像素颜色
    for x in range(240):
        for y in range(60):
            draw.point((x, y), fill = randImgColor())
    #设置文字
    activationCode = ''
    for i in range(4):
        createStr = randomStr(1)
        activationCode += createStr
        draw.text((60 * i + 17, 6), createStr, font = font, fill = randFontColor())
    print('create a random activation code %s' %activationCode)
    newImg.save('0010/code_img.jpg')

drawCodeImage()