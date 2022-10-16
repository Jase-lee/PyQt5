[TOC]

## 01  PyQt 简介

### Python图形界面开发的几种方案

前面的教程中，我们程序的用户交互界面都是命令行终端窗口。

程序的用户交互界面，英文称之为 UI (user interface)

当一个应用的 UI 比较复杂的时候，命令行方式就不便用户使用了，这时我们需要图形界面。

如果用 `Python` 语言开发 `跨平台` 的图形界面的程序，主要有3种选择：

- Tkinter

  基于Tk的Python库，这是Python官方采用的标准库，优点是作为Python标准库、稳定、发布程序较小，缺点是控件相对较少。

- wxPython

  基于wxWidgets的Python库，优点是控件比较丰富，缺点是稳定性相对差点、文档少、用户少。

- PySide2、PyQt5

  基于Qt 的Python库，优点是控件比较丰富、跨平台体验好、文档完善、用户多。

  缺点是 库比较大，发布出来的程序比较大。



白月黑羽的建议是，如果大家要开发小工具，界面比较简单，可以采用Tkinter。

如果是发布功能比较多的正式产品，采用 基于Qt的PySide2、PyQt5。

本教程介绍的就是 使用 PySide2、PyQt5 开发Python程序的图形界面。



### PySide2、PyQt5 简介

PySide2、PyQt5 都是基于著名的 Qt 库。

Qt库里面有非常强大的图形界面开发库，但是Qt库是C++语言开发的，PySide2、PyQt5可以让我们通过Python语言使用Qt。

但是 PySide2、PyQt5 这两者有什么区别呢？

可以形象地这样说： PySide2 是Qt的 `亲儿子` ， PyQt5 是Qt还没有亲儿子之前的收的 `义子` （Riverbank Computing这个公司开发的）。

那为什么 PyQt5 这个义子 反而比 PySide2 这个亲儿子更出名呢？

原因很简单：PySide2 这亲儿子最近（2018年7月）才出生。

但是亲儿子毕竟是亲儿子，Qt准备大力培养，PySide2 或许更有前途。

已经在使用 PyQt5 的朋友不要皱眉， 两个库的使用 对程序员来说，差别很小：它们的调用接口几乎一模一样。

如果你的程序是PyQt5开发的，通常只要略作修改，比如把导入的名字从 PyQt5 换成 PySide2 就行了。反之亦然。



### 安装 PySide2

很简单，直接执行

```py
pip install pyside2
```

即可下载安装。

这个库比较大，大概有100M左右，大家耐心等待。

有的朋友，网络比较慢，可以指定国内的安装源，下载安装。

比如，使用豆瓣源下载安装：

```
pip install pyside2 -i https://pypi.douban.com/simple/
```



### 安装PyQt5

如果你选择PyQt5，直接执行

```py
pip install pyqt5-tools
```

即可同时安装 PyQt5 和 一些重要的工具，比如 Qt designer。





## 一个案例

现在我们要开发一个程序，让用户输入一段文本包含：员工姓名、薪资、年龄。

格式如下：

```py
薛蟠     4560 25
薛蝌     4460 25
薛宝钗   35776 23
薛宝琴   14346 18
王夫人   43360 45
王熙凤   24460 25
王子腾   55660 45
王仁     15034 65
尤二姐   5324 24
贾芹     5663 25
贾兰     13443 35
贾芸     4522 25
尤三姐   5905 22
贾珍     54603 35
```

该程序可以把薪资在 2万 以上、以下的人员名单分别打印出来。

当然我们可以像以前一样，开发命令行程序（准确的说应该叫字符终端程序，因为UI是字符终端），让用户在字符终端输入。

但是如果我们能开发下面这样的图形界面程序，就更酷了

![image-20221016224910597](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016224911883-2031317270.png)

能，用 Python Qt，开发上面的界面就只要下面这短短的程序即可

```
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)

window.show()

app.exec_()
```

`QApplication` 提供了整个图形界面程序的底层管理功能，比如：

初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…

