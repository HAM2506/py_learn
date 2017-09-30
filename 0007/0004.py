# -*- coding: utf-8 -*-
#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def checkWord(url):
    with open(url, 'r') as f:
        reg = re.compile(r"\w+")
        wordObj = {}
        for line in f:
            #如果为空行
            if len(line) != 0:
                #找出一行内所有单词
                words = reg.findall(line)
                for word in words:
                    word = word.lower()
                    if word in wordObj:
                        wordObj[word] += 1
                    else:
                        wordObj[word] = 1
        return wordObj

for key, value in checkWord('0004/0004.txt').items():
    print(key, value)