# -*- coding: utf-8 -*-
#  第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计

import xlrd, re

def getTalkTime(url):
    talk_file = xlrd.open_workbook(url)
    talk_sheet = talk_file.sheets()[0]
    nrows = talk_sheet.nrows
    for i in range(1, nrows):
        yield(talk_sheet.row_values(i)[3])

def translateTimeToSec(time):
    sec = 0
    time_re = re.compile(r'(\d+)(\D+)')
    time_list = time_re.findall(time)
    for time_item in time_list:
        if time_item[1] == '秒':
            sec += int(time_item[0])
        elif time_item[1] == '分':
            sec += int(time_item[0]) * 60
        elif time_item[1] == '小时':
            sec += int(time_item[0]) * 3600
    return sec

def translateTimeToStr(time):
    s = time % 60
    m = time % 3600 // 60
    h = time // 3600
    return '%s小时%s分%s秒' % (h, m, s)

def init():
    total_time = 0
    for i in getTalkTime('0020/call_list.xls'):
        total_time += translateTimeToSec(i)
    print(total_time)
    print(translateTimeToStr(total_time))

if __name__ == "__main__":
    init()