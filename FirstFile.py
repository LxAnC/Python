# 时间：2023/7/1 16:31
# 作者：LxAnC
# 输出数字
print(520)
# 理解为加双引号
# 的意思就是不要编译器解释
print("helloword")
print(3+1)
# 输出到文件中
# 意思就是打开文件，a+的意思就是文件不存在就创建，
# 存在就在文件内容的后面继续追加
fp=open('D:/text.txt','a+')
print('helloworld',fp)

# 但文件中没有内容
# 如何解决呢

# 加上file=
print('helloworld',file=fp)


# 如果我不想换行输出（输出内容是在一行之中）
print('hello','world','python')
