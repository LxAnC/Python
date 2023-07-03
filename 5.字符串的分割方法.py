# 时间：2023/7/3 17:07
# 作者：LxAnC

'''字符串的分割'''
s='hello world python'
lst=s.split()
print(lst)
s1='hello|world|python'
print(s1.split()) # 默认看字符串中的空格进行分割
print(s1.split('|')) # 返回列表
print(s1.split(sep='|',maxsplit=1)) # 设置最大分割段数
'''split()默认从左侧开始劈分'''

print('用rsplit()分割'.center(30,'*'))
'''rsplit()从右侧开始'''
print(s.rsplit())
print(s1.rsplit('|'))
print(s.rsplit())
print(s1.rsplit(sep='|',maxsplit=1))