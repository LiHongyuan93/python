#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Animal(object):
    def __init__(self,name):
        self.name = name

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("Animal eat meet.")

animal_01 = Animal('a1')
print(animal_01.name)





class Dog(Animal):
    def eat(self):
        print("Dog eat bone.")

    def run(self):
        print("Dog runs quickly.")

class Cat(object):
    def catch(self,*numbers):
        print("Cat can catch %s mouses." % numbers)




# animal_02 = Animal('a2')
# dog = Dog('d1')
# cat = Cat()
#
# animal_01.name = 'a2'
#
# print("animal_01 name %s" % animal_01.name)
