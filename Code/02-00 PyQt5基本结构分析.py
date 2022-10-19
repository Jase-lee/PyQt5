# 导入需要的包
from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

# print(app.arguments())
# print(qApp.arguments())

# 2.1  创建控件
window = QWidget()
window.setWindowTitle("XX管理系统")
window.resize(500, 500)
window.move(400, 200)

# 如果控件没有顶层窗口，默认情况下不显示，只有手动设置才显示
# label= QLabel()
# label.setText("xxx")
# label.show()

# 加了顶层窗口，随着顶层窗口一起显示
label  = QLabel(window)
label.setText("Hello Qt!")
label.move(200, 200)

# 2.3  展示控件
window.show()

# 开始执行应用程序，并进入消息循环
# 让整个程序开始执行，并且进入消息循环（无限循环）
# 检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())