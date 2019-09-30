#参数定义的顺序必须是:必 选参数、默认参数、可变参数/命名关键字参数和关键字参数。
#空函数
def nop():
    pass

def my_abs(x):
    if not isinstance(x, (int, float)): #类型判断
        raise TypeError('bad operand type') #向上抛出异常
    if x >= 0:
        return x
    else:
        return -x

#多个返回值 其实就是tuple
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(100, 100, 60, math.pi / 6)) #(151.96152422706632, 70.0)
#带默认值的参数，注意默人参数不传递时不要修改默认参数的值
def power(x, n=2):
    s =1
    while n > 0:
        n-=1
        s=s* x
    return s

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#可以将list转成可变参数直接传给可变参数函数
nums = [1, 2, 3]
print(calc(*nums))
#dict形式的可变参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30) #name: Michael age: 30 other: {}
person('Adam', 45, gender='M', job='Engineer') #name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
#表示只能接受key为city或job的
def person(name, age, *, city, job):
    print(name, age, city, job)

# 列表生成式
[x*x for x in range(1,11)]  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x*x for x in range(1,11) if x % 2 == 0]    #筛选出仅偶数的平方 [4, 16, 36, 64, 100]
[m+n for m in 'ABC' for n in 'XYZ']     #可以使用两层循环生成全排列 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
import os
[d for d in os.listdir('.')]            #列出当前目录下的所有文件和目录名 ['advance.py', 'basic.py', 'high.py', 'misc.xml', 'modules.xml', 'OOP.py', 'test.py', 'vcs.xml', 'workspace.xml']
d={'x':'A','y':'B','z':'C'}
[k + '=' + v for k,v in d.items()]      #使用两个变量来生成list   ['x=A', 'y=B', 'z=C']
L=['Hello','World','IBM','Apple']
[s.lower() for s in L]                  #把所有字符串都变成小写    ['hello', 'world', 'ibm', 'apple']
x='abc'
y=123
isinstance(x,str)                       #使用内建的isinstance函数判断一个变量是不是字符串    True
isinstance(y,str)                       #使用内建的isinstance函数判断一个变量是不是字符串    False
