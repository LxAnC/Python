# 时间：2023/7/12 11:27
# 作者：LxAnC
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return'我的名字是{0},今年{1}岁'.format(self.name,self.age)
stu=Student('张三',20)
# dir内置函数可以查看指定对象的所有的属性
print(dir(Student)) # 很多的方法可以查看，都不是我们所定义的属性
print(stu) # 输出的是一个内存地址
# _str_()方法也是object的自带的一个方法。用于返回一个对于对象的描述，对应于内置函数str（）
# 经常用于print()方法，帮助我们查看对象的信息，所以我们经常会对_str_()进行重写
# 当我使用重写__str__()方之后就可以实现这个描述输出