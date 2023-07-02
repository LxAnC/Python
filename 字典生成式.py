# 时间：2023/7/3 3:27
# 作者：LxAnC

# 字典生成式
# 1.zip()内置函数"打包"
items=['Fruits','Books','Others']
prices=[96,78,85]
# 2.字典生成式
dic={ item.upper():price for item,price in zip(items,prices)}
print(dic)