# 时间：2023/7/3 22:03
# 作者：LxAnC
# 参数定义
# 默认值参数
def fun(a,b=10):
    print('{0}和{1}'.format(a,b))
fun(100) # 用默认值
fun(100,20) # 顶替默认值
# ctrl按着看print()的源码可以查看函数参数

# 个数可变的位置参数(我也不知道要传几个)
def fun1(*args):  # 个数可变地位置参数只能定义一个
    print(args)
    print(args[0])# 不过输出地是元组，不可变序列
fun1(10)
fun1(10,30)
fun1(30,405,50)

# 个数可变地关键字形参
def fun2(**args): # 个数可变地关键字参数也只能定义一个
    print(args) # 输出是字典
fun2(a=10)
fun2(a=20,b=30,c=50)

# 可以形参和实参可以换位置
def fun3(a=1,b=2,c=3):
    print(a,b,c)
lst1=[10,20,30]
fun3(*lst1)
dic={'a':123,'b':23,'c':98}
fun3(**dic)

# 设置后两个参数必须关键值参数
def fun6(a,b,*,c,d):# 后两个参数必须使用关键字参数
    pass
def fun7(*args,**args2):
    pass
def fun8(a,b,*args,**args2):
    pass
'''
在一个函数地定义过程中，既有个数可变的关键字形参也有可变的位置形参
那么一定要把位置形参放最前面(一个*号)，不然报错
def fun3(*args1,**args2):
    pass
def fun3(**args1,*args2):
    pass
'''
