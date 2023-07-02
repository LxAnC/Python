# 时间：2023/7/2 19:11
# 作者：LxAnC

# remove()删除元素
lst=[10,20,30,40,50,60,30]
lst.remove(30) # 移出一个元素，有重复移除第一个
print(lst)
# lst.remove(122)  # 报错

# pop()根据索引去移除元素
lst.pop(1)
print(lst)
# lst.pop(5) # 报错，如果不存在会异常
print(lst)
lst.pop() # 如果没有参数则会删除最后一个元素
print(lst)

print('-------切片操作-删除至少一个元素,将产生一个新的列表对象--------')
new_list=lst[1:3]
print('原列表:',lst)
print('现列表:',new_list)
'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)
# clear清除所有的元素
lst.clear()
print(lst)
# 删除整个列表
del lst