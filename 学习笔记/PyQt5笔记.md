[TOC]

## 第5章  PyQT5 结构

### 使用控件该导入哪个类

假如初次使用Qt创建一个控件，但是不知道该控件属于哪个类，可以使用如下方法：

```python
# 将基本全部模块中的类综合到一个单一的模块中
from PyQt5.Qt import *
```

使用上面的导入方法的好处和坏处：

好处：使用控件的时候不用关心属于哪个模块哪个类

坏处：占用内存



## 第6章  PyQT5 初体验

使用PyQt5做一个小案例，需求如下：

1）展示一个 500 * 500 的窗口

2）设置窗口标题为 "XXX管理系统"

3）添加子控件（标签控件），并显示 "Hello World"



 代码实现如下：

```python
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("XXX管理系统")
window.resize(500, 500)
window.move(200, 200)

label = QLabel(window)
label.setText("Hello World")
label.resize(100,100)
label.move(200, 200)

window.show()
sys.exit(app.exec_())
```



## 第7章  程序基本结构分析

### 7.1  app = QApplication(sys.argv)

**sys.argv 含义**

sys.argv 是一个参数列表，这个列表存放着从外界获取到的参数（可能有多个）。下面举一个例子来讲解：

```python
# test.py

import sys
lst = sys.argv
print(lst)
```

在终端使用命令：`python test.py` 运行 test.py 文件，得到的结果如下：

```
['test.py']
```

可以看到 sys.argv 是一个列表，里面有一个元素就是当前文件的文件名。

接下来再次在终端运行 test.py 文件，但是要传入一个参数，比如 1：`python test.py 1`。运行结果如下：

```
['test.py', '1']
```

传入多个参数，观察运行结果：`python test.py 1 '哈哈哈' True`

```python
['test.py', '1', '哈哈哈', 'True']
```

可以看到sys.argv的第一个元素是执行的 py 文件相对于当前工作目录的路径，然后传入什么参数就添加什么参数到该列表中。



**sys.argv 使用**

工作中我们可能会遇到这种情况，需要在命令行执行 py 文件，并且传入一些参数。这时候 sys.argv 就派上用场了，sys.argv 维护着一个列表，从外界传入的参数都记录在这个列表里面，从而可以在 py 文件中使用这些参数。例如：

```python
# test.py

"""
使用命令行方式执行改文件，第一个参数为请输入姓名，第二个参数请输入年龄，如：
python test.py 张三 18
"""

import sys

def func():
    print("sys.argv[0]：" + sys.argv[0])
    print("sys.argv[1]：" + sys.argv[1])
    print("sys.argv[2]：" + sys.argv[2])
    print("----------------")
    print("Welcome " + sys.argv[1])
    if int(sys.argv[2])< 18:
        print("未成年不可以投票哦！")
    else:
        print("您的年龄已能进行投票！")
func()
```

执行结果：

```python
sys.argv[0]：.\test.py
sys.argv[1]：张三
sys.argv[2]：18
----------------
Welcome 张三
您的年龄已能进行投票！
```

`app = QApplication(sys.argv)`里面传递 sys.argv 就是在使用应用该程序的时候可以给一整个 QApplication 传递参数。

假如在一个test.py文件中创建`app = QApplication(sys.argv)`，app对象只在当前模块，如果要在其他模块中使用这个app对象该如何做？有两种方法：

- 可以使用 `app.argumnets()`来获取传递的参数。

- 可以使用`qApp.arguments()`来获取

`app = QApplication(sys.argv)`这一整句话的作用就是创建一个应用程序对象。

------

### 7.2  window = QWidget()

```
window = QWidget()
window.setWindowTitle("XXX管理系统")
window.resize(500, 500)
window.move(200, 200)

windows.show()
```

`window = QWidget()`的作用就是创建一个控件，把它当做一个顶层控件（窗口），来容纳其他的控件。当我们创建一个控件之后，如果这个控件没有父控件，则把它当做顶层控件（窗口），系统会自动的给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题，图标）。

`window.setWindowTitle("XXX管理系统")`设置窗口的标题。

`window.resize(500, 500)`设置窗口的大小，分别是宽度和高度。

`window.move(200, 200)`以下图为例，屏幕左上角的点坐标为（0, 0），这句表示window 窗口相对于该点向右和向下移动200个像素。

![在这里插入图片描述](https://img-blog.csdnimg.cn/30fa5417e8eb46818948da51441bc3ee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA54u4Xw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)



`window.show()`一个没有父对象的控件默认不显示，必须要调用 show( ) 才可以。



**QLabel() 标签**

```
label = QLabel(window)
label.setText("Hello World")
label.resize(100,100)
label.move(200, 200)
```

使用 QLabel 创建一个 label 标签，在创建的时候指定 window 作为其父控件，所以它就被添加到了window内部。如下：

<img src="https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221020225038600-739578513.png" alt="image-20221020225037508" style="zoom:80%;" />



假如不指定 window 作为它的父控件，执行代码后这个控件不会显示，除非手动的调用 `label.show()` 才会显示 label 标签，但是它不是在 window 的内部。如下：

```python
...

label = QLabel()
label.setText("Hello World")
label.resize(100,100)
label.move(200, 200)
label.show()

window.show()
...
```



![image-20221020225221369](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221020225222397-1850415511.png)

------

### 7.3  sys.exit(app.exec_())

sys模块的exit函数，通过抛出一个SystemExit异常来尝试结束程序，Python代码可以捕获这个异常来进行一些程序退出前的清理工作，也可以不退出程序。sys.exit函数同样可以带一个参数来作为程序的退出码，默认是0。

```python
import sys

try:
    print('try_开始')
    sys.exit(1)
    print('如果没有异常处理机制,程序就会终止')
except:
    print('执行sys.exit后走异常语句')
finally:
    print('sys_不管异常或正常都走')
```

上面执行到 `sys.exit(1)` 时，因为做了异常处理，所以程序正常退出了，可以看到执行结果中的退出码是 0：

![image-20221019235546968](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221019235548481-825226803.png)

修改上面的程序：

```python
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
```

程序执行到 `sys.exit(87)` 时退出，并返回一个退出码87，观察程序的运行结果：

![image-20221019235804513](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221019235805045-402662082.png)

退出码为0被视为“成功终止”，任何非零值被shell等视为“异常终止”。

**sys.exit(app.exec_())**的作用是获取程序的退出状态，看程序是正常退出还是因为内部的bug退出。



**app.exec_()**

作用就是让整个应用程序开始执行，进入到消息循环（无限循环），检测整个程序所接收到的用户的交互信息。

------

## 第8章  PyCharm活动模板的设置

