# 时间：2023/7/1 18:58
# 作者：LxAnC
# 数据类型的转换
name="张三"
age=20
print(type(name),type(age))# 说明类型不相同
# print('我叫'+name+'今年'+age+‘岁’)# 会报错
# 使用str转换
print('我叫'+name+'今年'+str(age)+'岁')# 不会报错
# str int float这三种类型的类型转换
print('---------------------------str()将其他类型转成str类型-----')
# a=10
# b=198.9
# c=False
# print(type(a),type(b),type(c))
# print(str(a),str(b),str(c))
print('---------------------------int()将其他类型转成int类型-----')
d=True
e=2.2323
f='123.123'
f1='123'
s1=29
print(d,e,f,s1)# bool转换会报错
print(int(e),int(f1))# 字符串转换时只有数字串才转换的出来，否则报错
print('---------------------------float()将其他类型转成float类型-----')
a1='123.98'
a2='32'
a3=True
a4='hello'
print(type(a1),type(a2),type(a3),type(a4))
print(float(a1),float(a2),float(a3),float(a4))# 转换时时非数字串则不允许转换

