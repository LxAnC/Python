# 时间：2023/7/12 12:19
# 作者：LxAnC

print(dir(object))
# dir可以查看对象指向的属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
x=C('Jack',20)
print(x.__dict__) # __dict__可以查看实例对象的属性以字典方式输出
print(C.__dict__) # 实例类对象的属性
print('-------------------------')
print(x.__class__) # 输出对象所属的类
print(C.__bases__) # 输出类的父类的元组
print(C.__base__) # 输出C类第一个继承的父类(最近的)
print('-----类的层次结构')
print(C.__mro__) # 查看类的层次结构
print(A.__subclasses__()) # 查看类的子类

