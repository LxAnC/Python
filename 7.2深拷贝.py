# 时间：2023/7/13 18:52
# 作者：LxAnC


# 深拷贝，使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象
# 和拷贝对象所有的子对象也不相同
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
# 变量的赋值操作
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)
# 类的浅拷贝
print('----------------------------------')
disk=Disk()
computer=Computer(cpu1,disk)
import copy # 安装模块copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
# 深拷贝
print('-----------------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
