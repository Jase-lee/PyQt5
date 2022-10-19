import sys
args = sys.argv
print(args) # 输出结果：['D:/CodeDownLoad/PyQt5/02-01 sys.argv 讲解.py']

"""
    我们的代码的执行方式有两种：
    1：右击执行
    2：命令行方式执行：python 文件名.py 参数
    当别人通过命令行启动程序的时候，可以向代码传递一些参数来执行不同的业务逻辑，如：
    if args[1] == '1':
        print("XXXX")
    else:
        print("YYYY")
"""
