# -*- coding: utf-8 -*-
#  敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

import os

def exportWord(url):
    words = []
    with open(url, 'r') as f:
        for word in f:
            if word.strip() != '':
                words.append(word.strip())
    return words

input_words = input('input a sentence please: ')

for i in exportWord('0012/forbiddenword.txt'):
    if i in input_words:
        input_words = input_words.replace(i, '**')

print(input_words)