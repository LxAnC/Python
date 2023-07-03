# 时间：2023/7/3 16:40
# 作者：LxAnC

# 查询方法
'''
index()
rindex()
find()
rfind()
'''
s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))
# print(s.index('k'))# 会报错
print(s.find('k'))# 不会抛异常