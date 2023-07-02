# 时间：2023/7/2 15:44
# 作者：LxAnC
# range内置函数
# 目前已经学了的input(),print()

# 语法:range(整数) 返回0到整数的
# 第一种方式  一个参数
a=range(5) # 列表，一个参数就是默认0开始，默认相差1----步长
print(a)
print(list(a))
# 第二种方式  两个参数包含开始和结束
r=range(1,10)
# 不包含10
print(r)
print(list(r))
# 第三种方式  三个参数包含开始，结束，还有步长
b=range(1,10,2)
print(b)
print(list(b))
'''判断指定的值是否在序列中存在'''
# in,not in
print(0 in r)
print(9 in b) # 在当前的序列中
print(0 not in r)# 10不在里面


'''优点：不管长度为多长，占用空间都是一样的
是一个迭代器，只有当用range函数之间的对象的时候，才会来计算
可以使用in或者not in判断是否在序列中
'''