对 QApplication 细节比较感兴趣的话，可以[点击这里参考官方网站](https://doc.qt.io/qt-5/qapplication.html)

既然QApplication要做如此重要的初始化操作，所以，我们必须在任何界面控件对象创建前，先创建它。



QMainWindow、QPlainTextEdit、QPushButton 是3个控件类，分别对应界面的主窗口、文本框、按钮

他们都是控件基类对象QWidget的子类。

要在界面上 `创建一个控件` ，就需要在程序代码中 `创建` 这个 `控件对应类` 的一个 `实例对象`。



在 Qt 系统中，控件（widget）是 `层层嵌套` 的，除了最顶层的控件，其他的控件都有父控件。

QPlainTextEdit、QPushButton 实例化时，都有一个参数window，如下

```py
QPlainTextEdit(window)
QPushButton('统计', window)
```

就是指定它的父控件对象 是 window 对应的QMainWindow 主窗口。

而 实例化 QMainWindow 主窗口时，却没有指定 父控件， 因为它就是最上层的控件了。



控件对象的 move 方法决定了这个控件显示的位置。

比如

`window.move(300, 310)` 就决定了 主窗口的 左上角坐标在 `相对屏幕的左上角` 的X横坐标300像素, Y纵坐标310像素这个位置。

`textEdit.move(10,25)` 就决定了文本框的 左上角坐标在 `相对父窗口的左上角` 的X横坐标10像素, Y纵坐标25像素这个位置。



控件对象的 resize 方法决定了这个控件显示的大小。

比如

`window.resize(500, 400)` 就决定了 主窗口的 宽度为500像素，高度为400像素。

`textEdit.resize(300,350)` 就决定了文本框的 宽度为300像素，高度为350像素。



放在主窗口的控件，要能全部显示在界面上， 必须加上下面这行代码

```
window.show()
```

最后 ，通过下面这行代码

```py
app.exec_()
```

进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。

### 界面动作处理 (signal 和 slot)

接下来，我们要实现具体的统计功能：

当用户点击 **统计** 按钮时， 从界面控件 QPlainTextEdit 里面获取 用户输入的字符串内容，进行处理。

首先第一个问题： 用户点击了 **统计** 按钮，怎么通知程序？ 因为只有程序被通知了这个点击，才能做出相应的处理。

在 Qt 系统中， 当界面上一个控件被操作时，比如 被点击、被输入文本、被鼠标拖拽等， 就会发出 `信号` ，英文叫 `signal` 。就是表明一个事件（比如被点击、被输入文本）发生了。

我们可以预先在代码中指定 处理这个 signal 的函数，这个处理 signal 的函数 叫做 `slot` 。

比如，我们可以像下面这样定义一个函数

```py
def handleCalc():
    print('统计按钮被点击了')
```

然后， 指定 如果 发生了button 按钮被点击 的事情，需要让 `handleCalc` 来处理，像这样

```py
button.clicked.connect(handleCalc)
```

用QT的术语来解释上面这行代码，就是：把 button 被 点击（clicked） 的信号（signal）， 连接（connect）到了 handleCalc 这样的一个 slot上

大白话就是：让 handleCalc 来 处理 button 被 点击的操作。



但是上面这行代码运行后，只能在字符窗口 打印出 `统计按钮被点击了` ， 还不能处理分析任务。

要处理分析任务，我们还得从 textEdit 对应的 文本框中 获取用户输入的文本，并且分析薪资范围，最终弹出对话框显示统计结果。

我们修改后，代码如下

```py
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

def handleCalc():
    info = textEdit.toPlainText()

    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name,salary,age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                '统计结果',
                f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                )

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)
button.clicked.connect(handleCalc)

window.show()

app.exec_()
```

运行后，你会发现结果如下

![image-20221016225034222](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225034622-793190129.png)

### 封装到类中

上面的代码把控件对应的变量名全部作为全局变量。

如果要设计稍微复杂一些的程序，就会出现太多的控件对应的变量名。

而且这样也不利于 代码的模块化。

所以，我们通常应该把 一个窗口和其包含的控件，对应的代码 全部封装到类中，如下所示

```py
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)


    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
```

这样代码的可读性是不是好多了？

### 常见问题

不少学员发现， 运行python qt程序时，弹出错误提示框，显示如下提示信息

```py
This application failed to start because no Qt platform plugin could be 
initialized. Reinstalling the application may fix this problem.
```

解决方法是：

把 PySide2 或者 PyQt5 安装在解释器目录下的 `\plugins\platforms` 目录添加到环境变量Path中。

比如，我的环境就是把这个路径加到 环境变量 `Path` 中

```py
c:\Python38\Lib\site-packages\PySide2\plugins\platforms
```



另外有这种说法：

如果使用的 Python 解释器 是 Anaconda/Miniconda里面的，请把 `\plugins\platforms` 目录添加到环境变量 `QT_QPA_PLATFORM_PLUGIN_PATH` 中。



## 界面设计师 Qt Designer

### Qt Designer 简介



[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=4)

QT程序界面的 一个个窗口、控件，就是像上面那样用相应的代码创建出来的。

但是，把你的脑海里的界面，用代码直接写出来，是有些困难的。

很多时候，运行时呈现的样子，不是我们要的。我们经常还要修改代码调整界面上控件的位置，再运行预览。反复多次这样操作。

可是这样，真的…太麻烦了。

其实，我们可以用QT界面生成器 `Qt Designer` ，拖拖拽拽就可以直观的创建出程序大体的界面。

怎么运行这个工具呢？

Windows下，运行 Python安装目录下 `Scripts\pyside2-designer.exe` 这个可执行文件



如果你安装的是pyqt5， 运行 Python安装目录下 `Scripts\pyqt5designer.exe` 这个可执行文件



根据上面链接的视频讲解，大家初步了解一下 Qt Designer 的使用方法。



通过 Qt Designer 设计的界面，最终是保存在一个ui文件中的。

大家可以打开这个ui文件看看，就是一个XML格式的界面定义。

### 动态加载UI文件



[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=5)

有了界面定义文件，我们的Python程序就可以从文件中加载UI定义，并且动态 创建一个相应的窗口对象。

如下：

```py
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('main.ui')

        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')

            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.ui,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
```



如果你使用的是PyQt5 而不是 PySide2，加载UI文件的代码如下

```py
from PyQt5 import uic

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("main.ui")
```

### 转化UI文件为Python代码

还有一种使用UI文件的方式：先把UI文件直接转化为包含界面定义的Python代码文件，然后在你的程序中使用定义界面的类

1. 执行如下的命令 把UI文件直接转化为包含界面定义的Python代码文件

```py
pyside2-uic main.ui > ui_main.py
```



如果你安装的是PyQt5，执行如下格式的命令转化

```py
pyuic5 main.ui > ui_main.py
```

然后在你的代码文件中这样使用定义界面的类

```py
from PySide2.QtWidgets import QApplication,QMainWindow
from ui_main import Ui_MainWindow

# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问
        self.ui.webview.load('http://www.baidu.com')

app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()
```



那么我们该使用哪种方式比较好呢？动态加载还是转化为Python代码？

白月黑羽建议：通常采用动态加载比较方便，因为改动界面后，不需要转化，直接运行，特别方便。

但是，如果 你的程序里面有非qt designer提供的控件， 这时候，需要在代码里面加上一些额外的声明，而且 可能还会有奇怪的问题。往往就 要采用 转化Python代码的方法。

### 一个练习

请大家利用Qt Designer 实现一个 类似 `Postman` 的 HTTP 接口测试工具。

界面如下

![image-20221016225157304](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225157730-1065374316.png)

要实现的功能，[点击这里观看视频说明](https://www.bilibili.com/video/BV1cJ411R7bP?p=6)

这个界面里面用到了常见的几个控件：按钮，单行文本框，多行文本框，组合选择框，表格。

其中 选择框、表格 这两个控件 没有接触过的朋友，可以先学习一下本教程 后面章节 `常见控件2` 。

如果你对 使用Python语言发送HTTP请求不熟悉，可以先把界面做出来。

然后[点击这里，学习白月黑羽的 HTTP Requests 教程](https://www.byhy.net/tut/auto/apitest/03/)后，再去实现。



`游客` 也可以 做这个练习，并且得到参考代码，[点击这里查看](https://www.byhy.net/adv/bonus/qt2/)

### 界面布局 Layout

我们前面写的界面程序有个问题，如果你用鼠标拖拽主窗口边框右下角，进行缩放，就会发现里面的控件一直保持原有大小不变。这样会很难看。

我们通常希望，随着主窗口的缩放， 界面里面的控件、控件之间的距离也相应的进行缩放。

Qt是通过界面布局Layout类来实现这种功能的。



我们最常用的 Layout布局 有4种，分别是

- QHBoxLayout 水平布局

QHBoxLayout 把控件从左到右 水平横着摆放，如下所示

![image-20221016225225256](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225225515-452600443.png)

- QVBoxLayout 垂直布局

QHBoxLayout 把控件从上到下竖着摆放，如下所示

![image-20221016225242035](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225242362-730909524.png)

- QGridLayout 表格布局

QGridLayout 把多个控件 格子状摆放，有的控件可以 占据多个格子，如下所示

![image-20221016225254031](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225254287-650841683.png)

- QFormLayout 表单布局

QFormLayout 表单就像一个只有两列的表格，非常适合填写注册表单这种类型的界面，如下所示

![image-20221016225307247](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225307503-576418240.png)

### MainWindow 的Layout

如果我们选择的主窗口是MainWindow类型，要给MainWindow整体设定Layout，必须 `先添加一个控件到 centralwidget 下面` ，如下

![image-20221016225322862](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225323206-139841980.png)

然后才能右键点击 MainWindow，选择布局，如下

![image-20221016225334311](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225334896-1161125009.png)

### 调整控件位置和大小

### 调整layout中控件的大小比例

可以通过设定控件的sizePolicy来调整，具体操作请看视频讲解。

### 调整控件间距

要调整控件上下间距，可以给控件添加layout，然后通过设定layout的上下的padding 和 margin 来调整间距，具体操作请看视频讲解。

要调整控件的左右间距，可以通过添加 horizontal spacer 进行控制，也可以通过layout的左右margin

### 调整控件次序

有的时候 我们需要调整 一个layout里面，控件的上下显示次序，或者左右显示次序，该怎么做呢？

如果是简单的两个控件在 layout里面，通常直接拖动就行了。

但如果是更复杂的情况，比如，

大家[点击这里](https://cdn2.byhy.net/files/py/qt/qss_pilot.zip)，下载一个白月黑羽实战班学员开发的程序界面代码，解压后，拖动里面的main.ui界面文件到Qt设计师里面。

如果我们要在原来的界面上做一些修改，如下图所示

![image-20221016225416239](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225416543-460716265.png)

大家可以自己尝试 新建一个垂直layout，把原来的两个layout 拖动到垂直layout里面。

就会发现，如果要调整两个layout的上下显示次序，直接拖动经常会导致界面混乱。

怎么办呢？

## 界面布局步骤建议

[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=9)

对界面控件进行布局，白月黑羽的经验是 按照如下步骤操作

- 先不使用任何Layout，把所有控件 按位置 摆放在界面上
- 然后先从 最内层开始 进行控件的 Layout 设定
- 逐步拓展到外层 进行控件的 Layout设定
- 最后调整 layout中控件的大小比例， 优先使用 Layout的 layoutStrentch 属性来控制

## 从一个窗口跳转到另外一个窗口

经常有朋友问我，程序开始的时候显示一个窗口（比如登录窗口），操作后进入到另外一个窗口，怎么做。

方法很简单，主要就是 实例化另外一个窗口，显示新窗口，关闭老窗口。

如下代码所示

```py
from PySide2 import QtWidgets
import sys

class Window2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口2')

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        button = QtWidgets.QPushButton('按钮2')

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(button)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口1')

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        button = QtWidgets.QPushButton('打开新窗口')
        button.clicked.connect(self.open_new_window)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(button)

    def open_new_window(self):
        # 实例化另外一个窗口
        self.window2 = Window2()
        # 显示新窗口
        self.window2.show()
        # 关闭自己
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```



[点击这里下载](https://cdn2.byhy.net/files/qt/window-switch.zip) 一个登录切换到主窗口 的示例代码包



如果经常要在两个窗口来回跳转，可以使用 `hide()` 方法 隐藏窗口， 而不是 `closes()` 方法关闭窗口。 这样还有一个好处：被隐藏的窗口再次显示时，原来的操作内容还保存着，不会消失。

## 弹出模式对话框

有的时候，我们需要弹出一个模式对话框输入一些数据，然后回到 原窗口。

所谓模式对话框，就是弹出此对话框后， 原窗口就处于不可操作的状态，只有当模式对话框关闭才能继续。

参考如下代码

```py
from PySide2 import QtWidgets
import sys

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('模式对话框')

        self.resize(500, 400)
        self.textEdit = QtWidgets.QPlainTextEdit(self)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QtWidgets.QPushButton('统计', self)
        self.button.move(380, 80)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        button = QtWidgets.QPushButton('打开模式对话框')
        button.clicked.connect(self.open_new_window)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(button)

    def open_new_window(self):
        # 实例化一个对话框类
        self.dlg = MyDialog()        
        # 显示对话框，代码阻塞在这里，
        # 等待对话框关闭后，才能继续往后执行
        self.dlg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

### 课后练习

VIP实战班学员请联系老师，完成一个数据抽样的程序开发，界面如下

![image-20221016225505786](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225506492-358470749.png)

# 发布程序

## 正式发布程序



[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=10)

前面，我们开发好了一个HTTP协议测试程序，但是这个程序是Python程序，运行它需要Python解释器。

如果我们要发布程序给客户使用，当然不能要求别人去安装Python解释器，并且敲命令 `python httpclient.py`。

我们应该做成 `可执行程序` 发布别人使用。

我们可以使用 `PyInstaller` 来制作独立可执行程序。

我们的教程有对PyInstaller的专门介绍，[点击这里查看](https://www.byhy.net/tut/py/etc/toexe/)

我们前面开发的QT界面程序，在Windows 上只需要执行下面的命令，即可制作独立exe程序

```
pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml
```

这样就会在当前目录下产生一个名为 `dist` 的目录。里面就有一个名为 httpclient 的目录，我们的可执行程序 httpclient.exe 就在里面。

其中

`--noconsole` 指定不要命令行窗口，否则我们的程序运行的时候，还会多一个黑窗口。 但是我建议大家可以先去掉这个参数，等确定运行成功后，再加上参数重新制作exe。因为这个黑窗口可以显示出程序的报错，这样我们容易找到问题的线索。

`--hidden-import PySide2.QtXml` 参数是因为这个 QtXml库是动态导入，PyInstaller没法分析出来，需要我们告诉它，

最后，别忘了，把程序所需要的ui文件拷贝到打包目录中。

因为PyInstaller只能分析出需要哪些代码文件。 而你的程序动态打开的资源文件，比如 图片、excel、ui这些，它是不会帮你打包的。

我们的 示例代码 需要 从 httpclient.ui 中加载界面，手动拷贝到 `dist/httpclient` 目录中。

然后，再双击运行 `httpclient.exe` ，完美！！

## 程序图标



[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=11)

### 添加主窗口图标

我们程序运行的窗口，需要显示自己的图标，这样才更像一个正式的产品。

通过如下代码，我们可以把一个png图片文件作为 程序窗口图标。

```py
from PySide2.QtGui import  QIcon

app = QApplication([])
# 加载 icon
app.setWindowIcon(QIcon('logo.png'))
```

注意：这些图标png文件，在使用PyInstaller创建可执行程序时，也要拷贝到程序所在目录。否则可执行程序运行后不会显示图标。

### 应用程序图标

应用程序图标是放在可执行程序里面的资源。

可以在PyInstaller创建可执行程序时，通过参数 `--icon="logo.ico"` 指定。

比如

```
pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo.ico"
```

注意参数一定是存在的ico文件，不能是png等图片文件。

如果你只有png文件，可以通过在线的png转ico文件网站，生成ico，比如下面两个网站

[网站1](https://www.zamzar.com/convert/png-to-ico/)

[网站2](https://www.easyicon.net/covert/)

注意：这些应用程序图标ico文件，在使用PyInstaller创建可执行程序时，不需要要拷贝到程序所在目录。因为它已经被嵌入可执行程序了。

## 常用控件1

本章和接下来几章，会列出Qt的 `常见控件` ，并且描述这些控件的 `常用操作` 。

要了解Qt `所有控件` 和它们 `所有操作` ，请参阅如下官方手册：

[Python Qt官方文档 - 控件部分](https://doc.qt.io/qtforpython-5.12/PySide2/QtWidgets/index.html#module-PySide2.QtWidgets)



[点击这里，边看视频讲解，边学习下面的内容](https://www.bilibili.com/video/BV1Zf4y1W79o?p=1)

### 按钮

`QPushButton` 就是常见的按钮

![image-20221016225615882](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225616149-1448215524.png)

### 信号：被点击

当按钮被点击就会发出 `clicked` 信号，可以这样指定处理该信号的函数

```py
button.clicked.connect(handleCalc)
```

### 改变文本

代码中可以使用 `setText` 方法来改变按钮文本，比如

```禁用、启用
button.setText(text)
```

### 禁用、启用

所有控件（继承自QWidget类）都支持 禁用和启用方法。

禁用后，该控件不再处理用户操作

- 禁用

```py
button.setEnabled(False)
```

- 启用

```py
button.setEnabled(True)
```

### 设置图标

可以通过如下方法给按钮设置图标

```py
from PySide2.QtCore import Qt,QSize
from PySide2.QtGui import QIcon

# 设置图标
button.setIcon(QIcon('logo.png'))

# 设置图标大小
button.setIconSize(QSize(30, 30))
```

### 单行文本框

`QLineEdit` 是只能单行编辑的文本框。

![image-20221016225652999](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225653335-1890178088.png)

### 信号：文本被修改

当文本框中的内容被键盘编辑，被点击就会发出 `textChanged `信号，可以这样指定处理该信号的函数

```py
edit.textChanged.connect(handleTextChange)
```

Qt在调用这个信号处理函数时，传入的参数就是 文本框目前的内容字符串。

### 信号：按下回车键

当用户在文本框中任何时候按下回车键，就会发出 `returnPressed` 信号。

有时我们需要处理这种情况，比如登录界面，用户输完密码直接按回车键就进行登录处理，比再用鼠标点击登录按钮快捷的多。

可以指定处理 returnPressed 信号，如下所示

```py
passwordEdit.returnPressed.connect(onLogin)
```

### 获取文本

通过 `text` 方法获取编辑框内的文本内容，比如

```py
text = edit.text()
```

### 设置提示

通过 `setPlaceholderText` 方法可以设置提示文本内容，比如

```py
edit.setPlaceholderText('请在这里输入URL')
```

### 设置文本

通过 `setText` 方法设置编辑框内的文本内容为参数里面的文本字符串，比如

```py
edit.setText('你好，白月黑羽')
```

原来的所有内容会被清除

### 清除所有文本

`clear` 方法可以清除编辑框内所有的文本内容，比如

```py
edit.clear()
```

### 拷贝文本到剪贴板

`copy` 方法可以拷贝当前选中文本到剪贴板，比如

```py
edit.copy()
```

### 粘贴剪贴板文本

`paste` 方法可以把剪贴板内容，拷贝到编辑框当前光标所在处，比如

```py
edit.paste()
```

### 多行纯文本框

`QPlainTextEdit` 是可以 `多行` 的纯文本编辑框。

![image-20221016225716401](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225716698-1315923733.png)

注意：在苹果MacOS上，有 更新文本框内容后，需要鼠标滑过才能更新显示的bug，[参考这里](https://bugreports.qt.io/browse/PYSIDE-871)

文本浏览框 内置了一个 [QTextDocument](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QTextDocument.html) 类型的对象 ，存放文档。

### 信号：文本被修改

当文本框中的内容被键盘编辑，被点击就会发出 `textChanged `信号，可以这样指定处理该信号的函数

```py
edit.textChanged.connect(handleTextChange)
```

注意： Qt在调用这个信号处理函数时，**不会传入**文本框目前的内容字符串，作为参数。

这个行为 和 单行文本框不同。

### 信号：光标位置改变

当文本框中的光标位置变动，就会发出 `cursorPositionChanged` 信号，可以这样指定处理该信号的函数

```py
edit.cursorPositionChanged.connect(handleChanged)
```

### 获取文本

通过 `toPlainText` 方法获取编辑框内的文本内容，比如

```py
text = edit.toPlainText()
```

### 获取选中文本

```py
# 获取 QTextCursor 对象
textCursor = edit.textCursor()
selection = textCursor.selectedText()
```

### 设置提示

通过 `setPlaceholderText` 方法可以设置提示文本内容，比如

```py
edit.setPlaceholderText('请在这里输入薪资表')
```

### 设置文本

通过 `setPlainText` 方法设置编辑框内的文本内容 为参数里面的文本字符串，比如

```py
edit.setPlainText('''你好，白月黑羽
hello byhy''')
```

原来的所有内容会被清除

### 在末尾添加文本

通过 `appendPlainText` 方法在编辑框末尾添加文本内容，比如

```py
edit.appendPlainText('你好，白月黑羽')
```

注意：这种方法会在添加文本后 `自动换行`

### 在光标处插入文本

通过 `insertPlainText` 方法在编辑框末尾添加文本内容，比如

```py
edit.insertPlainText('你好，白月黑羽')
```

注意：这种方法 `不会` 在添加文本后自动换行

### 清除所有文本

`clear` 方法可以清除编辑框内所有的文本内容，比如

```py
edit.clear()
```

### 拷贝文本到剪贴板

`copy` 方法可以拷贝当前选中文本到剪贴板，比如

```py
edit.copy()
```

### 粘贴剪贴板文本

`paste` 方法可以把剪贴板内容，拷贝到编辑框当前光标所在处，比如

```py
edit.paste()
```

### 设置最大行数

有时候，代码会不断往文本框添加内容，为了防止占用过多资源，可以设置文本框最大行数。



像这样：

```py
edit.document().setMaximumBlockCount(1000)
```

就设置最大为 1000行

## 文本浏览框

`QTextBrowser` 是 `只能查看文本` 控件。

通常用来显示一些操作日志信息、或者不需要用户编辑的大段文本内容。

[官网介绍](https://doc.qt.io/qtforpython-5.12/PySide2/QtWidgets/QTextBrowser.html)

该控件 获取文本、设置文本、清除文本、剪贴板复制粘贴 等等， 都和上面介绍的 多行纯文本框是一样的。

下面我们主要讲解不同点

### 在末尾添加文本

通过 `append` 方法在编辑框末尾添加文本内容，比如

```py
textBrowser.append('你好，白月黑羽')
```



有时，浏览框里面的内容长度超出了可见范围，我们在末尾添加了内容，往往希望控件自动翻滚到当前添加的这行，

可以通过 `ensureCursorVisible` 方法来实现

```py
textBrowser.append('你好，白月黑羽')
textBrowser.ensureCursorVisible()
```

注意：这种方法会在添加文本后 `自动换行`

### 在光标处插入文本

通过 `insertPlainText` 方法在编辑框末尾添加文本内容，比如

```py
edit.insertPlainText('你好，白月黑羽')
```

注意：这种方法 `不会` 在添加文本后自动换行

### 标签

`QLabel` 就是常见的标签，可以用来显示文字（包括纯文本和富文本）、图片 甚至动画。

![image-20221016225736792](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225737384-1589000969.png)

### 改变文本

代码中可以使用 `setText` 方法来改变标签文本内容，比如

```py
button.setText(text)
```

### 显示图片

QLabel可以用来显示图片，有时一个图片可以让界面好看很多，如下图所示

![image-20221016225750548](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225751000-903156115.png)

怎么用QLabel 显示图片呢？

可以在 Qt Designer上 属性编辑器 QLabel 栏 的 pixmap 属性设置中选择图片文件指定。



下面有示例代码包， 演示如何显示图片，并且控制图片的显示风格

大家[点击这里](https://cdn2.byhy.net/files/py/qt/qss_pilot2.zip)，下载一个 程序界面代码，解压后，拖动里面的main.ui界面文件到Qt设计师里面。

## 常用控件2

### 组合选择框

`QComboBox` 是组合选择框，如下图所示

![image-20221016225812311](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225812667-756073878.png)

### 信号：选项改变

如果用户操作修改了QComboBox中的选项就会发出 `currentIndexChanged `信号，可以这样指定处理该信号的函数

```py
cbox.currentIndexChanged.connect(handleSelectionChange)
```

### 添加一个选项

代码中可以使用 `addItem` 方法来添加一个选项到 `末尾` ，参数就是选项文本

```py
cbox.addItem('byhy')
```

### 添加多个选项

代码中可以使用 `addItems` 方法来添加多个选项到 `末尾`，参数是包含了多个选项文本的列表

```py
cbox.addItems(['byhy','白月黑羽','python教程'])
```

### 清空选项

代码中可以使用 `clear` 方法来清空选项，也就是删除选择框内所有的选项

```py
cbox.clear()
```

### 获取当前选项文本

代码中可以使用 `currentText` 方法来获取当前 `选中的选项` 的文本，比如

```py
method = cbox.currentText()
```

### 列表

`QListWidget` 是列表控件，如下图所示

![image-20221016225839805](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225840150-1472897859.png)

Qt Designer 如下图 选择：

![image-20221016225851803](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225852377-959031374.png)

### 添加一个选项

代码中可以使用 `addItem` 方法来添加一个选项到 `末尾` ，参数就是选项文本

```py
listWidget.addItem('byhy')
```

### 添加多个选项

代码中可以使用 `addItems` 方法来添加多个选项到 `末尾`，参数是包含了多个选项文本的列表

```py
listWidget.addItems(['byhy','白月黑羽','python教程'])
```

### 删除一个选项

代码中可以使用 `takeItem` 方法来删除1个选项，参数是该选项所在行

```py
listWidget.takeItem(1)
```

就会删除第二行选项

### 清空选项

代码中可以使用 `clear` 方法来清空选项，也就是删除选择框内所有的选项

```py
listWidget.clear()
```

### 获取当前选项文本

`currentItem` 方法可以得到列表当前选中项对象（QListWidgetItem） ，再调用这个对象的 `text` 方法，就可以获取文本内容，比如

```py
listWidget.currentItem().text()
```



可以使用 item 方法获取指定某行的 QListWidgetItem，

比如，

```py
listWidget.item(0).text()
```

就获取了 `第1行` 的列表项的文本。

### 表格

`QTableWidget` 是表格控件，如下图所示

![image-20221016225910996](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225911279-752449256.png)

表格控件单元格里面可以显示文字，也可以显示富文本、图片等内容。

表格控件的每个单元格里面要显示内容，都必须创建一个 `QTableWidgetItem` 类型的对象。

Qt Designer 如下图 选择：

![image-20221016225939417](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225939908-1645252219.png)

### 创建列 和 标题栏

我们可以通过 Qt designer 为一个表格创建列和对应的标题栏。

只需要双击 Qt designer 设计的窗体中的 表格控件， 就会出现这样的对话框

![image-20221016225953172](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016225953464-596708086.png)

在 `列` 标签栏中，点击左下角的加号，就可以为 添加一个列，并且设置标题栏名称。

![image-20221016230004369](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230004733-1154343246.png)

### 插入一行、删除一行

`insertRow` 方法可以在指定位置插入一行，比如

```py
table.insertRow(0)
```

就插入一行到第 `1` 行这个位置， 表格原来第1行（包括原来的第1行）以后的内容，全部往下移动一行。

```py
table.insertRow(2)
```

就插入一行到第 `3` 行这个位置， 表格原来第3行（包括原来的第3行）以后的内容，全部往下移动一行。



`removeRow` 方法可以删除指定位置的一行，比如

```py
table.removeRow(0)
```

就删除第 `1` 行， 表格原来第1行以后的内容，全部往上移动一行。

```py
table.removeRow(2)
```

就删除第 `3` 行， 表格原来第3行以后的内容，全部往上移动一行。

### 设置单元格内容、对齐、属性

qt表格的单元格内的内容对象 是一个 单元格对象 `QTableWidgetItem` 实例

如果单元格 `没有被设置过` 内容，可以这样

```py
from PySide2.QtWidgets import QTableWidgetItem

item = QTableWidgetItem()
item.setText('白月黑羽')
table.setItem(row, 0, item)
```



也可以简写为

```py
from PySide2.QtWidgets import QTableWidgetItem

table.setItem(row, 0, QTableWidgetItem('白月黑羽'))
```



如果单元格 `已经被设置过` 文本内容，

`item` 方法可以获取指定位置的 QTableWidgetItem ，再调用这个对象的 `setText` 方法，就可以设置单元格文本内容，比如

```py
table.item(0,0).setText('白月黑羽-江老师')
```

就设置了 `第1行，第1列` 的单元格里面的文本。

```py
table.item(2,4).setText('白月黑羽-江老师')
```

就设置了 `第3行，第5列` 的单元格里面的文本。



如果希望某个单元格为 **只读**，不允许修改，可以使用QTableWidgetItem对象的 `setFlags` 方法，像这样

```py
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt

item = QTableWidgetItem('白月黑羽')
item.setFlags(Qt.ItemIsEnabled) # 参数名字段不允许修改
table.setItem(row, 0, item)
```



如果想文本内容 **居中对齐**，每个当对应的QTableWidgetItem 调用 setTextAlignment，如下

```py
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt

item = QTableWidgetItem()
item.setText('白月黑羽')
# 文本居中
item.setTextAlignment(Qt.AlignCenter) 
table.setItem(row, 0, item)
```



如果想设置 表格框 和 单元格边线 的颜色，可以使用样式如下

```css
QTableWidget {
	border:1px solid green;
    gridline-color: rgb(71, 191, 255);
}
```



### 获取单元格文本的内容

`item` 方法可以指定位置的单元格对象（QTableWidgetItem） ，再调用这个对象的 `text` 方法，就可以获取文本内容，比如

```py
table.item(0,0).text()
```

就获取了 `第1行，第1列` 的单元格里面的文本。

```py
table.item(2,4).text()
```

就获取了 `第3行，第5列` 的单元格里面的文本。

### 获取所有行数、列数

代码中可以使用 `rowCount` 方法来获取表格所有的 `行数` ，比如

```py
rowcount = table.rowCount()
```



可以使用 `columnCount` 方法来获取表格所有的 `列数` ，比如

```py
rowcount = table.columnCount()
```

### 获取当前选中是第几行

代码中可以使用 `currentRow` 方法来获取当前选中是第几行，比如

```py
currentrow = table.currentRow()
```

注意：行数是从0开始的， 第一行的行数是 0

### 设置表格行数、列数

代码中可以使用 `setRowCount` 方法来设置表格 `行数` ，比如

```py
table.setRowCount(10)
```

代码中可以使用 `setColumnCount` 方法来设置表格 `列数` ，比如

```py
table.setColumnCount(10)
```

### 清除/删除所有内容

`clearContents` 方法可以清除表格所有的内容，比如

```py
table.clearContents()
```

清除后，仍然会留下表格栏



如果连表格栏都要删除，可以使用 `setRowCount(0)`，像这样

```py
table.setRowCount(0)
```

### 设定列宽、宽度自动缩放

Qt Designer 上目前没法拖拽设定 每个列的宽度，只能在代码中指定。

如下所示

```py
# 设定第1列的宽度为 180像素
table.setColumnWidth(0, 180)

# 设定第2列的宽度为 100像素
table.setColumnWidth(1, 100)
```



如想让 表格控件宽度 随着父窗口的缩放自动缩放，可以

在 属性编辑器 中 勾选 `HorizontalHeaderStretchLastSection`

或者使用下面代码

```py
table.horizontalHeader().setStretchLastSection(True)
```

### 信号：单元格内容改动

当用户修改了一个单元格的内容，会发出 `cellChanged` 信号，并且携带参数指明该单元格的行号和列号。

我们的代码可以对该信号进行相应的处理。

示例代码如下

```py
    def __init__(self):
        # 指定单元格改动信号处理函数
        self.ui.table.cellChanged.connect(self.cfgItemChanged)

    
    def cfgItemChanged(self,row,column):
        # 获取更改内容
        cfgName = self.ui.table.item(row, 0).text() # 首列为配置名称
        cfgValue = self.ui.table.item(row, column).text()
```

### 边界线样式

表格控件的边界线颜色可以通过QSS 属性 `gridline-color` 指定

如下所示

```py
QTableWidget {
    gridline-color: green;
}
```

就会指定表格边界线颜色为 绿色。

### 实战练习

表格控件常用于展示行列结构的数据， 比如数据库数据。下面的截图是实战班的一个数据库 和 表格控件 数据联动的练习。

小班学员请联系老师获取相关练习和参考代码。

![image-20221016230027249](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230027656-1106749020.png)

## 常用控件3

## 单选按钮 和 按钮组

`QRadioButton` 是单选按钮，如下图所示

![image-20221016230047993](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230048315-1920867629.png)

### 说明

`同一个父窗口` 里面的多个单选按钮，只能选中一项。

如果你有多组单选按钮， 每组都应该有不同的父控件，或者不同的Layout。

通常建议：多组单选按钮，放到不同的 按钮组 `QButtonGroup` 中

[具体内容，点击这里，查看视频讲解](https://www.bilibili.com/video/BV1cJ411R7bP?p=12)

### 信号：选中状态改变

如果用户操作点击了按钮组 `QButtonGroup` 中的一个按钮， QButtonGroup 就会发出 `buttonClicked` 信号，可以这样指定处理该信号的函数

```py
buttongroup.buttonClicked.connect(handleButtonClicked)
```

然后，在处理函数中调用QButtonGroup对象的 `checkedButton()` 函数，返回值就是被选中的按钮对象。

再调用这个返回的按钮对象的 `text()` 方法得到界面文本，就可以知道是哪个选项被选中了。

### 勾选按钮 和 按钮组

`QCheckBox` 是勾选按钮，如下图所示

![image-20221016230108282](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230108570-1344835006.png)

### 说明

通常建议：多组勾选按钮，放到不同的 按钮组 `QButtonGroup` 中，按钮组就是父控件。



可以在 Qt设计师中设置 QButtonGroup 的 `exclusive` 属性， 来控制 是否 只能单选一个选项。

### 信号：选中状态改变

如果用户操作点击了按钮组 `QButtonGroup` 中的一个按钮， QButtonGroup 就会发出 `buttonClicked` 信号，可以这样指定处理该信号的函数

```py
buttongroup.buttonClicked.connect(handleButtonClicked)
```



QButtonGroup 设置为 `单选` 情况下：

在处理函数中调用QButtonGroup对象的 `checkedButton()` 函数，返回值就是被选中的按钮对象。

再调用这个返回的按钮对象的 `text()` 方法得到界面文本，就可以知道是哪个选项被选中了。



QButtonGroup 设置为 `多选` 情况下：

要得知哪些按钮被选中， 可以 对所有该组中的 按钮调用 `isChecked` 方法 ，来判断。

### tab页控件

我们可以通过tab页控件把界面分为好几个页面，如下所示

![image-20221016230125125](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230125640-178767109.png)

通过Qt designer 只需要拖拽控件到各个页面即可。

要修改tab页的标题，可以先点击该tab页，然后在下图所示处修改

![image-20221016230136538](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230137363-129065719.png)

### tab页中布局Layout

如果我们要在tab页上布局， 你可能会在对象查看器总直接右键点击该tab，可以你会发现 右键菜单里面没有布局项。

这是 Qt designer 非常坑爹的地方，我当时足足花了一个小时才找到方法。

1. 首先需要你在tab页上添加一个控件
2. 然后点击 在对象查看器 右键点击上层 TabWidget ，这时，你就会发现有布局菜单了

[点击这里，看视频讲解tab页中布局Layout](https://www.bilibili.com/video/BV1cJ411R7bP?p=13)

### 进度条

`QProgressBar` 是进度条，如下图所示

![image-20221016230153326](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230153603-97869925.png)

### 说明

进度条也是一个常用的控件，当程序需要做一件比较耗费时间的任务（比如统计数据，下载文件等）时，可以用来向用户指示操作的进度。

而且有了进度显示，用户就知道应用程序仍在运行，并没有出问题。

QProgressBar进度条把每个进度称之为一个step（步骤）。

我们可以通过它的 `setRange` 方法设定步骤个数，比如

```py
progressBar.setRange(0,5)
```

就设定了，进度分为5步。

然后，通过 `setValue` 方法，指定当前完成到了哪一步，比如

```py
progressBar.setValue(3)
```

就表示完成了 3/5， 也就是 60%， 进度条就会显示60%的进度。



可以使用reset()将进度条倒退到开头。



有时候我们的任务没法知道完成了多少，比如下载一个未知大小的文件。

这时，可以把range 范围都设置为0，这样，进度条会显示忙碌指示符，而不是显示进度百分比。



下面是一个进度条程序的示例代码

```py
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QProgressBar,QMessageBox
from time import sleep
from threading import  Thread

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)

        self.progressBar = QProgressBar(self.window)
        self.progressBar.resize(300, 20)
        self.progressBar.move(80, 30)
        # 进度是 0 - 5，
        self.progressBar.setRange(0,5)

        self.button = QPushButton('统计', self.window)
        self.button.move(80, 80)

        self.button.clicked.connect(self.handleCalc)

        # 统计进行中标记，不能同时做两个统计
        self.ongoing = False

    def handleCalc(self):
        def workerThreadFunc():
            self.ongoing = True
            for i in range(1,6):
                sleep(1)
                # 设置进度值
                self.progressBar.setValue(i)
            self.ongoing = False

        if self.ongoing:
            QMessageBox.warning(
                self.window,
                '警告','任务进行中，请等待完成')
            return

        # 通常任务执行比较耗时，应该在新的线程中进行
        # 否则会阻塞主线程显示界面
        worker = Thread(target=workerThreadFunc)
        worker.start()

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
```



上面的代码，运行时，会有很多告警，因为我们在新线程中操作界面对象，容易出问题。

更合理的方法是通过信号，在线程之间传递信息，对界面的操作都在主线程中完成。

如下

```py
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QProgressBar,QMessageBox
from time import sleep
from threading import  Thread
from PySide2.QtCore import Signal,QObject

# 信号库
class SignalStore(QObject):
    # 定义一种信号
    progress_update = Signal(int)
    # 还可以定义其他作用的信号

# 实例化
so = SignalStore()

class Stats():
    def __init__(self): 
        # 连接信号到处理的slot函数
        so.progress_update.connect(self.setProgress)
        
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)

        self.progressBar = QProgressBar(self.window)
        self.progressBar.resize(300, 20)
        self.progressBar.move(80, 30)
        # 进度是 0 - 5，
        self.progressBar.setRange(0,5)

        self.button = QPushButton('统计', self.window)
        self.button.move(80, 80)

        self.button.clicked.connect(self.handleCalc)

        # 统计进行中标记，不能同时做两个统计
        self.ongoing = False

    def handleCalc(self):
        def workerThreadFunc():
            self.ongoing = True
            for i in range(1,6):
                sleep(1)
                # 发出信息，通知主线程进行进度处理
                so.progress_update.emit(i)
            self.ongoing = False

        if self.ongoing:
            QMessageBox.warning(
                self.window,
                '警告','任务进行中，请等待完成')
            return

        worker = Thread(target=workerThreadFunc)
        worker.start()

    # 处理进度的slot函数
    def setProgress(self,value):
        self.progressBar.setValue(value)

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
```

### 数字输入框

`QSpinBox` 是数字输入框，可以输入或使用上下箭头选择数字，如下图所示

![image-20221016230216574](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230217161-654959992.png)

### 获取数字

通过 `value` 方法获取编辑框内的文本内容，比如

```py
number = box.value()
```

注意：返回的是整数对象，不是字符串

### 设置数字

通过 `setValue` 方法可以设置提示文本内容，比如

```py
box.setValue(100)
```

### 日期控件

`QDateEdit` 类可以用来选择日期时间，如下图所示

![image-20221016230232546](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230232867-1134052209.png)

### 获取日期

当用户点击日期时间控件并且选取了 日期和时间，后来程序要获取这个控件里面选定的日期时间，可以使用date方法获取日期对象。

如下所示

```py
# 返回 PySide2.QtCore.QDate 对象
qdate = dateEdit.date()

# 可以转化为 指定格式的字符串
dateStr = qdate.toString('yyyy-MM-dd')

# 也可以获取年月日 对应的数字 ，比如日期是2020年5月2号
year = qdate.year()   # 返回 2020
month = qdate.month() # 返回 5
day = qdate.day()     # 返回 2
```

QDate 对象的具体说明[参考官方文档](https://doc.qt.io/qtforpython-5.12/PySide2/QtCore/QDate.html)

### 选择文件框

`QFileDialog` 类可以用来选择文件或者目录，如下图所示

![image-20221016230247481](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230247954-540986286.png)

### 选择目录

通过 `getExistingDirectory 静态方法` 选择目录。

该方法，第一个参数是父窗口对象，第二个参数是选择框显示的标题。

比如

```py
from PySide2.QtWidgets import QFileDialog

filePath = QFileDialog.getExistingDirectory(self.ui, "选择存储路径")
```

返回值即为选择的路径字符串。

如果用户点击了 选择框的 取消选择按钮，返回 空字符串。

### 选择单个文件

如果你想弹出文件选择框，选择一个 `已经存在` 的文件，可以使用 QFileDialog 静态方法 `getOpenFileName` ，比如

```py
from PySide2.QtWidgets import QFileDialog

filePath, _  = QFileDialog.getOpenFileName(
            self.ui,             # 父窗口对象
            "选择你要上传的图片", # 标题
            r"d:\\data",        # 起始目录
            "图片类型 (*.png *.jpg *.bmp)" # 选择类型过滤项，过滤内容在括号中
        )
```

该方法返回值 是一个元组，第一个元素是选择的文件路径，第二个元素是文件类型，如果你只想获取文件路径即可，可以采用上面的代码写法。

如果用户点击了 选择框的 取消选择按钮，返回 空字符串。



如果你想弹出文件选择框，选择路径和文件名，来 `保存一个文件` ，可以使用 QFileDialog 静态方法 `getSaveFileName` ，比如

```py
from PySide2.QtWidgets import QFileDialog

filePath, _  = QFileDialog.getSaveFileName(
            self.ui,             # 父窗口对象
            "保存文件", # 标题
            r"d:\\data",        # 起始目录
            "json类型 (*.json)" # 选择类型过滤项，过滤内容在括号中
        )
```

### 选择多个文件

如果要选择多个文件，使用 `getOpenFileNames 静态方法`

```py
from PySide2.QtWidgets import QFileDialog

filePaths, _  = QFileDialog.getOpenFileNames(
            self.ui,             # 父窗口对象
            "选择你要上传的图片", # 标题
            r"d:\\data",        # 起始目录
            "图片类型 (*.png *.jpg *.bmp)" # 选择类型过滤项，过滤内容在括号中
        )
```

上例中 filePaths 对应的返回值是一个列表，里面包含了选择的文件。

如果用户点击了 选择框的 取消选择按钮，返回 空列表。

## 常用控件4

## 树控件

`QTreeWidget 树控件` 树控件， 是和 `QTreeWidgetItem 树节点控件` 结合使用的。

如下图所示

![image-20221016230313858](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230314312-744579961.png)

### 提示框

`QMessageBox` 类可以用来弹出各种提示框

[官网介绍](https://doc.qt.io/qtforpython-5.12/PySide2/QtWidgets/QMessageBox.html)

该类可以通过一系列静态方法，显示 如下弹出框

- 错误报告

![image-20221016230328034](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230328476-226884015.png)

使用 `critical` 方法

```py
QMessageBox.critical(
    self.ui,
    '错误',
    '请选择爬取数据存储路径！')
```

- 警告
- ![image-20221016230343559](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230343953-943082598.png)

使用 `warning` 方法

```py
QMessageBox.warning(
    self.ui,
    '阅读太快',
    '阅读客户协议必须超过1分钟')
```

- 信息提示
- ![image-20221016230401837](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230402143-1305046255.png)

使用 `information` 方法

```py
QMessageBox.information(
    self.ui,
    '操作成功',
    '请继续下一步操作')
```

也可以使用 `about` 方法

```py
QMessageBox.about(
    self.ui,
    '操作成功',
    '请继续下一步操作')
```

- 确认继续

- ![image-20221016230417329](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230417696-1385619192.png)

- 使用 `question` 方法

  ```py
  choice = QMessageBox.question(
      self.ui,
      '确认',
      '确定要删除本文件吗？')
  
  if choice == QMessageBox.Yes:
      print('你选择了yes')
  if choice == QMessageBox.No:
      print('你选择了no')
  ```

  ### 输入对话框

  `QInputDialog` 输入对话框 只让用户输入一行数据信息，比如 姓名、年龄等。

  可以方便的用来获取简单的信息。



![image-20221016230433522](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230433833-647436725.png)

比如

```py
from PySide2.QtWidgets import QInputDialog,QLineEdit

# 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
title, okPressed = QInputDialog.getText(
    self, 
    "输入目录名称",
    "名称:",
    QLineEdit.Normal,
    "")

if not okPressed:
    print('你取消了输入')
```



常用的方法有：

- getText

  弹出对话框，让用户输入 单行文本

- getMultiLineText

  弹出对话框，让用户输入 多行文本

- getInt

  弹出对话框，让用户输入 整数

- getItem

  弹出对话框，让用户选择 选项

  ```py
  items = ["春天", "夏天", "秋天", "冬天"]
  
  item, ok = QInputDialog().getItem(self, 
                                    "请选择",
                                    "季节:", 
                                    items, 
                                    0, 
                                    False)
  if ok and not item.isEmpty():
      itemLabel.setText(item)
  ```

### 菜单

可以在 Qt Designer上很方便的添加菜单，如下所示

![image-20221016230448467](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230448983-1184529418.png)

点击菜单的信号是 `triggered`， 处理点击菜单的的代码如下

```py
self.ui.actionOpenFile.triggered.connect(self.openPageFile)
```



注意：如果菜单和工具栏有 `相同的 action` ，通常是先在 动作编辑器 创建一个action， 然后分别拖动到 菜单 和 工具栏

### 工具栏

在 Qt 设计师上添加工具栏，可以右键点击 `Main Window` 类型的窗体空白处，如下所示

![image-20221016230503972](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230504426-1735272335.png)

选择添加工具栏



注意，只有 `Main Window` 类型的窗体，才能添加工具栏，如下

![image-20221016230515443](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230515764-241248541.png)

添加工具栏后，还要在工具栏上添加图标。

方法是点击右下角 动作编辑器，新建动作，如下图所示

![image-20221016230530588](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230531042-743730125.png)

然后如下图所示进行设置

![image-20221016230545803](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230546156-1201243308.png)

添加动作成功后，就可以直接拖到工具栏上了。



然后，在代码中定义动作触发后的处理函数，如下所示

```py
self.ui.actionAddNote.triggered.connect(self.actionAddNode)
```

### 状态栏

[官网介绍](https://doc.qt.io/qtforpython-5.12/PySide2/QtWidgets/QStatusBar.html)

要在状态栏显示文本信息，只需要调用 QStatusBar 的 `showMessage` 方法

```py
self.ui.statusbar.showMessage(f'打开文件{filePath}')
```

### 剪贴板

Qt程序可以获取和设置剪贴板内容

[官网介绍](https://doc.qt.io/qtforpython-5.12/PySide2/QtGui/QClipboard.html)

```py
from PySide2.QtGui import QGuiApplication

cb = QGuiApplication.clipboard()
# 获取剪贴板内容
originalText = cb.text()
# 设置剪贴板内容
clipboard.setText(newText)
```

### MDI 多个子窗口

QMdiArea 提供了一个主窗口区，里面可以存放多个 QMdiSubWindow 子窗口

如图：

![image-20221016230617200](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230618657-2021273294.png)

## 后台线程 与 信号界面阻塞问题

前面我们的练习里开发了一个类似 Postman 的HTTP接口测试工具。

其中，具体发送请求消息的代码如下

```py
    def sendRequest(self):

        method = self.ui.boxMethod.currentText()
        url    = self.ui.editUrl.text()
        payload = self.ui.editBody.toPlainText()

        # 获取消息头
        headers = {}
        # 此处省略一些对消息头的处理

        req = requests.Request(method,
                               url,
                               headers=headers,
                               data=payload
                               )

        prepared = req.prepare()

        self.pretty_print_request(prepared)
        s = requests.Session()
        
        try:
            # 发送请求并且接收响应消息
            r = s.send(prepared)
            # 打印出响应消息
            self.pretty_print_response(r)
        except:
            self.ui.outputWindow.append(
                traceback.format_exc())
```

这里有一个问题：

我们 `点击发送按钮` 发送HTTP消息消息，如果服务端接收处理的比较慢，就会导致下面这行代码中的send方法要比较长的时间才能返回。

```py
r = s.send(prepared)
```

这会导致什么问题呢？

假设10秒钟后，才接收到服务端的响应消息，这时候，界面就会 `僵死` 10秒钟。

这期间，你点击界面没有任何反应。

为什么呢？

## 原因

这是因为，我们现在的代码都是在主线程中执行的。

其中最末尾的代码

```py
app.exec_()
```

其实会让主线程进入一个死循环，循环不断的处理 用户操作的事件。

当我们点击发送按钮后，Qt的 核心代码就会接受到这个 点击事件，并且调用相应的 slot函数去处理。

因为我们代码做了这样的设置

```py
        # 信号处理
        self.ui.buttonSend.clicked.connect(self.sendRequest)
```

指定了点击发送按钮由 sendRequest 方法处理。

如果这个sendRequest 很快能接收到 服务端的相应，那么sendRequest就可以很快的返回。

返回后， 整个程序又进入到 app.exec_() 里面接收各种 事件，并且调用相应的函数去处理。界面就不会僵死，因为所有的操作界面的事件，都能得到及时的处理。

但是，如果这个sendRequest 要很长时间才能返回，这段时间内，整个程序就停在 下面这行代码处

```py
r = s.send(prepared)
```

自然就没有机会去处理其他的用户操作界面的事件了，当然程序就僵死了。

## 子线程处理

典型的一种解决方法就是使用多线程去处理。

关于Python的多线程的讲解，[可以点击参考我们这里的教程](https://www.byhy.net/tut/py/extra/multi_thread/)

修改代码如下

```py
    def sendRequest(self):

        method = self.ui.boxMethod.currentText()
        url    = self.ui.editUrl.text()
        payload = self.ui.editBody.toPlainText()

        # 获取消息头
        headers = {}
        # 此处省略一些对消息头的处理

        req = requests.Request(method,
                               url,
                               headers=headers,
                               data=payload
                               )

        prepared = req.prepare()

        self.pretty_print_request(prepared)
        s = requests.Session()

        # 创建新的线程去执行发送方法，
        # 服务器慢，只会在新线程中阻塞
        # 不影响主线程
        thread = Thread(target = self.threadSend,
                        args= (s, prepared)
                        )
        thread.start()

    # 新线程入口函数
    def threadSend(self,s,prepared):

        try:
            r = s.send(prepared)
            self.pretty_print_response(r)
        except:
            self.ui.outputWindow.append(
                traceback.format_exc())
```

这样，通过创建新的线程去执行发送方法，服务器响应再慢，也只会在新线程中阻塞

主线程启动新线程后，就继续执行后面的代码，返回继续运行Qt的事件循环处理 ，可以响应用户的操作，就不会僵死了。

VIP 实战班学员请联系老师获取完整代码示例。

## 子线程发信号更新界面

[点击这里，边看视频讲解，边学习下面的内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=19)

上面的示例中，我们在子线程里面操作了界面，如下代码所示

```py
    def threadSend(self,s,prepared):

        try:
            r = s.send(prepared)
            # 在新线程中输出内容到界面
            self.pretty_print_response(r)
        except:
            # 在新线程中输出内容到界面
            self.ui.outputWindow.append(
                traceback.format_exc())
```

Qt建议： `只在主线程中操作界面` 。

在另外一个线程直接操作界面，可能会导致意想不到的问题，比如：输出显示不全，甚至程序崩溃。

但是，我们确实经常需要在子线程中 更新界面。比如子线程是个爬虫，爬取到数据显示在界面上。

怎么办呢？



这时，推荐的方法是使用信号。

前面我们曾经看到过 各种 Qt 控件可以发出信号，比如 被点击、被输入等。

我们也可以自定义类，只要这个类继承QObject类，就能发出自己定义的各种Qt信号，具体做法如下：

- 自定义一个Qt 的 QObject类，里面封装一些自定义的 Signal信号

  怎么封装自定义的 Signal信号？参考下面的示例代码。

  一种信号定义为 该类的 一个 静态属性，值为Signal 实例对象即可。

  可以定义 `多个` Signal静态属性，对应这种类型的对象可以发出的 `多种` 信号。

  注意：Signal实例对象的初始化参数指定的类型，就是 发出信号对象时，传递的参数数据类型。因为Qt底层是C++开发的，必须指定类型。

- 定义主线程执行的函数处理Signal信号（通过connect方法）

- 在新线程需要操作界面的时候，就通过自定义对象 发出 信号

  通过该信号对象的 emit方法发出信号， emit方法的参数 传递必要的数据。参数类型 遵循 定义Signal时，指定的类型。

- 主线程信号处理函数，被触发执行，获取Signal里面的参数，执行必要的更新界面操作



一个示例代码如下

```py
from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
from threading import Thread

from PySide2.QtCore import Signal,QObject

# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):

    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(QTextBrowser,str)

    # 还可以定义其他种类的信号
    update_table = Signal(str)

# 实例化
global_ms = MySignals()    

class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')

        # 自定义信号的处理函数
        global_ms.text_print.connect(self.printToGui)


    def printToGui(self,fb,text):
        fb.append(str(text))
        fb.ensureCursorVisible()

    def task1(self):
        def threadFunc():
            # 通过Signal 的 emit 触发执行 主线程里面的处理函数
            # emit参数和定义Signal的数量、类型必须一致
            global_ms.text_print.emit(self.ui.infoBox1, '输出内容')
        
        thread = Thread(target = threadFunc )
        thread.start()

    def task2(self):
        def threadFunc():
            global_ms.text_print.emit(self.ui.infoBox2, '输出内容')

        thread = Thread(target=threadFunc)
        thread.start()
```

## 显示样式

## QSS 概念

[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=15)

前面，我们开发的程序界面有点简陋。

大家[点击这里](https://cdn2.byhy.net/files/py/qt/qss_pilot.zip)，下载一个白月黑羽实战班学员开发的程序界面代码，解压后，拖动里面的main.ui界面文件到Qt设计师里面。

像这样

![image-20221016230847427](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016230847868-608076113.png)

要让产品更好看一些，通常就是指定界面元素的 `显示样式` 。比如指定颜色、字体、间距。

像这样

![image-20221016231016515](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231017049-1339115630.png)

Qt有种定义界面显示样式的方法，称之为 `Qt Style Sheet` ，简称 `QSS`

如果你学习过Web网页开发，就会发现这个名词和 `CSS` 特别的相似。

没错，它的 语法和用途 和 CSS 特别的相似。



我们来看上图对应的示例

如果在设计师界面上 最上层的 MainWindow 对象 `styleSheet` 属性指定如下的内容

```css
QPushButton { 
    color: red ;
    font-size:15px;
}
```

就会发现，所有的按钮上的文字都变成了红色的，并且字体变大了。

注意这个指定界面元素 显示样式的 语法，由 selector 和 declaration 组成。

花括号前面的 部分，比如示例中的 `QPushButton` 称之为 selector。

花括号后面的 部分，比如示例中的

```css
{ 
    color: red ;
    font-size:15px;
}
```

称之为 Properties （样式属性）

### selector 选择器

[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=16)

花括号前面的 部分称之为 selector（中文可以叫 选择器），用来 告诉Qt `哪些特征的元素` 是你要设定显示效果的。

比如：`QPushButton` 选择所有类型为 QPushButton （包括其子类） 的界面元素 。

QSS selector语法 几乎 和 Web CSS 的 selector语法没有什么区别，了解CSS的朋友可以轻松掌握。

具体可以[点击这里，参考官方文档中的说明](https://doc.qt.io/qt-5/stylesheet-syntax.html)

### selector常见语法

| Selector            | 示例                        | 说明                                              |
| ------------------- | --------------------------- | ------------------------------------------------- |
| Universal Selector  | `*`                         | 星号匹配所有的界面元素                            |
| Type Selector       | `QPushButton`               | 选择所有 QPushButton类型 （包括其子类）           |
| Class Selector      | `.QPushButton`              | 选择所有 QPushButton类型 ，但是不包括其子类       |
| ID Selector         | `QPushButton#okButton`      | 选择所有 `对象名为 okButton` 的QPushButton类型    |
| Property Selector   | `QPushButton[flat="false"]` | 选择所有 flat 属性值为 false 的 QPushButton类型。 |
| Descendant Selector | `QDialog QPushButton`       | 选择所有 QDialog `内部` QPushButton类型           |
| Child Selector      | `QDialog > QPushButton`     | 选择所有 QDialog `直接子节点` QPushButton类型     |

### Pseudo-States 伪状态

我们可以这样指定当鼠标移动到一个元素上方的时候，元素的显示样式

```css
QPushButton:hover { color: red }
```

再比如，指定一个元素是disable状态的显示样式

```css
QPushButton:disabled { color: red }
```

再比如，指定一个元素是鼠标悬浮，并且处于勾选（checked）状态的显示样式

```css
QCheckBox:hover:checked { color: white }
```

### 优先级

如果一个元素的显示样式被多层指定了， `越靠近元素本身` 的选择指定，优先级越高

### 样式属性

[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/BV1cJ411R7bP?p=17)

QSS的样式属性和网页CSS非常相似。

QSS支持的具体样式，可以[点击这里，查看Qt官方文档](https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-properties)

我们这里介绍一些常见的样式属性

### 背景

可以指定某些元素的背景色，像这样

```css
QTextEdit { background-color: yellow }
```

颜色可以使用红绿蓝数字，像这样

```css
QTextEdit { background-color: #e7d8d8 }
```



也可以像这样指定背景图片

```css
QTextEdit {
    background-image: url(gg03.png);
}
```

### 边框

可以像这样指定边框 `border:1px solid #1d649c;`

其中

`1px` 是边框宽度

`solid` 是边框线为实线， 也可以是 `dashed`(虚线) 和 `dotted`（点）

比如

```css
*[myclass=bar2btn]:hover{
	border:1px solid #1d649c;
}
```



边框可以指定为无边框 `border:none`

### 字体、大小、颜色

可以这样指定元素的 文字字体、大小、颜色

```css
*{	
	font-family:微软雅黑;
	font-size:15px;
	color: #1d649c;
}
```

### 宽度、高度

可以这样指定元素的 宽度、高度

```css
QPushButton {	
	width:50px;
	height:20px;
}
```

### margin、padding

见下图，根据视频讲解，理解margin、padding 的概念

![image-20221016231052624](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231053084-922869749.png)

可以这样指定元素的 元素的 margin

```css
QTextEdit {
	margin:10px 11px 12px 13px
}
```

分别指定了元素的上右下左margin。

也可以使用 margin-top, margin-right, margin-bottom, margin-left 单独指定 元素的上右下左margin

比如

```css
QTextEdit {
	margin:10px 50px;
	padding:10px 50px;
}
```

## Matplotlib 绘图

Matplotlib 提供非常全面的数据可视化功能。

## 安装

非常简单，直接 执行 `pip install matplotlib` 即可

## 简单示例

下面的代码，运行一下看看

```py
import matplotlib.pyplot as plt

# 如果只传入一个数组作为参数， matplotlib 认为是 Y 轴的坐标
# 并自动产生 从 0 开始的 对应 X 轴坐标： 0、1、2、3 ...
plt.plot([2, 4, 6, 8])
plt.ylabel('some numbers')
plt.show()
```

当然，我们也经常需要 `同时指定` 作图点的 X 坐标 和 Y 坐标

```py
import matplotlib.pyplot as plt

# 绘图点的 X 轴 坐标依次为 1, 3, 5, 7
# 绘图点的 Y 轴 坐标依次为 2, 4, 6, 8
plt.plot([1, 3, 5, 7], [2, 4, 6, 8])
plt.ylabel('some numbers')
plt.show()
```

可以在一幅图上，画多组数据，如下所示

```py
import matplotlib.pyplot as plt

# 画一组数据
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# 再画一组数据
plt.plot([1, 2, 3, 4], [1, 3, 5, 8])
plt.show()
```

## 显示中文字符

matplotlib的缺省字体不支持中文，我们可以指定一个支持中文的字体

```py
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
# 设定字体为微软雅黑
plt.rcParams['font.sans-serif']=['Microsoft Yahei']

plt.plot([1, 2, 3, 4])
plt.xlabel('times 次数')
plt.show()
```

## 显示格式

给定了xy坐标作为 plot 的前两个参数， 还可以有可选的第三个参数，表示数据绘制的风格，缺省值为 `b- `。

`b` 表示 蓝色， `-` 表示 是线图。

如果想显示红色点图，就是 风格参数 `r.` ， `r` 代表红色， `.` 代表点， 如下

```py
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r.')
plt.show()
```

完整的 风格参数定义，[点击这里参考官方文档](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)

## 指定宽度

我们可以 使用参数 `linewidth` 指定绘图的线条宽度

```py
import matplotlib.pyplot as plt

plt.plot(range(10), range(10), linewidth=0.5)
plt.show()
```

我们可以 使用参数 `markersize` 指定点的大小

```py
import matplotlib.pyplot as plt

plt.plot(range(10), range(10), 'r.', markersize=2.5)
plt.show()
```

## numpy 数组

其实 matplotlib 内部都是把作图数据转化为 numpy 的 ndarray 数组类型进行处理的。

所以，我们当然可以，直接使用 numpy 的数组作为 画图数据

```py
import matplotlib.pyplot as plt
import numpy as np

# arange 就像 Python中的range
# 从 0 到 5 步长为 0.2
t = np.arange(0, 5, 0.2)

# 使用 numpy 的ndarray 作为数据
plt.plot(t, t**2, 'b.')
plt.show()
```

## 柱状图

使用 `bar` 方法可以画柱状图

```py
import matplotlib.pyplot as plt

names = ['2016', '2017', '2018']
values = [1, 10, 100]

plt.bar(names, values)
plt.show()
```

## 饼图

```py
import matplotlib.pyplot as plt

# 指定饼图的每个切片名称
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# 指定每个切片的数值，从而决定了百分比
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
```

## 散点图

使用 `scatter` 方法可以画散点图

```py
import matplotlib.pyplot as plt

names = ['2016', '2017', '2018', '2019', '2020']
values = [75, 78, 100, 150, 210]

plt.scatter(names, values)
plt.show()
```

## 多个子图（axes）

`subplot` 方法可以用来创建多个子图（axes）。

前面的示例中，我们并没有创建子图，其实， matplotlib缺省会帮我们调用 `plt.subplot(1,1,1)` 指定 1行，1列，共1个子图，当前子图为第1个.

如果你想指定更多的子图，可以这样，

```py
import matplotlib.pyplot as plt
import numpy as np

# arange 就像 Python中的range
# 从 0 到 5 步长为 0.2
t = np.arange(0, 5, 0.2)

# 指定2行，1列，共两个axe，当前使用第1个绘图块
plt.subplot(2,1,1)   
plt.plot(t, t**2, 'b.')


# 当前使用第2个绘图块
plt.subplot(2,1,2)   
plt.plot(t, t**2, 'r-')
plt.show()
```

结果如下：

![image-20221016231158105](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231158633-2070836709.png)

### 多个绘图（Figure）

matplotlib 每个绘图区都对应一个 Figure 对象。

一个绘图 Figure 对象 里面可以包含多个 subplot对象。

而我们的程序可以同时打开多个绘图 Figure 对象。

比如下图，你可以发现有两个绘图窗口，对应两个 Figure 对象

![image-20221016231213077](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231213597-1446070993.png)

前面的示例中，我们并没有声明创建Figure对象，其实是默认使用了 matplotlib 缺省Figure 对象。

默认Figure ，也就是相当于调用 `plt.figure(1) `指定第一个绘图。

我们可以像下面这样创建多个Figure

```py
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

plt.show()
```

运行代码，就可以产生上面的图形。



### 图形中的文字

```py
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

# x轴标题
plt.xlabel('Smarts')
# y轴标题
plt.ylabel('Probability')
# 子图标题
plt.title('Histogram of IQ')
# 指定坐标处添加文本
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

结果如下：

![image-20221016231322731](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231323242-1904105574.png)

我们可以像这样，指定标题的颜色

```py
t = plt.xlabel('my data', fontsize=14, color='red')
```

### x轴刻度文字垂直

有时候我们作图时，x轴文字内容比较长，会出现重叠，这时需要x轴刻度文字垂直，可以如下设置

```py
import matplotlib.pyplot as plt
# 设定字体为微软雅黑
plt.rcParams['font.family'] = 'Microsoft Yahei'

# x刻度垂直，否则字会重叠
plt.xticks(rotation=-90)

# 加长底部空间，否则文字显示不全
plt.subplots_adjust(bottom=0.45)
```

### 嵌入Qt中

有时候，我希望Qt程序界面中包含 matplotlib绘图内容，怎么把 matplotlib绘图嵌入Qt中 呢？

就像这样

![image-20221016231429018](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231429697-9297058.png)

## PyQtGraph 绘图

### 数据绘图方案

Python语言 的数据可视化（绘图） 方法，常见的有 Matplotlib 和 PyQtGraph

- Matplotlib

说到 Python语言 的数据作图， Matplotlib 当然是最有名的。

优点： 功能完备、成熟稳定、社区生态圈庞大。

缺点： 某些作图场景性能不高。

- PyQtGraph

PyQtGraph 是基于Qt 的纯Python 库。

优点： 大数据量的作图性能高于 Matplotlib， 动态更新图的性能也比Matplotlib高。

并且和Qt图形界面框架完美融合，因为它的2D作图就是基于 Qt View Framework 开发的。

缺点： 作图功能没有Matplotlib多，开发社区没有Matplotlib大。



那么，我们应该使用哪种方案呢？我的建议是：

如果你已经使用Qt开发图形界面程序了，并且作图功能是PyQtGraph支持的， 建议使用 PyQtGraph，因为它和Qt界面无缝结合。

否则 使用 Matplotlib。



本文先介绍 PyQtGraph 的使用示例。

### PyQtGraph 安装

```py
pip install pyqtgraph
```

### 官方文档 和 案例

PyQtGraph 官方文档可以[点击这里查阅](https://pyqtgraph.readthedocs.io/en/latest/introduction.html)

其中包含了很多示例代码，我们只需运行如下代码，即可查看这些demo和对应的代码

```py
import pyqtgraph.examples
pyqtgraph.examples.run()
```

### 曲线图 示例

下面是一个最常见的 根据x/y轴对应的值 作曲线图的例子

```py
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

# 创建 绘制窗口类 PlotWindow 对象，内置一个绘图控件类 PlotWidget 对象
pw = pg.plot()

# 设置图表标题、颜色、字体大小
pw.setTitle("气温趋势",color='008080',size='12pt')

# 背景色改为白色
pw.setBackground('w')

# 显示表格线
pw.showGrid(x=True, y=True)

# 设置上下左右的label
# 第一个参数 只能是 'left', 'bottom', 'right', or 'top'
pw.setLabel("left", "气温(摄氏度)")
pw.setLabel("bottom", "时间")

# 设置Y轴 刻度 范围
pw.setYRange(min=-10,  # 最小值
             max=50)  # 最大值

# 创建 PlotDataItem ，缺省是曲线图
curve = pw.plot( pen=pg.mkPen('b')) # 线条颜色

hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

curve.setData(hour, # x坐标
              temperature  # y坐标
              )

QtGui.QApplication.instance().exec_()
```

### 清除画图区，重新绘制

如果使用新的数据再次绘图，可以先调用clear方法清除原来的内容（plotitem），如下

```py
# 清除原来的plot内容
pw.clear()

# 创建 PlotDataItem ，缺省是曲线图
curve = pw.plot( pen=pg.mkPen('b')) # 线条颜色
hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [130, 132, 134, 132, 133,131, 129, 132, 135, 145]

curve.setData(hour, # x坐标
              temperature  # y坐标
              )
```

### PlotWidget 和 GraphicsLayoutWidget

PyQtGraph 中 绘图控件类 有两种 PlotWidget 和 GraphicsLayoutWidget， 都是 [GraphicsView](https://pyqtgraph.readthedocs.io/en/latest/widgets/graphicsview.html?highlight=setBackground#graphicsview) 子类。GraphicsView 是 Qt 的 QGraphicsView 子类，在其基础上改进了一些功能。

PlotWidget 只能内置一个 绘图对象PlotItem， 而 GraphicsLayoutWidget 可以内置多个 绘图对象。 通常我们使用最多的是PlotWidget



PlotWidget对象的 内置绘图对象 [PlotItem](https://pyqtgraph.readthedocs.io/en/latest/graphicsItems/plotitem.html#pyqtgraph.PlotItem) ，可以通过 getPlotItem() 方法获取。

为了方便，大部分的PlotItem方法都可以直接通过 PlotWidget对象调用。 比如我们上面示例代码中的 setTitle、showGrid、setLabel、setYRange、plot 等。



调用 plot方法，会创建一个PlotDataItem， 缺省是曲线图



关于PyQtGraph绘图基本架构的更多细节，[点击这里查看官方文档](https://pyqtgraph.readthedocs.io/en/latest/plotting.html)

### 嵌入到Qt程序界面中

上面的例子，图表是在单独的程序中运行显示。

如果我们要把它 嵌入到我们的Qt程序界面 中，主要通过 pyqtgraph 的 PlotWidget 或者 GraphicsLayoutWidget 控件类， 代码如下所示

```py
from PySide2 import QtWidgets
import pyqtgraph as pg

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('pyqtgraph作图示例')

        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()

        # 设置图表标题
        self.pw.setTitle("气温趋势",color='008080',size='12pt')

        # 设置上下左右的label
        self.pw.setLabel("left","气温(摄氏度)")
        self.pw.setLabel("bottom","时间")
        # 背景色改为白色
        self.pw.setBackground('w')


        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # hour 和 temperature 分别是 : x, y 轴上的值
        self.pw.plot(hour,
                     temperature,
                     pen=pg.mkPen('b') # 线条颜色
                    )

        # 创建其他Qt控件
        okButton = QtWidgets.QPushButton("OK")
        lineEdit = QtWidgets.QLineEdit('点击信息')
        # 水平layout里面放 edit 和 button
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(okButton)

        # 垂直layout里面放 pyqtgraph图表控件 和 前面的水平layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.pw)
        vbox.addLayout(hbox)

        # 设置全局layout
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = MainWindow()
    main.show()
    app.exec_()
```

### 柱状图

pyqtgraph 可以产生这样的 柱状图

![image-20221016231516899](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231517262-905330669.png)

### 绘制多个图形

可以使用 GraphicsLayoutWidget，创建多个绘图对形

![image-20221016231533135](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231533458-281773087.png)

对应代码如下

```
本节内容 仅 内部学员 可见
```

### 实时更新图

要画动态的实时更新图，只需要在把变更的内容重新plot即可。

示例代码如下

```py
from PySide2 import QtWidgets
from pyqtgraph.Qt import  QtCore
import pyqtgraph as pg
import sys
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('pyqtgraph作图')

        # 创建 PlotWidget 对象
        self.pw = pg.PlotWidget()

        # 设置图表标题
        self.pw.setTitle("气温趋势",
                         color='008080',
                         size='12pt')

        # 设置上下左右的label
        self.pw.setLabel("left","气温(摄氏度)")
        self.pw.setLabel("bottom","时间")

        # 设置Y轴 刻度 范围
        self.pw.setYRange(min=-10, # 最小值
                          max=50)  # 最大值

        # 显示表格线
        self.pw.showGrid(x=True, y=True)

        # 背景色改为白色
        self.pw.setBackground('w')

        # 设置Y轴 刻度 范围
        self.pw.setYRange(min=-10, # 最小值
                          max=50)  # 最大值

        # 居中显示 PlotWidget
        self.setCentralWidget(self.pw)

        # 实时显示应该获取 PlotDataItem对象, 调用其setData方法，
        # 这样只重新plot该曲线，性能更高
        self.curve = self.pw.plot(
            pen=pg.mkPen('r', width=1)
        )

        self.i = 0
        self.x = [] # x轴的值
        self.y = [] # y轴的值

        # 启动定时器，每隔1秒通知刷新一次数据
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000)

    def updateData(self):
        self.i += 1
        self.x.append(self.i)
        # 创建随机温度值
        self.y.append(randint(10,30))

        # plot data: x, y values
        self.curve.setData(self.x,self.y)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    main = MainWindow()
    main.show()
    app.exec_()
```

### 在Qt Designer中加入第三方控件

PyQtGraph图形可以作为一个 Qt的 widget控件，嵌入到 Qt 程序主窗口中。

我们可以在 Qt Designer 中把 PyQtGraph图形控件 作为第三方控件 加入。

比如，像下面这样：

![image-20221016231616645](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231617327-2073062617.png)

通过 Qt Designer，我们可以预先把界面上的控件的位置大小设计好，然后动态加载。

但是 界面上摆放的都是 Qt内置的控件， 那么像 PyQtGraph 里面的 PlotWidget这种第三方控件怎么 放到 Qt Designer中呢？ 我们的代码又怎么去获取到该控件对应的对象呢？


[点击这里，边看视频讲解，边学习以下内容](https://www.bilibili.com/video/av78483752?p=3)



根据上面的视频，产生的界面ui文件在下面的链接zip文件中

https://cdn2.byhy.net/files/qt/stock-01.zip



如果你使用的是PySide2， 对应的代码如下，注意第14行 注册的作用

```py
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg

class Stock:

    def __init__(self):

        loader = QUiLoader()

        # pyside2 一定要 使用registerCustomWidget 
        # 来注册 ui文件中的第三方控件，这样加载的时候
        # loader才知道第三方控件对应的类，才能实例化对象
        loader.registerCustomWidget(pg.PlotWidget)
        self.ui = loader.load("main.ui")

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # 通过控件名称 historyPlot，找到Qt designer设计的 控件
        self.ui.historyPlot.plot(hour,temperature)

app = QApplication([])
stock = Stock()
stock.ui.show()
app.exec_()
```



如果使用 PyQt5，就更简单了， 无需注册，对应的代码如下

```py
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic

class Stock:

    def __init__(self):

        # PyQt5 直接加载ui文件
        # 因为 第三方控件通过promote的定义
        # 已经可以知道 控件类所在模块的路径
        self.ui = uic.loadUi("main.ui")

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        self.ui.historyPlot.plot(hour, temperature)

app = QApplication([])
stock = Stock()
stock.ui.show()
app.exec_()
```



### 轴刻度为字符串

上面的程序运行起来， X轴的刻度是 数字， 如果我们希望轴刻度是文字怎么做呢？

我们参考了这个网址的介绍： https://stackoverflow.com/questions/31775468/show-string-values-on-x-axis-in-pyqtgraph?lq=1

需要定义从数字到字符串的映射列表，参考如下代码

```py
import pyqtgraph as pg

# 刻度表，注意是双层列表
xTick = [[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]]
x = [0,1,2,3,4,5]
y = [1, 2, 3, 4, 5, 6]

win = pg.GraphicsWindow()
stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks(xTick)
plot = win.addPlot(axisItems={'bottom': stringaxis})
curve = plot.plot(x,y)

pg.QtGui.QApplication.exec_()
```

如果使用 PlotWidget，则要获取轴对象，参考代码如下

```py
# self.ui.historyPlot 就是 PlotWidget对象
xax = self.ui.historyPlot.getAxis('bottom')
xax.setTicks(xTick)
```



### 获取鼠标所在处刻度值

有时候，我们的程序需要获取 鼠标在 pyqtgraph 图形上移动时，鼠标所在对应的数据是什么。

```
解决方法，仅供实战班学员参考
```

## 内嵌web浏览器

有时候，我们需要在程序中嵌入浏览器，显示一个指定的网页。

Qt5中，有一个 QtWebEngineWidgets 模块，通过它，可以启动基于Chromium的浏览器（和chrome是同样的内核）进程，并且把web界面内嵌入 Qt程序中。


[参考官网说明](https://doc.qt.io/qt-5/qtwebengine-overview.html)

### 案例

我们可以实现一个内嵌浏览器，打开白月黑羽网站。

整个案例的参考代码，点击这里下载

链接：https://pan.baidu.com/s/1FBLdSU0w_LYSsPUzVjsQsA 提取码：byhy



首先使用Qt designer设计界面。

注意：显示web内容的是 QtWebEngineWidgets 模块里面的 QWebEngineView类。

所以需要 premote 一个QtWindget 控件为 QWebEngineView。详见参考代码中的ui文件。

创建完界面后，使用命令

```
pyside2-uic main.ui > ui_main.py
```

把界面定义转化为Python代码。



然后，编写如下代码，使用 QWebEngineView 打开网址

```py
from PySide2.QtWidgets import QApplication,QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问
        self.ui.webview.load('http://www.baidu.com/')

app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()
```



上述代码的一个问题，就是不能打开新标签页，如果要支持，可以使用QTabWidget。参考代码如下

```py
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        url = QUrl("https://www.163.com")
        view = HtmlView(self)
        view.load(url)
        ix = self.addTab(view, "加载中 ...")
        self.resize(800, 600)

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.tab = self.parent()

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = HtmlView(self.tab)
            ix = self.tab.addTab(webView, "加载中 ...")
            self.tab.setCurrentIndex(ix)
            return webView
        return QWebEngineView.createWindow(self, windowType)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = TabWidget()
    main.show()
    sys.exit(app.exec_())
```



## 项目实战1-数据处理工具

[点击这里，观看项目说明视频讲解](https://www.bilibili.com/video/BV19A411H7dS?p=1)

我们通过一个项目来锻炼 Python 图形界面程序 和 数据处理的 软件开发能力。

该项目主要是为实战班学员提供， 其中的一部分功能是免费开放的，游客也可以锻炼。

可以微信咨询 `byhy44` ，购买全套 视频讲解 和 参考代码。

### 背景概述

假设你是一家互联网教育公司的员工， 该公司有一个教学系统 `黑羽学院` ，为老师学生提供学习平台。 [点击这里查看黑羽学院详细功能](https://www.byhy.net/tut/others/hylearn/02/)

使用该系统一段时间后， 发现我们还需要一些额外的功能 ，比如：数据批量导入导出、消费数据分析等。

公司领导指定你来开发这个软件，名称为 `黑羽数据管理` 简称 `HYDM`

要求做成一个 MDI 多功能子窗口的 图形界面程序，方便公司内部使用。 界面如下

![image-20221016231747693](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231748330-725860295.png)

下面我们通过分阶段的实战练习，来一步步的开发这个软件。

### 黑羽学院网站系统安装

要开发的 `HYDM` 是用来管理 `黑羽学院` 网站系统 的数据的。

所以要开发，首先得安装好 `黑羽学院` 网站系统。

具体参考过程，[点击这里查看操作步骤和视频讲解](https://www.byhy.net/tut/others/hylearn/01/)

### 实战1 实现登录功能

系统功能需要登录后才能使用。

登录的账号是 `黑羽学院` 里面的管理员账号。 目前`黑羽学院`系统 中已经存在了一个管理员账号 `byhy` ，密码 `sdfsdf` 。

登录时，要使用 `黑羽学院`系统的登录接口， 接口定义[点击此处查看接口文档](https://www.byhy.net/tut/others/hylearn/api/)



该功能实现后，软件界面如下所示：

![image-20221016231810459](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231810839-398402616.png)

点击登录后的主界面可以先只显示一个简单的主窗口即可

[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=2) 观看具体的题目要求



大家先自己做。

做完后， [点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=3) 观看讲解视频

[点击这里](https://cdn2.byhy.net/files/qt/qt-pp-01.zip) 下载参考代码

### 实战2 菜单栏、工具栏、退出功能

本次练习主要是实现主窗口界面的 菜单栏、工具， 并且实现点击 `退出` 菜单，可以退回到登录界面的功能。



该功能实现后，软件界面如下所示：

![image-20221016231830017](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231830380-1760346292.png)

### 实战3 主界面 MDI 子窗口功能	

实现 Qt 加载展现 MDI 多个子窗口的功能。

把 系统参数配置功能做在一个子窗口内，并且实现 配置数据的加载 和 修改实时保存



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=7) 观看具体的题目要求



该功能实现后，软件界面如下所示：

![image-20221016231924495](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016231924914-2042640968.png)

### 实战4 优化 - 同类子窗口单例化

MDI子窗口界面一个常见的问题是，每次双击菜单打开，都会启动一个子窗口， 即使该子窗口已经存在。

请改进代码，实现 如果要打开的子窗口已经存在，不要重复打开，而是把存在的子窗口提升到界面最前面。

[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=8) 观看具体的题目要求

### 实战5 操作菜单树控件

图形界面如果功能稍微多一些，功能菜单都放在菜单栏里面就显得很臃肿。

一种常见的做法是，把子功能的操作项放在一个树状的子菜单区。

这次练习开发一个树状控件 存放在主界面左边的 菜单区。



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=9) 观看具体的题目要求



该功能实现后，软件界面如下所示：

![image-20221016232742360](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016232743047-665563696.png)

## 实战6 Excel导入账号功能

黑羽学院网站可以一个个的添加用户账号。

但是有的客户是学校，会提交学生名单在Excel中。 这时一个个的添加就很麻烦。

请实现： 点击选择 Excel 文件，通过黑羽学院系统的API接口，批量导入的功能。

学生名单Excel文件里面有多个表单，每个表单存储一个班级的学生信息。



[点击这里下载](https://cdn2.byhy.net/files/qt/qt-pp-accounts.xlsx)示例学生名单Excel文件 。



黑羽学院系统的添加账号API接口，[点击这里](https://www.byhy.net/tut/others/hylearn/api/#添加账号)查看接口文档



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=10) 观看具体的题目要求



该功能实现后，软件界面如下所示：

![image-20221016232800242](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016232800807-467033068.png)

## 实战7 导入课程信息到数据库

有些老师的课程录制视频和教程都是本地存储好的。

要上传课程到平台，一个个的添加太麻烦了。

现在要求老师们 按照一定的格式把 课程信息 和内容 存在在目录中。

请实现： 点击选择 课程信息目录，使用SQL客户端库，直接导入数据库中。



[点击这里下载](https://cdn2.byhy.net/files/qt/qt-pp-lessons.zip)要导入的课程信息zip包，然后解压到本地目录。



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=11) 观看具体的题目要求



要导入数据库，请使用 黑羽平台内部开放的 数据库账号： 用户名 `user1` 密码 `sdfsdf`

课程信息涉及到2张表 ： `by_video` 和 `by_lesson` ，表定义格式如下

```sql
CREATE TABLE `by_video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET  NOT NULL,
  `url` varchar(255) CHARACTER SET  NOT NULL,
  `author_id` bigint NOT NULL,
  CONSTRAINT `by_video_author_id_1180705f_fk_by_user_id` FOREIGN KEY (`author_id`) REFERENCES `by_user` (`id`)
) 


CREATE TABLE `by_lesson` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pubdate` datetime(6) NOT NULL,
  `title` varchar(200) CHARACTER SET  NOT NULL,
  `content` longtext CHARACTER SET ,
  `coverimage` varchar(300) CHARACTER SET  DEFAULT NULL,
  `status` smallint unsigned NOT NULL,
  `thumbupcount` int unsigned NOT NULL,
  `favorcount` int unsigned NOT NULL,
  `price` decimal(6,0) NOT NULL,
  `purchasecount` int unsigned NOT NULL,
  `approved` smallint unsigned NOT NULL,
  `reviewcomments` longtext CHARACTER SET ,
  `videos` longtext CHARACTER SET ,
  `usage` smallint unsigned NOT NULL,
  `courses` longtext CHARACTER SET ,
  `author_id` bigint NOT NULL,
  CONSTRAINT `by_lesson_author_id_596d9291_fk_by_user_id` FOREIGN KEY (`author_id`) REFERENCES `by_user` (`id`),
)
```

其中 `by_lesson` 表 的

`status` 表示状态，取值含义为 `1-发布 2-草稿 3-封禁` ，此处固定填写 1 即可。

`approved` 表示批准状态 ，取值含义为 `0-待批准， 1-批准， 2-待修改` ，此处固定填写 1 即可。

`usage` 表示课程是否可以单独出现，还是只能出现在专辑中 `1: 可以单独 0：不可以单独` ，此处固定填写 1 即可。

`videos` 字段，格式是如下的json格式，记录了该课程包含的视频信息

```json
[{"id": 8, "name": "xpath1"}, {"id": 9, "name": "xpath2"}, {"id": 10, "name": "xpath3"}]
```

每个元素表示一个视频，id是视频在 `by_video` 表里面的记录ID ，name是该视频的名字



该功能实现后，软件界面如下所示：

![image-20221016232827890](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016232828514-1053358752.png)

### 实战8 深度优先算法 - 树数据保存加载

本次练习的重点是：图形界面树状控件的数据，如何保存到磁盘文件？ 如何从磁盘文件加载？



黑羽学院系统中的 目录 和 标签 是一个树状的结构。

我们要实现在HYDM界面上创建、修改 目录、标签树的功能， 并且能够把树的信息保存在本地文件中，方便重启软件时，从本地文件加载。

本次练习使用 递归深度优先算法来实现树结构的 保存和读取。



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=12) 观看具体的题目要求



该功能实现后，软件界面如下所示:

![image-20221016232851138](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016232851634-1507218438.png)

### 实战9 广度优先算法 - 树数据导入数据库

本次练习的重点是：图形界面树状控件的数据，如何导入到数据库？



黑羽学院系统中的 目录 和 标签 是存储在MySQL数据库表中的。

我们要实现把 Qt界面上的树结构信息推送到数据。

本次练习使用 循环广度优先算法来实现树结构的 数据库存储。



要导入数据库，请使用 黑羽平台内部开放的 数据库账号： 用户名 `user1` 密码 `sdfsdf`

目录树 和 标签树 分别对应2张表 ： `by_category` 和 `by_tag` ，表定义格式都是一样的，如下：

```sql
CREATE TABLE `by_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) CHARACTER SET  NOT NULL,
  `pid` bigint NOT NULL
)


CREATE TABLE `by_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) CHARACTER SET  NOT NULL,
  `pid` bigint NOT NULL
)
```

其中，每条记录对应一个树节点，每条记录的 `pid` 值就是其父节点的记录ID。

如果该节点是顶层节点，pid值为0



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=13) 观看具体的题目要求

### 实战10 数据分析 曲线图 和 坐标响应

黑羽学院系统中的 课程、专辑购买 记录 存储在MySQL数据库表 `by_purchase_record` 中。

我们要根据购买记录，完成一些数据分析。



本次练习要完成：在指定的 某个时间段，获取和分析每天订单数量和金额 数据，画出曲线图。

并且能做到，当鼠标在曲线图界面上移动时，在图表上方和状态栏 显示当前位置对应当天的日期 和当前的订单数量和金额。



开发之前，我们需要创建一些订单数据。

访问黑羽学院网址 http://网站IP地址/memberop-qt.html

在操作网页上点击按钮 `重置数据库 - 数据分析环境1（需激活）` ，这样就会重置数据库，导入从2019年1月1日到2021年1月1日的大约6万多条订单数据。



MySQL数据库表 `by_purchase_record` ，表格式如下：

```sql
CREATE TABLE `by_purchase_record` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `producttypeid` smallint unsigned NOT NULL,
  `productid` bigint unsigned NOT NULL,
  `quantity` int unsigned NOT NULL,
  `total_fee` decimal(6,0) DEFAULT NULL,
  `paiddatetime` datetime(6) NOT NULL,
  `paymenttype` smallint unsigned DEFAULT NULL,
  `tradeno_hy` varchar(100) CHARACTER SET  DEFAULT NULL,
  `tradeno_paychannel` varchar(100) CHARACTER SET  DEFAULT NULL,
  `user_id` bigint NOT NULL
) 
```

其中 ：

- producttypeid 表示订单购买的产品类型ID

  值为 1 表示 课程，productid 就是课程的ID，对应课程记录 在表 by_lesson 中，

  值为 2 表示 专辑，productid 就是专辑的ID，对应专辑记录 在表 by_course 中，

- total_fee 表示订单金额

- paiddatetime 就是下订单的时间

- paymenttype 是付款方式

  其取值含义如下：

  {1:‘支付宝’,2:‘微信’,3:‘工行卡’,4:‘农行卡’,5:‘招行卡’,6:‘建行卡’,7:‘其它’}

- user_id 表示购买者的ID，对应用户记录在表 by_user 中



[点击这里](https://www.bilibili.com/video/BV19A411H7dS?p=14) 观看具体的题目要求



该功能实现后，软件界面如下所示：

![image-20221016232910491](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016232911155-126364938.png)

### 实战11 数据分析 饼图

本次练习承接上次的练习，要完成：在指定的 某个时间段，获取和分析每种购买渠道的订单量，画出饼图

该功能实现后，软件界面如下所示

![image-20221016233039246](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016233039688-927882757.png)

### 实战12 数据分析 柱状图

本次练习要完成：在指定的 某个时间段，获取前10名购买量最大的课程 和 前10名购买量最大的专辑。

结果分别画在两张柱状图中，并且在每根柱子的下方列出对应哪套课程名称 和 作者姓名，已经购买量。

该功能实现后，软件界面如下所示：

![image-20221016233139111](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016233139822-1687816369.png)

## 项目实战2-测试工具开发

[点击这里，观看项目说明视频讲解](https://www.bilibili.com/video/BV1FR4y147bx?p=1)

我们通过一个项目来锻炼 Python 做测试开发工具的能力。

可以微信咨询 `byhy44` ，购买 参考代码 和 视频讲解 。

### 概述

实战要求开发一款性能测试工具 `黑羽压测Qt版` ，可以用来做 基于HTTP API接口 的性能测试。

要求做成一个 MDI 多功能子窗口的 图形界面程序，方便公司内部使用。 界面如下

![image-20221016233224577](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016233225287-1493380952.png)

本次锻炼涉及的知识点包括：

- Qt图形界面开发的各个要点：

  菜单栏、工具栏、dockwindow、树控件、表格控件、字体图标的使用、MDI 多子窗口、控件动态边界调整、上下文菜单、编辑框文本语法高亮、动态曲线图、matplotlib作图。

- Socket编程

  使用 UDP Socket 来接收 压测进程的统计数据，并且可视化呈现

- 多进程外部程序调用

  启动独立的新压测进程，而不是在图形界面进程中运行压测。



下面我们通过分阶段的实战练习，来一步步的开发这个软件。

## 安装 hyload 库

因为要开发的 性能测试工具 要高效发送 HTTP请求对被测系统进行性能测试，这就必须要有一个高效收发HTTP请求的库。

这里使用白月黑羽自己研发的 hyload 库。

安装非常简单，直接运行 `pip install hyload==0.0.2` 即可。



既然是API接口 压测工具， 就需要一个API服务端 测试你的工具。

可以使用 `http://httpbin.org/uuid` 这个网址进行测试

