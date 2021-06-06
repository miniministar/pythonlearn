# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: easy_mysql
author: admin
create date: 2021/6/2 19:47
description: 
"""
import pymysql

host = 'localhost'
user = 'root'
password = 'root'
database = 'test'

try:
    # 打开数据库连接
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
except pymysql.Error as e:
    print("数据库连接失败：" + str(e))


def query_one(sql):
    one = {}
    try:
        #返回数据为字典类型{key:value}
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            one = cursor.fetchone()
    except Exception as e:
        return False
    finally:
        return one

if __name__ == "__main__":
    sql = "select id, name from user where id = 1"
    one = query_one(sql)
    print(one)

    sql = "select * from user where id = 2"
    user2 = query_one(sql)
    print(user2)
