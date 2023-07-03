# 时间：2023/7/3 19:23
# 作者：LxAnC

s='hello,Python'
s1=s[:5] # 由于没有指定开始位置，默认为0
print(s1)
s2=s[6:]# 没有指定结束，默认到末尾
print(s2)
s3=s1+'!'+s2
print(s3)
'''步长'''
print(s[1:6:2])
print(s[::2]) # 两个间隔为2
print(s[::-1]) # 默认从最后面开始，到字符串的第一个字符结束
print(s[6:])