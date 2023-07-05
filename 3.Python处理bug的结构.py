# 时间：2023/7/5 22:13
# 作者：LxAnC

# try---except---else结构
# try:
#    a=int(input('请输入第一个整数'))
#    b=int(input('请输入第二个整数'))
#    result=a/b
# except BaseException as e:
#     print('出错了',e)
# else:
#     print('计算结果为：',result)
# try---except---else---finally结构
# finally是无论是否发生异常都会被执行，能常用来释放try块中申请的资源
try:
    n1=int(input('请输入第一个整数'))
    n2=int(input('请输入第二个整数'))
    r=n1/n2
except BaseException as c:
    print('出错了')
    print(c)
else:
    print('计算结果是',r)
finally:
    print('无论发生什么都会执行')