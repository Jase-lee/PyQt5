"""
1、全选并复制下面的代码作为模板代码
2、按 Ctrl + Alt + S 快捷键打开设置
3、搜索框输入 live 找到 Live Templates
4、找到 Python,点击右侧的 + 号，选择 live template
5、
Abbreviation：填你想使用的快捷单词，比如你输入了这个单词就迅速生成这个模板，在此我写的是 qtt
Description：描述你这个模板是干嘛用的
Template Text: 把第1步复制的模板代码粘贴进去，并在 window.setWindowTitle("$TITLE$") 加一个 $TITLE$，当生成
代码时，光标会自动定位到 $TITLE$ 的位置，接着在 window.resize(500, 500) 行的下面加 $CODE$，当输入完 TITLE后，
按回车就自动跳到 $CODE$ 的位置了

6、下方的 define 选择 python，然后点 apply 再点 ok
"""

# 导入需要的包
from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1  创建控件
window = QWidget()

# 2.2设置控件
window.setWindowTitle("")
window.resize(500, 500)


# 2.3  展示控件
window.show()

# 开始执行应用程序，并进入消息循环
sys.exit(app.exec_())