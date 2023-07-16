# 时间：2023/7/16 14:28
# 作者：LxAnC
import sys
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
import time
print(time.time())
print(time.localtime(time.time()))
# import os访问操作系统服务的标准库
import urllib.request
print(urllib.request.urlopen("http://www.baidu.com").read())

