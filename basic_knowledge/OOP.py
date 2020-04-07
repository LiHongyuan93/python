#面向对象编程
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
#可以动态设置对象的属性
bart.sex=0
print(bart.sex) #0
#print(lisa.sex) #报错，不存在这个属性
#空类
class Student(object):
    pass
#变量前面加__ 则变为了private
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score


#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
dog.run() #Animal is running...

#覆盖了原方法
class Dog(Animal):
    name='small'
    def __init__(self, name="july"):
        self.name = name
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

a = list() # a是list类型
b = Animal() # b 是 Animal 类型
c = Dog() # c是Dog类型
isinstance(a, list) #True
isinstance(b, Animal) #True
isinstance(c, Dog) #True

#查看类型
print(type(123)) #<class 'int'>
import types
def fn():
    pass
type(fn)==types.FunctionType #True
type(abs)==types.BuiltinFunctionType #True
#判断类型
print(isinstance(b,Animal))#True
isinstance([1, 2, 3], (list, tuple)) #True 有一个符合则为True
#获得一个对象的所有属性和方法
print(dir('ABC'))
#判断是否存在某个属性
print(hasattr(c, 'x')) #False
print(hasattr(c, 'name')) #False
setattr(c, 'y', 19) # 设置一个属性'y'
print(getattr(c, 'y')) #19
getattr(c, 'z', 404) # 获取属性'z'，如果不存在，返回默认值 404
#类属性
class Student(object):
    name = 'Student'
s = Student()
print(s.name) # 打印 name 属性，因为实例并没有 name 属性，所以会继续 查找 class 的 name 属性
print(Student.name) # 打印类的 name 属性
s.name = 'Michael' # 给实例绑定 name 属性
print(s.name) #Michael 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的 name 属性
print(Student.name) #Student 但是类属性并未消失，用 Student.name 仍然可以 访问
del s.name # 如果删除实例的 name 属性
print(s.name) #Student 再次调用 s.name，由于实例的 name 属性没有找到，类的 name 属性就显示出来了

#动态增加方法
def set_age(self, age): # 定义一个函数作为实例方法 ...
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) #25
s2 = Student() # 创建新的实例
#s2.set_age(25) # 尝试调用方法,注意报错
#为了给所有实例都绑定方法，可以给 class 绑定方法:
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, Student)
s.set_score(100)
print(s.score) #100
#限制类的属性名
class Studenta(object):
    __slots__ = ('name', 'age') # 用 tuple 定义允许绑定的属性名称
sa = Studenta() # 创建新的实例
sa.name = 'Michael' # 绑定属性'name'
sa.age = 25 # 绑定属性'age'
print(sa.age)
#sa.score = 99 # 绑定属性'score' 报错！'Studenta' object has no attribute 'score'

#修饰器
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score = 60 # OK，实际转化为 s.set_score(60)
s.score # OK，实际转化为 s.get_score()
