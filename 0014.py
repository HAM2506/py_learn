# -*- coding: utf-8 -*-
#  第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

import os, xlwt, json

from collections import OrderedDict

if os.path.exists('0014/') == False:
    os.mkdir('0014/')

with open('0014/student.txt', 'r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    # 创建 xls 文件对象
    wb = xlwt.Workbook()
    # 新增一个表单
    sh = wb.add_sheet('student')
    for index, (key, values) in enumerate(data.items()):
        # 按位置添加数据
        sh.write(index, 0, key)
        for i, value in enumerate(values):
            sh.write(index, i + 1, value)
    # 保存文件
    wb.save('0014/student.xls')