# 时间：2023/7/12 12:28
# 作者：LxAnC
a=20
b=100
c=a+b # 两个整数类型的对象的相加操作
d=a.__add__(b) # 底层的操作是实现这个函数
print(c)
print(d)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name # 重写加法运算
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')

s=stu1+stu2 #
print(s)
'''
len
'''
lst=[11,2,2,3]
print(len(lst))
print(lst.__len__()) # 底层
print(len(stu1))

'''
new
创建对象
init
创建之后初始化
'''
class Person:

    def __new__(cls,*args,**kwargs):
        print('__new__被调用了,cls的id值是{}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为:{}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('init被调用了，self的id值为:{}'.format(id(self)))
        self.name=name
        self.age=age
print('object这个类对象的id为{}'.format(id(object)))
print('Person这个类对象的id为{}'.format(id(Person)))
print('---------  ----------')
p=Person('张三',20)
print('p的这个Person类的实例对象的id：{}'.format(id(p)))