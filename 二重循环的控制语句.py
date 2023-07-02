# 时间：2023/7/2 17:27
# 作者：LxAnC
# 控制语句在循环中的妙用
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()