# 时间：2023/7/5 22:27
# 作者：LxAnC
# 可以打印错误信息

# print(10/0)
# 报错的开头就是traceback
import traceback  # 安装traceback的模块
try:
    print('---------------')
    print(1/0)
except:
    traceback.print_exc()  #打印出来的函数，以后可能要放在日志信息里面