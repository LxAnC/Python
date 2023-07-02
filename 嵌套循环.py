# 时间：2023/7/2 17:17
# 作者：LxAnC
# 嵌套循环
# 三行四列的矩形
for i in range(3):
    for j in range(4):
        print('*',end='\t')
    print()
# 直角三角形
for a in range(1,10):
    for b in range(1,a+1):
        print(a,'*',b,'=',a*b,end='\t')
    print()