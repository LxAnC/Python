# 时间：2023/7/1 20:54
# 作者：LxAnC
# 输入函数input
# present=input('大圣想要什么礼物呢')
# print(present)
# # 课后作业
# a=int(input('输入第一个数'))
# b=int(input('输入第二个数'))
# print('他们的和是',a+b)

# 运算符
# 标准运算符
# print(1+1)
# print(1-1)
# print(1*5)
# print(2/3)
# print(2//3)
# print(2%3)
# print(2**8)

# 特别注意：一正一负的情况
# print(9//-2)
# print(-9//2)
# print(9%-4)

# 赋值运算符 从右到左
# a=3+4
# print(a)
# 链式赋值
# a=b=c=20
# print(a,type(a),b,type(b),c,type(c))
# print(id(a),id(b),id(c))

# 参数赋值
# a=2
# a*=2
# print(a)
# a/=2
# print(a)
# print(type(a))
# a*=19
# a//=3
# 除的时候会变为float类型

# 支持解包赋值//交换两个变量的值
# a,b,c=20,30,40
# print(a,b,c)
# a,b=b,a
# print(a,b)

# 比较运算符 结果都是bool类型
# …………各种大于小于
# 重点！！
a=b=10
# 一个变量由三个部分组成 地址，类型，值
# ==比较的是他们的值，
# 比较对象的地址用is
# print(a==b) # True
# print(a is b) #True
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)  #值  True
print(list1 is list2)  #id False
print(id(list1))
print(id(list2))
print(a is not b) #False a的id和b的id是相等的
print(list1 is not list2) #True list1和list2的id是不相等的