## 实战1：主窗口界面

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=2) 观看具体的题目要求



实现一个主窗口界面，功能包括

- 构建菜单栏、工具栏

  先实现在 菜单栏、工具栏 `打开项目目录` 功能。

  另外，給主窗口添加产品图标

- 实现日志停靠窗口

  程序各模块可以调用打印日志库函数， 日志窗口显示这些打印信息

  日志窗口可以停靠在主窗口的下面、右侧，也可以单独分离出主窗口。

  设置日志窗口的最大显示行数为1000行。

  超过日志窗口可见范围，要能始终显示最新打印的内容。

- 侧边栏和图标字体

  我们通常会将常用的操作， 放到工具栏上。

  但是有时工具栏上的按钮很多， 其中有些最常用的，往往希望用醒目的大图标单独放置一处。

  上图中，垂直左侧边栏就是一个很好的实现方式。

  其中的图标当然可以自己制作图片，但是比较麻烦。 学过前端开发的朋友知道，有图标字体，比如 `font awesome` ， `Material Icons` ，内置了一套图标，可以直接拿来使用，非常方便。

  如何在 Python Qt 程序中使用这些图标字体呢？

  请大家自己搜索资料实现。

## 实战2：MDI 子窗口功能

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=3) 观看具体的题目要求

先学习 前面教程 `常用控件4` 中， `MDI 多个子窗口` 这一节的内容。

