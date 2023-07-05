# 时间：2023/7/5 22:51
# 作者：LxAnC
class Student1:
    # 定义属性
    native_pace = '吉林'

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


# 语法：实例名=类名()
# 创建Student1的对象
stu1 = Student1('张三',20) # 他是如何知道张三和20是哪个类的呢，原来就是有个类指针
print(id(stu1))
print(type(stu1))
print(stu1)  # 实际上是输出的是stu1的内存地址(十六进制)
print('------')
print(id(Student1))
print(type(Student1))
print(Student1)# 两个不同

stu1.eat() # 调用方法
print(stu1.name,stu1.age) # 都可以用.来访问，来调用
print('----------------')
Student1.eat(stu1) # 这也是另一种用法，都是相同的 这里面的stu1其实就是定义时候的self(自己)