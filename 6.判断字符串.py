# 时间：2023/7/3 17:19
# 作者：LxAnC
s='hello,python'
print('1.',s.isidentifier())
print('2.','hello'.isidentifier())
print('3.','张三'.isidentifier())
print('4.','张三_123'.isidentifier())

'''判断是否为空格组成'''
print('5.',' '.isspace())
print('6.','\t'.isspace())
'''判断是否全部由字母组成'''
print('7.','zhangs'.isalpha())
print('8.','张三'.isalpha())
'''是否全部由十进制数字组成'''
print('9.','zhangs'.isdecimal())
print('10.','1232131'.isdecimal())
'''是否全部由数字组成'''
print('11.','123四'.isnumeric())
print('12.','四五六'.isnumeric())
# 罗马数字和大写数字也算数字，但不算十进制数字，
'''判断是否全部由字母和数字构成'''
print('13.','abc1'.isalnum())
print('14.','张三123'.isalnum())
print('15.','abc!'.isalnum())
# 汉字也算字母