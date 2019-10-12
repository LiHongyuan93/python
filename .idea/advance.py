#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#异常捕获
try:
    year = int(input('input year:'))
except ValueError as e:                          #通用的捕获用Exception
    print('年份要输入数字 %s' %e)

##raise可以自己定义错误提示信息
try:
    raise NameError('helloError')
except Exception as e:
    print(e)

##无论name.txt是否打开成功，finally都执行
try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()

#高级特性
#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]) #['Michael', 'Sarah', 'Tracy']
print(L[-2:-1]) #['Bob']
L = list(range(100))
L[:10] #前10个
L[-10:]#后10个
L[10:20] #前10-20个
L[:10:2] #前 10 个数，每两个取一个
L[::5] #所有数，每 5 个取一个
L[:] #只写[:]就可以原样复制一个 list
(0, 1, 2, 3, 4, 5)[:3] #(0, 1, 2)
'ABCDEFG'[:3] #'ABC'
'ABCDEFG'[::2] #'ACEG'


#生成器generato，保存的是算法
L=[x * x for x in range(10)]   #列表
g=(x * x for x in range(10))    #生成器
next(g)                         #打印generator的下一个返回值

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#迭代
from collections import Iterable
isinstance('abc', Iterable) # str 是否可迭代
isinstance([1,2,3], Iterable) # list 是否可迭代
isinstance(123, Iterable) # 整数是否可迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#变量可以指向函数
x=abs(-10)      #函数调用结果赋值给变量
x=abs           #函数本身赋值给变量
abs=10
x=abs           #这时abs指向的是一个整数.注：由于abs函数实际上定义在_builtin_模块中的，所以要让修改abs变量的指向在其他模块也生效，要用_builtin_.abs=10

#map函数
def f(x):
    return x * x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))        #[1, 4, 9, 16, 25, 36, 49, 64, 81]
list(map(str,[1,2,3,4,5,6,7,8,9,0]))                    #把数字转化成字符串['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#filter过滤器
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)                            #返回的不是求和结果，而是求和函数<function lazy_sum.<locals>.sum at 0x037E86F0>
print(f())                          #调用函数f时，才真正计算求和结果 36


