# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: mul_extends
author: admin
create date: 2021/6/5 18:15
description: 
"""
'''
接口:就是一套协议规范
具体表现形式:有一堆函数,但是只明确了函数的名称,没有明确函数的具体表现
'''''
import abc
class USB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def open(self):
        pass
    @abc.abstractmethod
    def work(self):
        pass
    @abc.abstractmethod
    def close(self):
        pass

class Output(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def console(self):
        pass

class Mouse(USB):
    def open(self):
        print('mouse open')
    def work(self):
        print('mouse work')
    def close(self):
        print('mouse close')

class KeyBord:
    def open(self):
        print('KeyBoard open')

    def work(self):
        print("KeyBoard working...")

    def close(self):
        print("KeyBoard closed")

#问题是无法限制子类,必须真正的实现接口中的功能
class Camera(USB):
    def open(self):
        pass
    def work(self):
        pass
    def close(self):
        pass

class PC:
    def device(self, usb_device):
        usb_device.open()
        usb_device.work()
        usb_device.close()
    def dvd(self, dvd):
        dvd.open()
        dvd.console()
        dvd.work()
        dvd.close()

class DVD(USB, Output):
    def open(self):
        print("dvd open")
    def console(self):
        print("打印日志")
    def work(self):
        print("dvd working ...")
    def close(self):
        print("dvd close")

if __name__ == '__main__':
    #在实例化Camera  abc模块就会检查Camera是否实现了所有的抽象方法,如果没有则无法实例化
    c = Camera()
    p = PC()
    # 创建一个鼠标设备
    m = Mouse()
    #创建一个键盘设备
    key1 = KeyBord()
    #链接到电脑上
    p.device(m)
    p.device(key1)

    dvd = DVD()
    p.dvd(dvd)