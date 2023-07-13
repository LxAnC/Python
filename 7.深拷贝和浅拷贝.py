# 时间：2023/7/13 18:34
# 作者：LxAnC

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk


# 变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)
# 类的浅拷贝
print('----------------------------------')
disk=Disk()
computer=Computer(cpu1,disk)

import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
