# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moneydata_ui_selectlwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.led_id = QtWidgets.QLineEdit(self.frame_5)
        self.led_id.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_id.sizePolicy().hasHeightForWidth())
        self.led_id.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.led_id.setFont(font)
        self.led_id.setObjectName("led_id")
        self.horizontalLayout_2.addWidget(self.led_id)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_id_load = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_id_load.sizePolicy().hasHeightForWidth())
        self.btn_id_load.setSizePolicy(sizePolicy)
        self.btn_id_load.setObjectName("btn_id_load")
        self.horizontalLayout_3.addWidget(self.btn_id_load)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cmb_year = QtWidgets.QComboBox(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_year.sizePolicy().hasHeightForWidth())
        self.cmb_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_year.setFont(font)
        self.cmb_year.setObjectName("cmb_year")
        self.horizontalLayout_8.addWidget(self.cmb_year)
        self.label_23 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        self.cmb_month = QtWidgets.QComboBox(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_month.sizePolicy().hasHeightForWidth())
        self.cmb_month.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_month.setFont(font)
        self.cmb_month.setObjectName("cmb_month")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.cmb_month.addItem("")
        self.horizontalLayout_8.addWidget(self.cmb_month)
        self.label_24 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_8.addWidget(self.label_24)
        self.cmb_day = QtWidgets.QComboBox(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_day.sizePolicy().hasHeightForWidth())
        self.cmb_day.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmb_day.setFont(font)
        self.cmb_day.setObjectName("cmb_day")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.cmb_day.addItem("")
        self.horizontalLayout_8.addWidget(self.cmb_day)
        self.label_25 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_8.addWidget(self.label_25)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.cmb_type = QtWidgets.QComboBox(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_type.sizePolicy().hasHeightForWidth())
        self.cmb_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cmb_type.setFont(font)
        self.cmb_type.setObjectName("cmb_type")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.horizontalLayout_10.addWidget(self.cmb_type)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.led_money = QtWidgets.QLineEdit(self.frame_13)
        self.led_money.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_money.sizePolicy().hasHeightForWidth())
        self.led_money.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.led_money.setFont(font)
        self.led_money.setObjectName("led_money")
        self.horizontalLayout_9.addWidget(self.led_money)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_16 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.led_note = QtWidgets.QLineEdit(self.frame_16)
        self.led_note.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_note.sizePolicy().hasHeightForWidth())
        self.led_note.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.led_note.setFont(font)
        self.led_note.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.led_note.setObjectName("led_note")
        self.horizontalLayout_12.addWidget(self.led_note)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_15 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_load = QtWidgets.QPushButton(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load.sizePolicy().hasHeightForWidth())
        self.btn_load.setSizePolicy(sizePolicy)
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout_11.addWidget(self.btn_load)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "使用id進行精準搜尋"))
        self.label_2.setText(_translate("MainWindow", "輸入要找尋的資料id:"))
        self.btn_id_load.setText(_translate("MainWindow", "開始讀取"))
        self.label_5.setText(_translate("MainWindow", "通過以下資訊進行搜尋"))
        self.label_23.setText(_translate("MainWindow", "年"))
        self.cmb_month.setItemText(0, _translate("MainWindow", "無"))
        self.cmb_month.setItemText(1, _translate("MainWindow", "01"))
        self.cmb_month.setItemText(2, _translate("MainWindow", "02"))
        self.cmb_month.setItemText(3, _translate("MainWindow", "03"))
        self.cmb_month.setItemText(4, _translate("MainWindow", "04"))
        self.cmb_month.setItemText(5, _translate("MainWindow", "05"))
        self.cmb_month.setItemText(6, _translate("MainWindow", "06"))
        self.cmb_month.setItemText(7, _translate("MainWindow", "07"))
        self.cmb_month.setItemText(8, _translate("MainWindow", "08"))
        self.cmb_month.setItemText(9, _translate("MainWindow", "09"))
        self.cmb_month.setItemText(10, _translate("MainWindow", "10"))
        self.cmb_month.setItemText(11, _translate("MainWindow", "11"))
        self.cmb_month.setItemText(12, _translate("MainWindow", "12"))
        self.label_24.setText(_translate("MainWindow", "月"))
        self.cmb_day.setItemText(0, _translate("MainWindow", "無"))
        self.cmb_day.setItemText(1, _translate("MainWindow", "01"))
        self.cmb_day.setItemText(2, _translate("MainWindow", "02"))
        self.cmb_day.setItemText(3, _translate("MainWindow", "03"))
        self.cmb_day.setItemText(4, _translate("MainWindow", "04"))
        self.cmb_day.setItemText(5, _translate("MainWindow", "05"))
        self.cmb_day.setItemText(6, _translate("MainWindow", "06"))
        self.cmb_day.setItemText(7, _translate("MainWindow", "07"))
        self.cmb_day.setItemText(8, _translate("MainWindow", "08"))
        self.cmb_day.setItemText(9, _translate("MainWindow", "09"))
        self.cmb_day.setItemText(10, _translate("MainWindow", "10"))
        self.cmb_day.setItemText(11, _translate("MainWindow", "11"))
        self.cmb_day.setItemText(12, _translate("MainWindow", "12"))
        self.cmb_day.setItemText(13, _translate("MainWindow", "13"))
        self.cmb_day.setItemText(14, _translate("MainWindow", "14"))
        self.cmb_day.setItemText(15, _translate("MainWindow", "15"))
        self.cmb_day.setItemText(16, _translate("MainWindow", "16"))
        self.cmb_day.setItemText(17, _translate("MainWindow", "17"))
        self.cmb_day.setItemText(18, _translate("MainWindow", "18"))
        self.cmb_day.setItemText(19, _translate("MainWindow", "19"))
        self.cmb_day.setItemText(20, _translate("MainWindow", "20"))
        self.cmb_day.setItemText(21, _translate("MainWindow", "21"))
        self.cmb_day.setItemText(22, _translate("MainWindow", "22"))
        self.cmb_day.setItemText(23, _translate("MainWindow", "23"))
        self.cmb_day.setItemText(24, _translate("MainWindow", "24"))
        self.cmb_day.setItemText(25, _translate("MainWindow", "25"))
        self.cmb_day.setItemText(26, _translate("MainWindow", "26"))
        self.cmb_day.setItemText(27, _translate("MainWindow", "27"))
        self.cmb_day.setItemText(28, _translate("MainWindow", "28"))
        self.cmb_day.setItemText(29, _translate("MainWindow", "29"))
        self.cmb_day.setItemText(30, _translate("MainWindow", "30"))
        self.cmb_day.setItemText(31, _translate("MainWindow", "31"))
        self.label_25.setText(_translate("MainWindow", "日"))
        self.label_8.setText(_translate("MainWindow", "類型:"))
        self.cmb_type.setItemText(0, _translate("MainWindow", "收入"))
        self.cmb_type.setItemText(1, _translate("MainWindow", "支出"))
        self.label_7.setText(_translate("MainWindow", "金額:"))
        self.label_6.setText(_translate("MainWindow", "備註:"))
        self.btn_load.setText(_translate("MainWindow", "開始讀取"))
