# 时间：2023/7/3 16:47
# 作者：LxAnC
'''字符串的大小写转换操作'''
s='hello,python'
a=s.upper() # 因为是不可变序列，所以会重新创建一个新的
print(a,id(a))
print(s,id(s))
print(s.lower(),id(s.lower()))# 会重新创建一个新的
print(s,id(s))

s2='hello,Python'
print(s2.swapcase()) # 大小写互相换

print(s2.title()) # 首字母大写
