# -*- coding: utf-8 -*-
"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
"""

import json, xlwt

from collections import OrderedDict

with open('0015/city.txt', 'r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    # 创建 xls 文件对象
    wb = xlwt.Workbook()
    # 新增一个表单
    sh = wb.add_sheet('city')
    for index, (key, value) in enumerate(data.items()):
        # 按位置添加数据
        sh.write(index, 0, key)
        sh.write(index, 1, value)
    # 保存文件
    wb.save('0015/city.xls')