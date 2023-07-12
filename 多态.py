# 时间：2023/7/12 12:11
# 作者：LxAnC
# 多态：具有多个心态
# Java是静态语言，Python是动态语言
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person:
    def eat(self):
        print('人吃五谷杂粮')

def fun(ob):
    ob.eat()

fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
