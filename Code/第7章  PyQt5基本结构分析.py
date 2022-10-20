from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

"""
2、控件的操作
创建控件，设置控件（大小、位置、样式...），事件，信号处理
"""
# 2.1创建控件
# 当我们创建一个控件之后，如果这个控件没有父控件，则把它当做顶层控件（窗口）
# 系统会自动的给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题，图标）
window = QWidget()
window.setWindowTitle("XXX管理系统")
window.resize(500, 500)
window.move(200, 200)

# 创建一个子控件
label = QLabel(window)
label.setText("Hello World")
label.resize(100,100)
label.move(200, 200)
# label.show()

# 2.3展示控件
# 刚创建的控件（这个控件没有父控件），默认情况下不会展示，只有手动的调用 show() 才可以
window.show()
sys.exit(app.exec_())
