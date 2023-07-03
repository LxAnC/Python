# 时间：2023/7/3 17:27
# 作者：LxAnC
# 替换操作 三个参数就是 第一个是指定替换的参数第二个是要替换的内容，第三个是次数
s='hello,python'
print(s.replace('python','JAva'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))

# join()方法
# 将列表或者元组中的字符串合并成一个字符串
lst=['hello','java','python']
print('|'.join(lst)) # 用竖线来连接他们
t=('hello','Jaba','python')
print(''.join(t))  # 用空字符连接他们，所以没有空格
print('*'.join('Python')) # 将字符串看成序列，一个一个分割