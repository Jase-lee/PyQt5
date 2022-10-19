"""
使用PyQt5做一个小案例，需求如下：
1）展示一个 500 * 500 的窗口
2）设置窗口标题为 "XXX管理系统"
3）添加子控件（标签控件），并显示 "Hello World"
"""

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

