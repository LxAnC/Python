# 时间：2023/7/3 21:46
# 作者：LxAnC

print(bool(0)) # False
print(bool(1)) # True
def fun(num):
    odd=[]
    even=[]
    for item in num:
        if item%2:
            odd.append(item)
        else:
            even.append(item)
    return odd,even
# s=input('请输入一个数')
lst=[10,29,34,23,44,53,55]
print(fun(lst))
# 如果函数没有返回值可以省略return
# 函数的返回值，如果是1个，那就直接返回类型
# 函数的返回值，如果是多个，返回的结果是元组