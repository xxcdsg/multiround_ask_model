# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # 第一行：输入 api_key
        self.horizontalLayout_apiKey = QtWidgets.QHBoxLayout()
        self.horizontalLayout_apiKey.setObjectName("horizontalLayout_apiKey")
        self.label_apiKey = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_apiKey.setFont(font)
        self.label_apiKey.setObjectName("label_apiKey")
        self.horizontalLayout_apiKey.addWidget(self.label_apiKey)
        self.lineEdit_apiKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_apiKey.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_apiKey.setObjectName("lineEdit_apiKey")
        self.horizontalLayout_apiKey.addWidget(self.lineEdit_apiKey)
        self.gridLayout.addLayout(self.horizontalLayout_apiKey, 0, 0, 1, 5)

        # 第二行：输入 key_word
        self.horizontalLayout_keyWord = QtWidgets.QHBoxLayout()
        self.horizontalLayout_keyWord.setObjectName("horizontalLayout_keyWord")
        self.label_keyWord = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_keyWord.setFont(font)
        self.label_keyWord.setObjectName("label_keyWord")
        self.horizontalLayout_keyWord.addWidget(self.label_keyWord)
        self.lineEdit_keyWord = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_keyWord.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_keyWord.setObjectName("lineEdit_keyWord")
        self.horizontalLayout_keyWord.addWidget(self.lineEdit_keyWord)
        self.gridLayout.addLayout(self.horizontalLayout_keyWord, 1, 0, 1, 5)

        # 第三行：输入 words
        self.horizontalLayout_words = QtWidgets.QHBoxLayout()
        self.horizontalLayout_words.setObjectName("horizontalLayout_words")
        self.label_words = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_words.setFont(font)
        self.label_words.setObjectName("label_words")
        self.horizontalLayout_words.addWidget(self.label_words)
        self.lineEdit_words = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_words.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_words.setObjectName("lineEdit_words")
        self.horizontalLayout_words.addWidget(self.lineEdit_words)
        self.gridLayout.addLayout(self.horizontalLayout_words, 2, 0, 1, 5)

        # 第四行：线程数
        self.horizontalLayout_thread = QtWidgets.QHBoxLayout()
        self.horizontalLayout_thread.setObjectName("horizontalLayout_thread")
        self.label_thread = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_thread.setFont(font)
        self.label_thread.setObjectName("label_thread")
        self.horizontalLayout_thread.addWidget(self.label_thread)
        self.spinBox_thread = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_thread.setMinimum(1)
        self.spinBox_thread.setProperty("value", 5)
        self.spinBox_thread.setObjectName("spinBox_thread")
        self.horizontalLayout_thread.addWidget(self.spinBox_thread)
        self.gridLayout.addLayout(self.horizontalLayout_thread, 3, 0, 1, 5)

        # 第五行：模型选择
        self.groupBox_model = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_model.setObjectName("groupBox_model")
        self.horizontalLayout_model = QtWidgets.QHBoxLayout(self.groupBox_model)

        self.radio_chat = QtWidgets.QRadioButton(self.groupBox_model)
        self.radio_chat.setChecked(True)  # 默认选中chat模型
        self.radio_chat.setObjectName("radio_chat")
        self.horizontalLayout_model.addWidget(self.radio_chat)

        self.radio_reason = QtWidgets.QRadioButton(self.groupBox_model)
        self.radio_reason.setObjectName("radio_reason")
        self.horizontalLayout_model.addWidget(self.radio_reason)

        self.gridLayout.addWidget(self.groupBox_model, 4, 0, 1, 5)  # 插入到第4行

        # 第六行：按钮
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_buttons.addWidget(self.pushButton_start)

        self.pushButton_openDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openDir.setObjectName("pushButton_openDir")
        self.horizontalLayout_buttons.addWidget(self.pushButton_openDir)

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_buttons.addWidget(self.pushButton_exit)

        self.gridLayout.addLayout(self.horizontalLayout_buttons, 5, 0, 1, 5)

        # 信息显示框

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 6, 0, 1, 5)

        # 中央窗口部件设置
        MainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏和状态栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "多线程大模型询问工具"))
        self.label_apiKey.setText(_translate("MainWindow", "输入 api_key"))
        self.label_keyWord.setText(_translate("MainWindow", "输入 key_word"))
        self.label_words.setText(_translate("MainWindow", "输入 words"))
        self.label_thread.setText(_translate("MainWindow", "调节线程数"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_openDir.setText(_translate("MainWindow", "打开下载目录"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出"))
        self.groupBox_model.setTitle(_translate("MainWindow", "模型选择"))
        self.radio_chat.setText(_translate("MainWindow", "deepseek-chat"))
        self.radio_reason.setText(_translate("MainWindow", "deepseek-reasoner"))

