# 时间：2023/7/3 21:27
# 作者：LxAnC
# # 1.位置实参
# def calc(a, b):  # 函数的形参，形式参数
#     c = a + b
#     return
#
#
# print(calc(1, 2))  # 实际的参数值，实参
#
#
# # 2.关键值传递
# def calc(a, b):  # 函数的形参，形式参数
#     c = a + b
#     return
#
#
# print(calc(b=1, a=2))  # 实际的参数值，实参
def fun(arg1,arg2):
    print('arg1=',arg1,id(arg1)) # 传递过来的是内存，也就是驻留机制
    print('arg2=',arg2,id(arg2))
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)
n1=11
n2=[22,33,44]
print(n1)
print(n2)
print(id(n1))
print(id(n2))
print('------------------')
fun(n1,n2)
print(n1)
print(n2)
'''
函数调用过程中，如果修改的是
不可变序列，则原实参的值不会发生改变
如果是可变序列，则原实参的值会发生改变
'''