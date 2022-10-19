"""
02-02 我们已经设置了代码模板，现在在下面输入qtt并按tab键就可以生成我们设置的代码模板了
"""
# 导入需要的包
from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.1  创建控件
window = QWidget()

# 2.2设置控件
window.setWindowTitle("XxxManageSystem")
window.resize(500, 500)

label = QLabel(window)
label.setText("Hello World!")
label.resize(300,300)
label.move(100,250)


# 2.3  展示控件
window.show()

# 开始执行应用程序，并进入消息循环
sys.exit(app.exec_())