# 时间：2023/7/4 0:02
# 作者：LxAnC
# 粗心导致的语法错误syntaxError
# age=input('请输入你的年龄')
# print(type(age))
# if int(age)==18:
#     print('成年人')
# 由于知识的不熟练导致的错误
# indexError
# lst=[1,2,3,4]
# print(lst[4]) # 超过了范围
# append()方法使用的不熟练
# lst.append('a','b','c') # append一次只能添加一个元素，方法前面要加对象

# 被动掉坑 可以通过python提供的异常处理机制，可以在异常出现时即时捕获
# a=int(input('请输入第一个整数'))
# b=int(input('请输入第二个整数'))
# result=a/b
# print('结果是',result)
try: # 捕获异常
    c=int(input('请输入第一个整数'))
    d=int(input('请输入第二个整数'))
    r=c/d
    print('结果是%d'% r)
except ZeroDivisionError: # 如果没输值的话就不会走这里的错误
    print("1")
except ValueError: # 上一次处理不了的情况用这个去过滤错误
    print('只能输入数字')
# except BaseException: # 最高级的过滤

print('程序错误')
