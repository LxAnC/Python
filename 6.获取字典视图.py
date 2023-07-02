# 时间：2023/7/2 20:29
# 作者：LxAnC
scores={'张三':100,'李四':98,'王五':45}
'''keys()是获取所有的键'''
kes=scores.keys()
print(kes)
print(type(kes))
print(list(kes))
print(type(kes))
print(id(kes))
'''values()获取所有的值'''
valu=scores.values()
print(valu)
print(type(valu))
print(list(valu))
'''获取所有的键值对'''
items=scores.items()
print(items)
print(list(items))# 小括号是元组
# 转换之后的列表元素是由元组组成的
print(type(items))