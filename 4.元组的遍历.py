# 时间：2023/7/3 14:47
# 作者：LxAnC

# 元组是可迭代对象，所以可以用for-in循环，因为不知道有多少个
t=('Python','world',98)
'''第一种获取元组的方式，是使用索引'''
print(t[0])
print(t[1])
print(t[2])
'''但是你不知道他到底多少个'''
'''第二种就是遍历元组'''
for item in t:
    print(item,end='\t')