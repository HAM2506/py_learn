# -*- coding: utf-8 -*-
#   第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
# 北京
# 程序员
# 公务员
# 领导
# 牛比
# 牛逼
# 你娘
# 你妈
# love
# sex
# jiangge

import os

def exportWord(url):
    words = []
    with open(url, 'r') as f:
        for word in f:
            if word.strip() != '':
                words.append(word.strip())
    return words

input_word = input('input a word please: ')

if input_word in exportWord('0011/forbiddenword.txt'):
    print('Freedom')
else:
    print('Human Rights')