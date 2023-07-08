# 时间：2023/7/6 1:07
# 作者：LxAnC
class Student:
    # 定义属性
    native_pace = '吉林' # 类属性

    # 实例方法
    def eat(self):  # 在类之外定义的函数，在类之内的就是方法
        print('学生在吃饭...')

    def __init__(self, name, age):
        self.name = name  # self.name叫做实体属性，进行了一个赋值的操作
        self.age = age

    # 使用静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我使用了classmethod，所以我是类方法')
# 类属性的使用方式
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)
# 类方法的使用方式
print('----------------类方法的使用方式')
Student.cm()
print('----------------类静态方法')
Student.method()

# 静态方法