实现 点击侧边栏 中的 各个功能图标， 可以打开一个 MDI 子窗口。

各个子窗口中的具体功能后面再实现。



本次锻炼要做到， 多次点击同一个功能图标，比如 客户端 图标， 只会打开同一个 MDI 子窗口，而不是打开多个客户端子窗口。

## 实战3：API客户端1

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=4) 观看具体的题目要求

API 客户端是实现 可以编辑代码构建各种格式的HTTP请求 ，发送给被测服务端。

该功能实现后， 其实就是一个API接口测试的工具，类似 Postman这些工具。



本次练习先实现 左侧客户端代码文件管理框。

默认的客户端代码文件 放置在项目根目录下面的 client 目录中，

包括

- 显示client 目录中所有的代码文件， 为示例界面中的一个条目

- 可以对代码文件条目进行 增、删、改名

  点击工具栏增加条目图标，可以添加一个代码文件

  右键点击一个条目，显示

  双击节点，可以改变其文件名

  注意： 增、删、改名文件时， 标题栏显示内容对应的改变

- 代码目录刷新

## 实战4：API客户端2

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=5) 观看具体的题目要求

本次练习实现具体的 HTTP API 接口测试 代码编辑、执行功能。

当然第一反应，是应该使用 流行的 `Requests` 库 来 构建和 收发 HTTP消息。

