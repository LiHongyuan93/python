class Animal:
    def __init__(self,age):
       self.age=age
    def __init__(self,age,xname):
        self.age=age
        self.xname=xname
    def eat(self):
        print('Animal like eating')

class dOg(Animal):
    def __init__(self,age):
        self.age=age
    def eat(self):
        print('Dog is eating ')
        super().eat()
    def run(self):
        print('Dog is running ')

class cAt(Animal):
    def __init__(self,age,xname,color):
        self.age=age
        self.xname=xname
        self.color=color
    def CatchCat(self):
        print('lucy is very good at catching cat')

def all_eat(animal):
    animal.eat()

all_eat(dOg(10))