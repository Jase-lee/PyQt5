import sys

sys.exit(87)

try:
    print('try_开始')
    sys.exit(1)
    print('如果没有异常处理机制,程序就会终止')
except:
    print('执行sys.exit后走异常语句')
finally:
    print('sys_不管异常或正常都走')

