# -*- coding: utf-8 -*-
#**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os, re

def findTXT(url):
    for txt in os.listdir(url):
        #如果是以txt为后缀的文件
        if len(txt.split('.')) == 2 and txt.split('.')[1] == 'txt':
            findWord(url + txt)

def findWord(txt):
    mostCountWord = ''
    mostCount = 0
    with open(txt, 'r') as f:
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
        for word, value in wordObj.items():
            if value > mostCount:
                mostCountWord = word
                mostCount = value
    print(mostCountWord, mostCount)

findTXT('0006/')