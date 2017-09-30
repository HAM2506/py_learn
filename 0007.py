# -*- coding: utf-8 -*-
#**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os, re

def findCodeLine(url):
    reg = re.compile(r"^#")
    code_line = 0
    exp_line = 0
    space_line = 0
    with open(url, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '':
                space_line += 1
            elif reg.findall(line.strip()):
                exp_line += 1
            else:
                code_line +=1
    fileInfo = {'code_line': code_line, 'exp_line': exp_line, 'space_line': space_line}
    return fileInfo

def findPY(url):
    for py in os.listdir(url):
        #如果是以py为后缀的文件
        if len(py.split('.')) == 2 and py.split('.')[1] == 'py':
            fileInfo = findCodeLine(url + py)
            print('file %s infomation: %s' %(url + py, fileInfo))

findPY('0007/')