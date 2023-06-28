# -*- coding:utf-8 -*-
from ui.moneydata_ui_fileExprotwindow import *
import pandas as  pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QFileDialog
from ppp import P
import sys
from Ms import MessageBox
import os


class FileWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #設定按鈕功能
        self.btn_path.clicked.connect(self.file_path)
        self.btn_ok.clicked.connect(lambda :P.ok(self,"確定要離開?",'通知'))
        self.btn_cancel.clicked.connect(lambda :P.exit(self))
        self.btn_backDefaultValue.clicked.connect(self.backDefaultValue)
        self.btn_exportFile.clicked.connect(self.exportFile)
        #預設路徑
        self.path="c:\\moneydatas"
        self.lbl_path.setText(self.path)
        self.data=None
        #建立路徑
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    #選擇路徑
    def file_path(self):
        path=QFileDialog.getExistingDirectory()
        if self.path != '':
            self.path=path
            self.lbl_path.setText(path)
    #回到預設
    def backDefaultValue(self):
        self.path="c:\\moneydatas"
        self.lbl_path.setText(self.path)
        self.led_name.setText("記帳系統匯出檔")
        self.cmb_fileType.setCurrentIndex(0)
    #匯出檔案
    def exportFile(self):
        try:
            if self.cmb_fileType.currentIndex() == 0:
                self.data.to_csv(f'{self.lbl_path.text()}/{self.led_name.text()}.csv',encoding='utf-8-sig')
            elif self.cmb_fileType.currentIndex() == 1:
                self.data.to_json(f'{self.lbl_path.text()}/{self.led_name.text()}.json')
            else:
                self.data.to_excel(f'{self.lbl_path.text()}/{self.led_name.text()}.xlsx')
            MessageBox.show('匯出完成','通知',icon=1,btns=(QMessageBox.Ok),mode=False)  
        except Exception as e:
             MessageBox.show(e,"警告",icon=2,btns=(QMessageBox.Ok),mode=False)

        
if __name__ == '__main__':
#執行視窗程式
    app=QApplication(sys.argv)
    mainWindow=FileWindow()
    mainWindow.show()
    app.exec()
