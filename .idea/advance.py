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

#迭代
from collections import Iterable
isinstance('abc', Iterable) # str 是否可迭代
isinstance([1,2,3], Iterable) # list 是否可迭代
isinstance(123, Iterable) # 整数是否可迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#filter过滤器
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
