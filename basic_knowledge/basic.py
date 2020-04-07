#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 整数变量
a=1

# 浮点数变量
b=0.1

# 字符串
c="hello world"
d='hello world'

# 字符串转义
e='I\'m ok.'

# 用r表示‘’中的字符串不转义
e2=r'I\'m ok'

# 多行字符串
e3='''line1
line2
line3'''

# 布尔
True
False
True and True
5 > 3 or 3 > 1
not True

# 空值
None

# 普通除，就算除尽结果也是浮点数
print(9 / 3) #3.0

# 地板除，其实就是取整
print(10 // 3) #3

# 求余数
print(10 % 3) #1

print(ord('A')) #65
print(ord('中')) #20013
print('中国'.encode('utf-8')) #b'\xe4\xb8\xad\xe5\x9b\xbd'
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8')) #中国
print('\u4e2d\u6587') #中文
#格式化
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('Hello, %s' % 'world') #Hello, world
print('%.2f' % 3.1415926) #3.14

#List
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0]) #Michael
print(classmates[-1]) #Tracy
print(classmates[:2]) #['Michael', 'Bob']
print(classmates[0:2]) #['Michael', 'Bob']
print(classmates[1:]) #['Bob', 'Tracy']
print(classmates[1:-1]) #['Bob']
print(classmates[:]) #['Michael', 'Bob', 'Tracy']
print(len(classmates)) #3
classmates.append('Adam')
print(classmates) #['Michael', 'Bob', 'Tracy', 'Adam']
classmates.insert(1, 'Jack')
print(classmates) #['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
classmates.pop()
print(classmates) #['Michael', 'Jack', 'Bob', 'Tracy']
print(classmates.pop(1)) #Jack
classmates[1] = 'Sarah'
print(classmates) #['Michael', 'Sarah', 'Tracy']
#list元素类型可以不同
LDemo = ['Apple', 123, True]
#可以多维
LDemo = ['Apple', [1,2], True] #注意 len(LDemo) == 3
#排序
classmates.sort()

#tuple 元组 不可更改
classmates = ('Michael', 'Bob', 'Tracy')
t = (1) #不是元组 正确写法 t = (1,)

#条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print(list(range(5))) #[0, 1, 2, 3, 4]

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n =n - 2
print(sum) #2500

#dict 键值对应,注意key是无序的
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael']) #95
d['Adam'] = 67
#print(d['a']) 因为key不存在会报错
print(d.get('a')) #None
print(d.get('a',-1)) #-1
d.pop('Bob') #移除

#set 无序且不可以重复，所以不能放入变量
s = set([1, 1, 2, 2, 3, 3])
print(s) #{1, 2, 3}
s.remove(1)
#两个set和并集 及或集合
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) #{2, 3}
print(s1 | s2) #{1, 2, 3, 4}

#数据类型转换
int('123')
int(12.34)
float('12.34')
str(1.23)
str(100)
bool(1) #True
bool('') #False

#函数
a = abs # 变量a指向abs函数
print(a(-1)) #1
#定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


