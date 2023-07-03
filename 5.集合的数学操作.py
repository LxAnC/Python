# 时间：2023/7/3 15:23
# 作者：LxAnC

'''交集操作'''
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)  # 等价于intersection()，交集操作


'''并集操作'''
print(s1.union(s2))
print(s1 | s2)

print(s1)
print(s2)

'''差集操作'''
print(s1.difference((s2)))
print(s1 - s2)

'''4.对称差集'''
print(s1.symmetric_difference((s2)))
print(s1^s2)