但是 Requests 库不适合做性能测试， 它的性能很差，所以这里我们使用 白月黑羽自己研发的hyload库。

该库的使用详情，请参考[这个文档](https://www.byhy.net/tut/others/loadtest/interface/)



本次练习要实现的功能包括：

- 子窗口界面组成

  包括3个部分： 左侧文件浏览器框、中间代码编辑框、右侧代码助手框

  3个部分的大小可以拖到边界调整

- 代码助手功能

  实现 点击 右侧代码助手框里面的条目 后， 代码自动填充。

  最好是，可以根据 配置项 动态实现。

  条目和对应插入代码关系如下所示

```py
codeSnippets = [

        {
            'name': '创建 HTTP 客户端',
            'code': '''# 创建客户端
client = HttpClient('127.0.0.1', # 目标地址:端口
                    timeout=10   # 超时时间，单位秒
                   ) 
'''
        },

        {
            'name': '创建 HTTPS 客户端',
            'code': '''# 创建客户端
client = HttpsClient('127.0.0.1', # 目标地址:端口
                     timeout=10   # 超时时间，单位秒
                       ) 
'''
        },

        {
            'name': '使用代理',
            'code': '''client.proxy('127.0.0.1:8888')
'''
        },

       
        'separator',

        {
            'name': '发送 简单请求',
            'code': '''# 请求方法对应HTTP方法，包括：get、post、put、delete 等
response = client.get(
    '/api/path1'  # 请求URL
    )
'''
        },

        {
            'name': '设置 url参数',
            'code': '''response = client.get(
    '/api/path1', 
    # 通过params传入url参数
    params={
        'param1':'value1',
        'param2':'value2'
    }
    )
'''
        },

        {
            'name': '设置 消息头',
            'code': '''response = client.get(
    '/api/path1',
    # 通过headers传入指定消息头
    headers={
        'header1':'value1',
        'header2':'value2'
    })
'''
        },

        {
            'name': '设置 消息体，urlencode 格式',
            'code': '''response = client.post(
    '/api/path1',
    # 通过data传入指定urlencode格式的消息体参数
    data={
        'param1':'value1',
        'param2':'value2'
    })
'''
        },

        {
            'name': '设置 消息体，json 格式',
            'code': '''response = client.post(
    '/api/path1',
    # 通过json传入指定json格式的消息体参数
    json={
        'param1':'value1',
        'param2':'value2'
    })
'''
        },

        {
            'name': '设置 消息体，直接写入 字节',
            'code': """response = client.post(
    '/api/path1',
    headers={
        'Content-Type':'application/xml'
    }
    # 下面填写bytes的内容，注意最后的编码格式
    data='''
    <?xml version="1.0" encoding="UTF-8"?>
    <CreateBucketConfiguration>
        <StorageClass>Standard</StorageClass>
    </CreateBucketConfiguration>
    '''.encode('utf8')
    )
"""
        },

        {
            'name': '循环发10个请求',
            'code': '''for i in range(10): 
    response = client.get('/api/path1')
    sleep(5) # 间隔5秒
'''
        },

        'separator',

        {
            'name': '查看 响应时长',
            'code': '''print(f"响应时长为 {response.responseTime} ms")
'''
        },

        {
            'name': '查看 响应状态码',
            'code': '''print(f"响应状态码为 {response.status_code} ") 
'''
        },

        {
            'name': '查看 消息体 文本内容',
            'code': '''print(f"消息体字符串为 {response.text()} ") 
'''
        },

        {
            'name': '查看 消息体 原始内容',
            'code': '''print(f"消息体字节串为 {response.raw} ") 
'''
        },

        {
            'name': '查看 消息体 json格式',
            'code': '''pprint(response.json())
'''
        },

        {
            'name': '查看 消息头',
            'code': '''# 获取消息头Content-Type值
ct = response.headers['Content-Type']    
print(f"消息头Content-Type值为 {ct} ") 
'''
        },

        {
            'name': '报告一个错误',
            'code': '''      
Stats.oneError()  # 报告一个错误，加入到统计信息中 
TestLogger.write('这里写详细信息到测试日志中，方便定位问题')        
'''
        },

        {
            'name': '测试日志添加信息',
            'code': '''TestLogger.write('这里写日志信息')
'''
        },

        'separator',

        {
            'name': '等待10秒',
            'code': '''sleep(10)
'''
        },
    ]
```

- 点击其中一个文件条目，就加载该文件内容到代码编辑框中

  标题栏显示当前编辑文件的名字

  编辑过程中，点击保存按钮，可以保存编辑框内容到当前编辑文件中。

  切换代码文件时，如果当前文件正在编辑，请自动保存后，再切换到新文件。

- 代码编辑框中Python代码语法高亮显示

  请大家自己网上搜索相应资料实现

- 点击运行按钮，启动新进程，执行代码

  注意：点击运行按钮，如果该文件没有保存，要自动保存。

  然后获取编辑框的代码，并且在前面添加如下这几行代码，存入压测项目根目录的一个文件 run.py 。

  然后额外启动一个新的python进程，运行这个run.py 文件。

  为什么要额外启动新进程，而不是就在当前程序中运行该代码文件呢？可以自己思考一下。

```py
import time
from pprint import pprint
from time import sleep
from hyload.httpclient import HttpsClient,HttpClient
from hyload.logger import TestLogger
from hyload.stats import Stats
# 此参数只有被性能场景调用时才会传入
arg = None
```

## 实战5：性能场景定义

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=6) 观看具体的题目要求。

