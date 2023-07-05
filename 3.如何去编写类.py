# 时间：2023/7/5 22:41
# 作者：LxAnC
# class关键字
# 以下是一个student类
class Student:# Student为类的名称可以由一个或多个单词组成，每个单词的首字母大写，其余小写（规范）
    pass

# 如果是对象的话，由三部分组成，标识，类型，值
# 那么Student是对象吗
#python一切皆为对象，所Student也是对象
print('-----类的验证是否是对象-----')
print(id(Student))
print(type(Student)) #type也就是类对象
print(Student)

class Student1:
    # 定义属性
    native_pace='吉林'
    # 实例方法
    def eat(self):  # 在类之外定义的函数，在类之内的就是方法
        print('学生在吃饭...')
    def _init_(self,name,age):
        self.name=name# self.name叫做实体属性，进行了一个赋值的操作
        self.age=age
    # 使用静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod，所以我是静态方法')
    # 类方法
    @classmethod
    def cm(cls):
        print('我使用了classmethod，所以我是类方法')