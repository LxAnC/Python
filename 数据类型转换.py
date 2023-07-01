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
a=10
b=198.9
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))
print('---------------------------int()将其他类型转成int类型-----')
d=True
e=2.2323
f='asdadas'
print(d,e,f)
