# 时间：2023/7/2 15:53
# 作者：LxAnC

'''
循环的分类
1.while
2.for-in
'''
# 1.while语法
'''
while 条件表达式:
执行表达式
'''
# a=1
# while a<10:
#     # 执行条件执行体
#     print(a)
#     a+=1

# 四步循环法
# a=1
# while a<=10:
#     print("执行了",a,'次')
#     a+=1
# sum=0
# while a<5:
#     sum+=a
#
# print('1到4之间的总和为：',sum)

'''计算1-100之间的偶数和'''
'''初始化变量'''
# a=1
# sum=0
# '''条件判断'''
# while a<=100:
#     if a%2:   # a%2==0或者bool(a%2) 还可以使用not bool(a%2)可以表示奇数
#        sum+=a
#     a+=1
# '''改变变量'''
# print('1-100之间的偶数是:',sum)


# for-in循环
'''
for-in循环遍历的对象必须是可迭代对象
目前只学习了字符串或者range()
'''
# 字符串
# for item in 'python':
#     print(item)

# range()
# for i in range(10):
#     print(i)

# 如果在循环体中不需要使用到自定义变量，可以将自定义变量写为”_“
# for _ in range(5):
#     print('人生苦短，我用Python')

print('使用for循环，计算1-100的偶数和')
# sum=0
# for i in range(1,101):
#     if not bool(i%2):
#         sum+=i
# print('总和是:',sum)

print('打印出100-999之间的水仙花数')
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if(ge*ge*ge+shi*shi*shi+bai*bai*bai==item):
        print(item)

# 非正常结束循环结构
# 假如输密码，如何一次跳出

# for item in range(3):
#     pwd=input('请输入密码：')
#     if pwd!='8888':
#         print('密码不正常')
#     else:
#         print('密码正确')
#         break

# 以上改为while语句
a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
       print('密码正确')
       break
    else:
        print('不正确')