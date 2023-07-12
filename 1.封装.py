# 时间：2023/7/12 10:56
# 作者：LxAnC

# 封装：提高程序得安全性
# 继承：提高代码的复用性
# 多态：提高可扩展性
# 是所有语言都有的，是一种编程思想

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')
car=Car('宝马X5')
car.start()
print(car.brand)
# 在类外也可以访问，所以封装
# 如果不希望在类外调用函数，那么加两个__ 例如self.__brand=brand
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)
stu=Student('张三',20)
stu.show()
print(stu.name)
# print(stu.__age)报错，因为当加上了__系统就不会识别了，但是通过类里面的方法可以访问，例如C++的私有