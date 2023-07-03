# 时间：2023/7/3 15:14
# 作者：LxAnC

'''两个集合是否相等'''
s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)
print(s!=s2)
'''只要内容相同，不会管顺序'''

'''判断是否是子集'''
s3={10,20,30,40,50,60}
s4={10,20,30,40}
s5={10,20,90}
'''判断子集issubset()'''
print(s4.issubset(s3))
'''判断超集issuperset()'''
print(s3.issuperset(s4))
'''判断是否没有交集'''
print(s4.isdisjoint(s5)) # 有交集为False