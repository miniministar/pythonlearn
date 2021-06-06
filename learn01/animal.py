# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: animal
author: admin
create date: 2021/6/5 16:16
description: 
"""
class animal:
    name = ''
    __age__ = 0
    def __init__(self, name, age):
        self.name = name
        self.__age__ = age

    def get_age(self):
        return self.__age__
    def get_name(self):
        return self.name