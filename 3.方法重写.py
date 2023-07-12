# 时间：2023/7/12 11:19
# 作者：LxAnC
'''
方法重写
为什么? 当父类的方法和自己想要的不一样的时候

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
    def info(self):   #有个蓝色的图标和箭头，标识已经重写了
        super().info()
        # 可是只输出了学号没有输出name和age那么就可以使用super，以上方法
        print(self.stu_no)
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)
stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)
print('--------------')
stu.info()
teacher.info()
