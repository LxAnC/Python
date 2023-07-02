# 时间：2023/7/3 3:45
# 作者：LxAnC

# 元组的创建方式
# 第一种用()
t=('python','world',98)
print(t)
print(type(t))
# 第二种 使用内置函数tuple()
t1=tuple(('python','world',98))
print(t1)
print(type(t1))
# 可以省略小括号
t2='pyton','world',98
print(t2)
print(type(t2))
# t4='sdad'#如果只有一个元素一定要用逗号和小括号，不然会被当成str

# 空元组，空字典，空列表的创建方式
ls3=[]
ls4=list()

d1={}
d2=dict()

# 空元组
t5=()
t6=tuple()