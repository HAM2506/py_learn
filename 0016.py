# -*- coding: utf-8 -*-
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
"""

import json, xlwt

with open('0016/number.txt', 'r') as f:
    data = json.load(f)
    # 创建 xls 文件对象
    wb = xlwt.Workbook()
    # 新增一个表单
    sh = wb.add_sheet('number')
    for i, items in enumerate(data):
        for d, item in enumerate(items):
            # 按位置添加数据
            sh.write(i, d, item)
    # 保存文件
    wb.save('0016/number.xls')