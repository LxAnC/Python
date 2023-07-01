# 时间：2023/7/1 21:58
# 作者：LxAnC
a,b=1,2
print(a==1 and b==2) # True
print(a==1 and b<2)  # False
print(a!=1 and b==2) #False
print(a!=1 and b!=2) #False
# 总结 and一边为假就为假，两边为真就为真
print('-------------or ---------------')
print(a==1 or a==2) # True
print(a!=1 or b!=2) # False