黑羽压测工具的性能测试，就是先定义客户端行为，模拟单独的用户。

然后定义 性能场景， 就是 写代码 指定启动 n个 前面定义好的客户端， 从而模拟大量用户使用系统的场景。



本次练习就是实现 定义性能场景的代码。

界面组成和功能和 前面定义客户端类似， 只是代码助手的条目内容不同，最终执行时产生的代码文件和执行命令参数不同。



代码助手条目如下

```py
cmds_zh = [

        {
            'name': '启动3个客户端',
            'code': '''createClients(
    'client_1', # 客户端名称
    3,       # 客户端数量
    0.1,     # 启动间隔时间，秒
    )
'''
        },

        {
            'name': '启动3个客户端，反复执行',
            'code': '''createClientsAndKeep(
    'client_1', # 客户端名称
    3,       # 客户端数量
    0.1,     # 启动间隔时间，秒
    )
'''
        },

        {
            'name': '启动3个带参数客户端',
            'code': '''# 定义每个客户端对应的参数
args = ['user1','user2','user3']

createClients(
    'client_1', # 客户端名称
    3,       # 客户端数量    
    1,       # 启动间隔时间，秒
    args # 客户端参数
    )
'''
        },

        {
            'name': '启动3个带参数客户端，反复执行',
            'code': '''# 定义每个客户端对应的参数
args = ['user1','user2','user3']

createClientsAndKeep(
    'client_1', # 客户端名称
    3,       # 客户端数量    
    1,       # 启动间隔时间，秒
    args # 客户端参数
    )
'''
        },

        {
            'name': '等待10秒',
            'code': '''
sleep(10)
    '''
        },
    ]
```



