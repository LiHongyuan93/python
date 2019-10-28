#对文件的操作

#将小说的主要任务记录在文件中
file1 = open('name.txt','w')
file1.write('诸葛亮')
file1.close()               #写入完成记得要关闭

#读取文件
file2 = open('name.txt')
print(file2.read())

#追加写入信息
file3 = open('name.txt','a')
file3.write('刘备')
file3.close()
print(file3.read())

#逐行读入
file4 = open('name.txt', encoding='UTF-8')
print(file4.readline())

file5 = open('name.txt', encoding='UTF-8')
for line in file5.readlines():
    print(line)
    print('===')

#指针 seek
file6 = open('name.txt', encoding='UTF-8')
print(file6.tell())     #0 指针，告诉用于文件在什么位置。
file6.read(2)
print(file6.tell())     #6
file6.seek(0)        #seek可以配置两个参数，0表示把指针指向0
print(file6.tell())     #0

file6.seek(5,0)         #第一个参数代表偏移位置，第二个参数0表示从文件开头偏移，1表示从当前位置偏移，2表示从文件结尾
print('当前文件指针的位置 %s' %file6.tell())

#把末尾的'\n'删掉
for line in f.readlines():
    print(line.strip())

#当出现异常时，会自动调用finally；并且with语句可以自动帮我们调用close()方法
with open('/path/to/file','r') as f:
    print(f.read())

# 要读取非UTF-8编码的文本文件，需要给open函数传入encoding参数
f= open('/Users/michael/gbk.txt','r',encoding='gbk',errors='ignore')
f.read()

#操作目录
os.path.abspath('.')            #查看当前目录的绝对路径
os.path.join('/Users/iris','testdir')        #在某个目录下创建一个新目录
os.mkdir('/Users/iris/testdir')                #创建一个目录
os.rmdir('/Users/iris/testdir')                #删除一个目录
os.path.split('/Users/iris/testdir/file.txt')    #把一个路径拆分为两部分
os.path.splitext('/path/to/file.txt')            #可以直接得到扩展名

#操作文件
os.rename('test.txt','test.py')        #对文件重命名
os.remove('test.py')                    #删掉文件

#正则表达式,match
import re
p = re.compile(r'(\d+)-(\d+)-(\d+)')            #r:有转义字符不想让它转义的时候
p.match('2019-10-25')
year, month, day = p.match('2019-10-25').groups()
print(year,month,day)                       #2019 10 25

#搜索指定的字符串,search
import re
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print (p.search('aa2019-10-25bb'))         #<re.Match object; span=(2, 12), match='2019-10-25'>

#字符串的替换,sub
import re
phone = '123-456-789 # 电话号码'
p1 = re.sub('#.*$','',phone)
print(p1)                                       #123-456-789
p2 = re.sub('-','',p1)
print(p2)                                       #123456789

#时间与日期
import time
print(time.time())                      #1571995111.4539502
print(time.localtime())                    #time.struct_time(tm_year=2019, tm_mon=10, tm_mday=25, tm_hour=17, tm_min=18, tm_sec=31, tm_wday=4, tm_yday=298, tm_isdst=0)
print(time.strftime('%Y-%m-%d %H:%M:%S'))           #2019-10-25 17:18:31

import datetime
print(datetime.datetime.now())                      #2019-10-25 17:22:25.948455
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)            #2019-10-25 17:32:25.948455
one_day = datetime.datetime(2008,5,27)
new_date = datetime.timedelta(days=10)
print (one_day + new_date)                          #2008-06-06 00:00:00

#数学相关库，math，random
import random
print(random.randint(1,5))                          #随机输出1-5
print(random.choice(['aa','bb,''cc']))              #随机输出aa,bb,cc

#对文件和目录进行操作
import os
from os import path
print(os.path.abspath('.'))         #D:\iris.li\桌面\python_study\.idea
print(os.path.abspath('..'))        #D:\iris.li\桌面\python_study
os.path.exists('/Users')            #判断此目录/文件是否存在
os.path.isdir('/User')                #判断是否有这个文件夹
os.path.join('/tmp/a/','b/c')       #输出/tmp/a/b/c

from pathlib import Path
p = Path('.')
print(p.resolve())          #D:\iris.li\桌面\python_study\.idea
p.is_dir()
q = Path('/tmp/a/b/c')
Path.mkdir(q,parents=True)      #创建了/tmp/a/b/c

