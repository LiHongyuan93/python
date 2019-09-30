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

