# 时间：2023/7/2 11:35
# 作者：LxAnC
'''
请从键盘录入两个整数，比较两个整数的大小
'''
num_a=int(input('请输入第一个数'))
num_b=int(input('请输入第二个数'))
# 比较大小(常规写法)
# if num_a>=num_b:
#     print(num_a,'大于等于',num_b)
# else:
#     print(num_a,'小于等于',num_b)
print('用条件表达式进入比较')
print((str(num_a)+'大于等于'+str(num_b)) if num_a>=num_b else (str(num_a)+'小于等于'+str(num_b)))