import traceback

import requests
import os
import re
from threading import Thread
from queue import Queue
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import sys

from qt.layout import Ui_MainWindow as UIM
from BackendThread import BackendThread

# sk-49601e55aef94eb191cb0340a2689ba1

class UIM_Version(UIM, QtWidgets.QWidget):
    send_args = pyqtSignal(str, int)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)  # 因为继承关系，要对父类初始化

    def setFunction(self):
        self.pushButton_openDir.clicked.connect(self.openDir)
        self.pushButton_start.clicked.connect(self.send)
        self.pushButton_exit.clicked.connect(self.close_window)

    def openDir(self):
        path = os.getcwd()
        try:
            os.system(r'C:\Windows\explorer.exe "%s"' % path)
        except Exception as e:
            print(e)

    def close_window(self):
        qApp = QtWidgets.QApplication.instance()
        qApp.quit()

    def msg(self, title, msg):
        QtWidgets.QMessageBox.information(self, title, msg, QtWidgets.QMessageBox.Yes)

    def console_append(self,text):
        self.textBrowser.append(text)
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def send(self):

        # 获取参数
        api = self.lineEdit_apiKey.text()
        word = self.lineEdit_keyWord.text()
        words_string = self.lineEdit_words.text()
        selected_text = ""
        for radio in [self.radio_chat,self.radio_reason]:
            if radio.isChecked():
                selected_text = radio.text()
        words = [word.strip() for word in words_string.split(',')]
        thread_num = int(self.spinBox_thread.text())


        self.backend = BackendThread(api,word,words,thread_num,selected_text)  # 初始化线程类
        self.backend.update_data.connect(self.console_append)  # 连接线程类的输出与窗体的输出

        self.backend.start()  # 线程类启动

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) # 启用高DPI缩放支持
    app = QtWidgets.QApplication(sys.argv) # 创建一个GUI应用程序实例
    MainWindow = QtWidgets.QMainWindow() # 创建窗口
    ui = UIM_Version() # 创建样式
    ui.setupUi(MainWindow)
    ui.setFunction()
    # ui.handleDisplay("如果你不知道该如何使用本软件，请点击“使用说明”按钮查看帮助")
    MainWindow.show() # 使窗口可见
    sys.exit(app.exec_()) # 进入事件循环，直到应用程序退出