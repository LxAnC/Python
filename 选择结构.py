# 时间：2023/7/2 11:17
# 作者：LxAnC

# 选择结构是根据条件的布尔值来选择性的执行部分代码\

# if是单分支结果,if--else
# money=1000
# a=int(input('请输入你的取款金额'))# 取款金额
# # 判断余额是否充足
# if money>=a:
#    money-=a
#    print('取款成功，你的余额是,',money)
# else:
#     print('余额不足')

# 多分支结构
'''
if 条件表达式1:
    执行1
elif 条件表达式2:

'''
# score=int(input('请输入一个成绩'))
# if 90<=score<=100:   # python特色，与数学相同
#     print('a级')
# elif 80<=score<=89:
#     print('b级')
# elif 70<=score<=79:
#     print('c级')
# elif score>=60 and score<=69:
#     print('D级')
# elif score<=59:
#     print('不及格')
# else:
#     print('对不起成绩有误')

# 嵌套if
'''
会员  >=200 8折
     >=100  9折
     不打折
非会员
     >=200  9.5折
     不打折
'''
answer=input('您是会员吗?y/n')
money=float(input('请输入您的购物金额'))

if answer=='y':
    if(money>=200):
        print('付款金额为:',money*0.8)
    elif money>=100:
        print('付款金额为:',money*0.9)
    else:
        print('不打折您的付款金额为:',money)
else:
    if money>=200:
        print('付款金额为：',money*0.95)
    else:
        print('不打折。金额为:',money)