点击运行按钮后，程序要做如下处理

1. 先创建如下这些行代码，作为前缀部分

```py
from gevent import monkey
monkey.patch_all()

from gevent import spawn
import gevent

import time
from pprint import pprint
from time import sleep

from hyload.stats import Stats
from hyload.logger import TestLogger

from hyload.httpclient import HttpsClient,HttpClient

clientName2Func = {}

# 如果 args 有值，一定是列表，元素依次赋值给每次clientfunc调用
def createClients(clientName, clientNum, interval, args=None):
    clientFunc = clientName2Func[clientName]
    for i in range(clientNum):
        if args:
            spawn(clientFunc, args[i])
        else:
            spawn(clientFunc)

        if i < clientNum - 1:
            sleep(interval)

# 如果 args 有值，一定是列表，元素依次赋值给每次clientfunc调用
def createClientsAndKeep(clientName, clientNum, interval, args=None):
    clientFunc = clientName2Func[clientName]
    
    def realFunc(args=None):
        while True:
            try:
                clientFunc(args)
            except Exception as e:
                print(e)
            
    for i in range(clientNum):
        if args:
            spawn(realFunc, args[i])
        else:
            spawn(realFunc)

        if i < clientNum - 1:
            sleep(interval)

Stats.start()

################## write your code  * begin * ###################
```



