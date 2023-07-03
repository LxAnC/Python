# 时间：2023/7/3 17:49
# 作者：LxAnC
'''字符串的比较'''
# 比较规则 逐一比对
print('apple'>'app') # True
# 对应位置比较
print('apple'>'banana') # False
print(ord('a'),ord('b')) # 获取原始值  也就是ASCLL码
print(chr(98),chr(97))  # 与ord相对，是获取原始值的字母\
# ==和is的区别
# ==比较的是value
# is 比较的是标识
b=c='Python'
a='Python'
print(a==b)
print(c==b)
print(a is b)
# 内存驻留机制
print(a is c)
