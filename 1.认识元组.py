# 时间：2023/7/3 3:36
# 作者：LxAnC


# 可变序列：列表、字典
# 可以对序列执行增删改操作，对象地址不发生更改
lst=[10,20,45]
print(id(lst))
lst.insert(1,'hello')
print(id(lst))
print(lst)
print(lst) # 可变序列增加后不会改变地址
# 元组是一个python内置的数据结构之一，是一个不可变序列
# 用小括号

# 不可变序列与可变序列
# 不可变序列：字符串、元组
# 没有增删改的操作
s='hello'
print(id(s))
s=s+'world'
print(id(s))