1. 分析编辑框获取的代码， 将性能场景定义中所有的 `createClients` 里面的客户端定义代码找到。

比如， 这样的 代码

```py
createClients(
    'client_1', # 客户端名称
    3,       # 客户端数量
    0.1,     # 启动间隔时间，秒
    )

sleep(2)
    
createClients(
    'client_2', # 客户端名称
    3,       # 客户端数量
    0.1,     # 启动间隔时间，秒
    )
```

里面就涉及到两个客户端定义， `client_1` 和 `client_2` 。

需要你的程序找到对应的代码文件，读入其内容后，放置到如下的函数定义中

```py
def client_1(arg=None):
    # 这里写入 client_1 的 文件内容，并且产生缩进
 

def client_2(arg=None):
    # 这里写入 client_2 的 文件内容，并且产生缩进

# 最后再加上如下的定义关系
clientName2Func['client_1'] = client_1
clientName2Func['client_2'] = client_2
```

把上面的代码添加到步骤1后产生的代码后面，

后面再加上性能测试场景定义里面的代码



1. 在步骤2产生的代码 后面添加如下代码

```py
################## write your code * end * ###################

gevent.wait()
```



然后，存入压测项目根目录下的文件 run.py 中 。

再额外启动一个新的 Python进程，运行这个run.py 文件。

## 实战6：Socket编程 统计数据的接收

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=7) 观看具体的题目要求。

运行前面开发的性能测试run.py时，

如果提供了命令行参数 `console` 指定IP地址和端口，格式如下

```py
console=127.0.0.1:18444
```

启动的 压力测试进程 就会将每秒的统计信息 序列化为json格式，并且以 UDP 数据报 发送到 指定的地址和端口。

上面的示例中，就会发送到 127.0.0.1 本地地址，18444 UDP端口上。



接收到的字节串解码为字符串的内容如下所示

```json
{"t": 1637842350, "rps": 1, "tops": 0, "eps": 0, "tps": 0, "respTimeSum": 0, "avgRespTime": 0, "total": {"send": 1, "recv": 0}}
{"t": 1637842351, "rps": 0, "tops": 0, "eps": 0, "tps": 1, "respTimeSum": 0.4268, "avgRespTime": 0.4268, "total": {"send": 1, "recv": 1, "100-500ms": 1}}
{"t": 1637842352, "rps": 1, "tops": 0, "eps": 0, "tps": 1, "respTimeSum": 0.3913, "avgRespTime": 0.3913, "total": {"send": 2, "recv": 2, "100-500ms": 2}}
{"t": 1637842353, "rps": 1, "tops": 0, "eps": 0, "tps": 1, "respTimeSum": 0.2225, "avgRespTime": 0.2225, "total": {"send": 3, "recv": 3, "100-500ms": 3}}
```



每行代表一次发送的消息，具体含义目前不需要知道，后续练习会有讲解



这次任务，就是 实现UDP Socket 接受 `压力测试进程` 的统计数据，并且滚屏显示在日志框中。

当然，要实现：在前面已经实现的启动压力测试进程的 命令行 中 加上 `console=<IP>:<Port>` 参数。

注意：要确保使用的端口号没有被占用，如果被占用，应该找到并使用 一个没有占用的端口号。



关于 UDP Socket 编程，可以学习[这里的教程](https://www.byhy.net/tut/py/etc/socket/#udp-socket-编程)

## 实战7：实时监控 - 动态表格

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=8) 观看具体的题目要求。



`压力测试进程` 发送的统计数据是json格式，

各字段的含义如下

```py
{
  "t": 1636532998,       # 时间戳，1970年距离数字格式
  "rps": 24,             # 该秒发送请求数量
  "tps": 24,             # 该秒接收响应数量
  "tops": 0,             # 该秒超时数量
  "eps": 0,              # 该秒错误数量
  "respTimeSum": 5.7846, # 该秒累计响应时长，方便多个worker时统计
  "avgRespTime": 0.2083  # 该秒平均响应时长
  "total": {
    "send": 7981,        # 累计请求数量
    "recv": 7965,        # 累计响应数量
    "timeout": 11,       # 累计超时数量，如果为0 则该字段不存在
    "error": 1,          # 累计超时数量，如果为0 则该字段不存在
    "100-500ms": 7820,   # 响应时长在 100-500ms   之间的请求数量
    "500-1000ms": 141,   # 响应时长在 500-1000ms  之间的请求数量
    "1000-3000ms": 4     # 响应时长在 1000-3000ms 之间的请求数量
  }
}
```

具体说明，参考视频里面的讲解



本次练习要实现实时统计子窗口界面的**表格部分**。

表格展示 最近10秒统计数据，实现动态刷新，如下图所示

![image-20221016233304410](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016233304871-879747129.png)

## 实战8：实时监控 - 曲线图

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=9) 观看具体的题目要求。

实现监控统计界面里面两种图表的作图：请求响应实时曲线图 和 响应时长曲线图

其中：请求响应实时曲线图 实时展示最近10次 每秒RPS 和 TPS 两个曲线，X轴坐标单位是 时间几分几秒，Y轴坐标单位是个

响应时长曲线图 展示最近10次 每秒平均响应时长 曲线，X轴坐标单位是 时间几分几秒，Y轴坐标单位是秒

## 实战9：性能统计数据matplotlib作图

[点击这里](https://www.bilibili.com/video/BV1FR4y147bx?p=10) 观看具体的题目要求。

如果压力进程的启动命令中有 `statsfile` 参数，压力进程执行过程中，就会把统计数据写入到改参数指定的文件中。

比如

```
c:\python38\python.exe run.py console=127.0.0.1:18444 statsfile=D:/t1/loadtest2/stats_perf/20211128-101224.sts
```



本次练习，需要实现统计记录数据作图功能。

- 先在性能场景脚本运行命令行中，添加 statsfile 参数，其值为 当前项目目录的 stats_perf 子目录 里面的文件。文件名为当前日期时间，扩展名为sts。
- 然后在工具栏添加一个作图按钮，点击该按钮，可以让用户选择统计数据文件（可以多选）， 然后使用 matplotlib 库对这些文件中的统计数据作图，如下所示

![image-20221016233322873](https://img2022.cnblogs.com/blog/2056203/202210/2056203-20221016233323435-1564031152.png)

其中 ：

- 第1张图显示 rps （每秒请求数量）
- 第2张图显示 tps （每秒响应数量，蓝色）、eps（每秒错误数量，红点）、tops（每秒超时数量，绿点）
- 第3张图显示 lps （平均每秒响应时间）