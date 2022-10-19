# 导入需要的包
from PyQt5.Qt import *
import sys

# 创建一个应用程序
app = QApplication(sys.argv)

# 控件操作
window = QWidget()
window.setWindowTitle("XX管理系统")
window.resize(500, 500)
window.move(400, 200)

label  = QLabel(window)
label.setText("Hello Qt!")
label.move(200, 200)

window.show()

# 开始执行应用程序，并进入消息循环
sys.exit(app.exec_())