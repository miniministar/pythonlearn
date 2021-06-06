# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: mysql_util
author: admin
create date: 2021/6/6 8:08
description: 
"""
from idlelib.idle_test.test_editor import insert

import pymysql

host='localhost'
username='root'
password='root'
database='test'
try:
    # 打开数据库连接
    conn = pymysql.connect(host=host, user=username, password=password, database=database)
except pymysql.Error as e:
    print("数据库连接失败：" + str(e))

def query(sql):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    except pymysql.Error as e:
        print(e)
        return None

def query_all(sql):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except pymysql.Error as e:
        print(e)
        return ()

def insert_one(sql):
    try:
        with conn.cursor() as cursor:
            execute = cursor.execute(sql)
            return execute
    except pymysql.Error as e:
        print(e)
        return 0

def test_query():
    sql = "select * from user where id = 1111"
    user = query(sql)
    if user != None:
        print(user)
    else:
        print("该用户不存在")


def test_query_all():
    sql = "select * from user limit 10, 10"
    users = query_all(sql)
    print(users)


def test_insert():
    sql = "insert into user(is_deleted, name) values(0, '李四')"
    success = insert_one(sql)
    print(success)

if __name__ == '__main__':
    # test_query()
    # test_query_all()
    test_insert()
    pass