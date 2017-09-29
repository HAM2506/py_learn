# -*- coding: utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

#随机生成激活码
def randomActivationCode(leng):
    str = string.ascii_letters + string.digits
    createStr = ''
    for i in range(leng):
        # randomStr = str[random.randint(0, len(str))]
        randomStr = random.choice(str)
        createStr += randomStr
    return createStr

#随机生成num个激活码
def activationCodeCount(num, leng):
    for i in range(num):
        yield randomActivationCode(leng)

for i in activationCodeCount(2, 16):
    print(i)