# 时间：2023/7/1 18:20
# 作者：LxAnC
# 整型int
# 浮点型 float
# 布尔型 bool
# 字符串 str

# 整数类型
a=10
b=0b0101
c=0o123213127
d=0xabca
print()
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

# 浮点数
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
print(n1+n2)# 会不精确
# 解决办法？
# 接入模块
# from decimal import Decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 布尔类型
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
# 可以转化为整数计算
print(f1+1)
print(f2+1)

# 字符串类型 str
# 又称为不可变的字符序列
# 单引号和双引号必须在同一行
# 三引号可以多行
str1="sadasd"
str2='asdasas'
str3='''是阿达啊
撒大苏打
撒'''
print(str1)
print(str2)
print(str3)
