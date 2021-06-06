# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: file_util
author: admin
create date: 2021/6/5 18:44
description: 
"""
import os
def mkdirs(path):
    if os.path.isdir(path):
       pass
    else:
        os.makedirs(path)

def del_dirs(path):
    if os.path.isdir(path):
        os.removedirs(path)
    else:
        print("%s 文件夹不存在" % (path))

def create_file(path):
    rindex = path.rindex("/")
    if rindex != -1:
        dir = path[:rindex]
        # print(dir)
        mkdirs(dir)

    if os.path.isfile(path):
        print("file exit:" + path)
        pass
    else:
        try:
            with open(path, "w+") as fh:
                fh.close()
                print("file close:%s" %fh.closed)
        except OSError as info:
            print("打开文件失败！" + info)
    pass

if __name__ == '__main__':
    # print(os.path.isfile("../.gitignore"))
    # print(os.path.isfile("../.gitignore1"))
    # print(os.path.isdir("../file"))
    # print(os.path.isdir("../file1"))
    # mkdirs('../tmp/test')
    # del_dirs('../tmp/test')
    file = '../tmp/test/text1.txt'
    create_file(file)
    try:
        with open(file, "a+") as fd:
            msg = "将这一段话写入到文件中"
            fd.write(msg+"\n")
            fd.seek(0)
            fd_readline = fd.readline()
            print(fd_readline)
            fd.flush()
    except OSError as info:
        print("打开文件失败！" + info)