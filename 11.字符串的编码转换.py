# 时间：2023/7/3 20:39
# 作者：LxAnC
# 为什么需要编码转换？
'''A计算机->编码（encode()）出去，然后解码到B计算机'''
s='天涯共此时'
print(s.encode(encoding='GBK'))# 一个中文两个
print(s.encode(encoding='UTF-8')) # utf-8中，一个中文占三个字符

# 编码和解码操作（格式一定要相同）
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))