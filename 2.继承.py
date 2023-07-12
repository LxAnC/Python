# 时间：2023/7/12 11:07
# 作者：LxAnC

'''
       动物
爬行动物    哺乳动物  动物是他们的父类
鳄鱼  蛇    老虎   狮子 动物是他们的祖先类
如果一个类没有继承任何类，那么默认就是object类
'''
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)
stu.info()
teacher.info()
