# 时间：2023/7/3 15:07
# 作者：LxAnC

# 这是判断操作
s={10,20,30,405,60}
# print(10 in s)
# print(100 not in s)
# print(100 in s)

'''集合元素的新增操作'''
# 新增操作 add
s.add(39)
print(s)# 已经添加进去了
'''添加多个元素的方法update'''
s.update([10,20,800])
print(s)
s.update((90,44,55))
print(s)
'''集合元素的删除操作'''
# 1.remove()
s.remove(800)
print(s) # 如果不存在会报错keyerror
# 2.discard()
s.discard(100) # 不存在不会报错
print(s)
# 3.pop()方法
s.pop() # 随机删除一个元素
print(s)
# s.pop(100)
print('pop()方法不能加参数，否则报错')
# 4.clear()方法，清空集合，输出set()
s.clear()
print(s)