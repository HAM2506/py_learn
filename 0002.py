# -*- coding: utf-8 -*-
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import random, string, mysql.connector

def randomActivationCode(leng):
    str = string.ascii_letters + string.digits
    createStr = ''
    for i in range(leng):
        randomStr = random.choice(str)
        createStr += randomStr
    return createStr

def activationCodeCount(num, leng):
    for i in range(num):
        yield randomActivationCode(leng)

def saveSQL(a):
    try:
        #建立数据库连接
        conn = mysql.connector.connect(user='root', password='', database='codelist')
    except:
        print("failed")
    cur = conn.cursor()
    #如果code数据表存在就删除(数据库命令)
    cur.execute("DROP TABLE IF EXISTS code")
    #生成code数据表
    # cur.execute("CREATE TABLE code(code CHAR(%s))" %16)
    cur.execute("CREATE TABLE code(code CHAR(%s))", params=[16])
    for item in a:
        print(item)
        #往code数据表中插入数据
        cur.execute("INSERT INTO code(code) VALUES(%s)", params=[item])
    print("success")
    #提交事务
    conn.commit()
    cur.close()

saveSQL(activationCodeCount(20, 16))