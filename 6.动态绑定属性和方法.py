# 时间：2023/7/12 10:45
# 作者：LxAnC
class Student:
    def __init__(self,name,age): # 理解为构造函数，这两个属性是每个实例对象都有的
        self.name=name
        self.age=age
    def eat(self):  # 自定义函数
        print(self.name+'在吃饭')
stu1=Student('张三',20)
stu2=Student('李四',30)
stu1.eat()
print(id(stu1))
print(id(stu2))
# 动态绑定了属性 ‘随便增加属性'
stu1.gender='女' # 只为一个实例对象创建（绑定），其他的对象没有这个属性
print(stu1.gender)
# 动态绑定方法
# 共同的方法就是方法
stu1.eat()
stu2.eat()
# 自己定义个函数
def show():
    print('定义在类之外的，叫做函数')
stu1.show=show # 直接设置名字，不能加括号
stu1.show()
