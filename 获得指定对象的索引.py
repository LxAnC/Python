# 时间：2023/7/2 18:25
# 作者：LxAnC
lst=['hello','world',98,'hello','world',234]
print(lst.index('hello'))
# 输出为0
# 如果列表中有相同元素，只会返回第一个索引
# 如果找不存在的对象则会报错
# print(lst.index('python'))
# 还可以在指定范围内进行查找
print(lst.index('hello',1,4))#不包括3
# print(lst.index('hello',1,3))


#获取列表种指定索引的元素
#正向索引是0到n-1
# 逆向从-1开始
# 获取索引为2的元素
print(lst[2])
# 获取索引为-3的元素
print(lst[-3])
# 获取索引为10的元素
# print(lst[10]) # 如果不在这个范围则会报错indexError