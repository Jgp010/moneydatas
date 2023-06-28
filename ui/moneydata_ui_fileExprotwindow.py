# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moneydata_ui_fileExprotwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(297, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(9, 9, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lbl_path = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_path.sizePolicy().hasHeightForWidth())
        self.lbl_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_path.setFont(font)
        self.lbl_path.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_path.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_path.setText("")
        self.lbl_path.setObjectName("lbl_path")
        self.horizontalLayout.addWidget(self.lbl_path)
        self.btn_path = QtWidgets.QPushButton(self.frame)
        self.btn_path.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_path.setFont(font)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.led_name = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.led_name.setFont(font)
        self.led_name.setAlignment(QtCore.Qt.AlignCenter)
        self.led_name.setObjectName("led_name")
        self.horizontalLayout_4.addWidget(self.led_name)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cmb_fileType = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_fileType.sizePolicy().hasHeightForWidth())
        self.cmb_fileType.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cmb_fileType.setFont(font)
        self.cmb_fileType.setObjectName("cmb_fileType")
        self.cmb_fileType.addItem("")
        self.cmb_fileType.addItem("")
        self.cmb_fileType.addItem("")
        self.horizontalLayout_2.addWidget(self.cmb_fileType)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_backDefaultValue = QtWidgets.QPushButton(self.frame_2)
        self.btn_backDefaultValue.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_backDefaultValue.setFont(font)
        self.btn_backDefaultValue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_backDefaultValue.setObjectName("btn_backDefaultValue")
        self.horizontalLayout_3.addWidget(self.btn_backDefaultValue)
        self.btn_exportFile = QtWidgets.QPushButton(self.frame_2)
        self.btn_exportFile.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exportFile.setFont(font)
        self.btn_exportFile.setObjectName("btn_exportFile")
        self.horizontalLayout_3.addWidget(self.btn_exportFile)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_cancel = QtWidgets.QPushButton(self.frame_7)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_6.addWidget(self.btn_cancel)
        self.btn_ok = QtWidgets.QPushButton(self.frame_7)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_6.addWidget(self.btn_ok)
        self.verticalLayout.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "匯出檔案"))
        self.label.setText(_translate("MainWindow", "路徑:"))
        self.btn_path.setText(_translate("MainWindow", "選擇路徑"))
        self.label_2.setText(_translate("MainWindow", "檔案名稱:"))
        self.led_name.setText(_translate("MainWindow", "記帳系統匯出檔"))
        self.label_3.setText(_translate("MainWindow", "匯出檔案類型:"))
        self.cmb_fileType.setItemText(0, _translate("MainWindow", "csv"))
        self.cmb_fileType.setItemText(1, _translate("MainWindow", "json"))
        self.cmb_fileType.setItemText(2, _translate("MainWindow", "execl"))
        self.btn_backDefaultValue.setText(_translate("MainWindow", "恢復預設值"))
        self.btn_exportFile.setText(_translate("MainWindow", "匯出檔案"))
        self.btn_cancel.setText(_translate("MainWindow", "取消"))
        self.btn_ok.setText(_translate("MainWindow", "確認"))