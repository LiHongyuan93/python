#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 查找某个目录下*tar结尾最后修改时间半年以前的文件并删除

import os,os.path,time,datetime

path = 'D:\iris.li\桌面\\test'
#进入到目录
os.chdir(path)
#找到以.tar结尾的文件
tar_files=[x for x in os.listdir(path) if os.path.isfile(x) and os.path.splitext(x)[1]=='.tar']
print('符合条件的tar文件列表：',tar_files)

#定义函数，遍历tar文件，获取每个文件的时间，找到时间大于半年的文件并删除
def fileremove(files):
    now=datetime.datetime.now()
    for file in files:
        file_modify_time=datetime.datetime.fromtimestamp(os.path.getmtime(file))
        if (now - file_modify_time).days > 180:
            os.remove(file)
            print('这个文件半年内未做修改，已被删除',file)

#调用函数
fileremove(tar_files)

