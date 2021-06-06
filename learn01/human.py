# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: human
author: admin
create date: 2021/6/5 16:23
description: 
"""
from learn01.animal import animal
class human(animal):
    sex = ''
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex
    def get(self):
        return "name=" + self.name + "\nage=" + str(super().get_age()) + "\nsex=" + self.sex

if __name__ == "__main__":
    person1 = human("张三", 20, "男")
    print(person1.get())