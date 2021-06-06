# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: people
author: admin
create date: 2021/6/5 17:00
description: 
"""
#类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print("%s 说： 我 %d 岁, 体重 %f kg。" % (self.name, self.age, self.__weight))
    def get_weight(self):
        return self.__weight