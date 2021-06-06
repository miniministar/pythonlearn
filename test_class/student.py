# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: student
author: admin
create date: 2021/6/5 17:02
description: 
"""
import os, sys
# print(sys.path)
curPath = os.path.dirname(os.path.abspath(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# print(curPath, rootPath)
# D:\workspace\github\pythonlearn\test_class D:\workspace\github\pythonlearn
# sys.path.append("../")
# 导入模块
from test_class.people import people
class student(people):
    grade = ''
    # 调用父类的构函
    def __init__(self, name, age, weight, grade):
        super().__init__(name, age, weight)
        self.grade = grade
    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，体重 %.1f kg，我在读 %d 年级" % (self.name, self.age, super().get_weight(), self.grade))
    def __str__(self):
        return "%s 说: 我 %d 岁了，体重 %.1f kg，我在读 %d 年级" .format (self.name, self.age, super().get_weight(), self.grade)

if __name__ == '__main__':
    # 子类实例
    student1 = student('小红', 10, 45.1, 6)
    # 子类调用重写方法
    student1.speak()
    # 用子类对象调用父类已被覆盖的方法
    super(student, student1).speak()

    print("student.__doc__:", student.__doc__)
    print("student.__name__:", student.__name__)
    print("student.__module__:", student.__module__)
    print("student.__bases__:", student.__bases__)
    print("student.__dict__:", student.__dict__)
    print(student1.__str__())