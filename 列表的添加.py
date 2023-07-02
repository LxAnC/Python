# 时间：2023/7/2 19:02
# 作者：LxAnC

# append()末尾添加一个元素
lst=[10,20,30]
print('原列表:',lst)
print('原标识',id(lst))
lst.append(100)
print('添加之后:',lst)
print('现标识',id(lst))

# extend()列表的末尾至少添加一个元素
lst2=['hello','world']
# lst.append(lst2) # 将lst2作为一个元素添加到末尾,就是列表嵌套列表
lst.extend(lst2) # extend的作用就是把列表分开添加
print(lst)

# insert():任意位置去添加元素
lst3=[10,20,30,'hello']
lst3.insert(1,90)
print(lst3)

# 切片,从此处添加
lst3[1:]=lst
print(lst3)
