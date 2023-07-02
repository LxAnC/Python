# 时间：2023/7/2 19:36
# 作者：LxAnC

# 列表
# 第一种方式 sort()方法
lst=[20,40,10,96,54]
print('排序前的列表:',lst,id(lst))
# 开始排序(升序)
lst.sort()
print('排序之后的列表:',lst,id(lst))
#开始排序(逆序)
lst.sort(reverse=True) # False表示升序排序 True表示降序排序
print('排序之后的列表:',lst,id(lst))
# 第二种方式 内置函数sorted()
print('------------使用内置函数进行排序，会产生一个新的对象-----------------')
lst=[20,40,10,98,54]
print(lst,id(lst))
sorted(lst)
print(lst,id(sorted(lst)))
print('------------也可以使用参数进行逆序--------------------------------')
print(lst,sorted(lst,reverse=True))