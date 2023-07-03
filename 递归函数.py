# 时间：2023/7/3 22:55
# 作者：LxAnC
# 函数内部调用他本身
# 每递归调用一次函数，都会在栈内存分配一个栈帧
# 每执行完一次函数，都会释放空间
# 占用内存多，效率低，优点是代码简单

# 计算6的阶乘
# 普通做法
def fun(a):
    s=1
    for i in range(1,a+1):
        s*=i
    return s
def fun1(a):
    if a==1:
        return 1
    else:
        return a*fun1(a-1)
print('6的阶乘是:',fun1(6))

# 斐波拉契数列
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))