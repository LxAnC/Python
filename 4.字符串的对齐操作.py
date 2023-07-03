# 时间：2023/7/3 16:51
# 作者：LxAnC

s='hello,Python'
print(s.center(20,'*'))# 减去原字符的长度，左右互相补，默认补空格
print(s.ljust(20,'*'))# 只左居中
print(s.ljust(20)) # 默认空格填充
print(s.rjust(20,'0'))
print(s.rjust(10))  # 如果小于元字符长度就是返回源字符串


'''右对齐，使用0进行填充'''
print(s.zfill(20))
print(s.zfill(10)) # 小于长度会返回元字符
print('-8910'.zfill(8))
