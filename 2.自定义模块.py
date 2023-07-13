# 时间：2023/7/13 19:06
# 作者：LxAnC
# 单击右键-》新键一个python文件，也就是一个模块
# 导入模块 import 模块 as 别名
import  math
from math import pi # 指定导入部分的函数
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('--------------------')
print(dir(math))
print(math.ceil(9.001)) # 向上取整 ceil是天花板的意思
print(math.floor(9.001)) # 向上取整 floor是地板的意思
print('----以下是我自定义模块,那么如何导入')
# 如何直接import，会报错
import 自定义模块
a=add(1,2)