# -*- coding:utf-8 -*-
from ui.moneydata_ui_one_updatewindow import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Ms import MessageBox
import sys
import mysql.connector
from ppp import P
#更新視窗
class OneWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.led_real_date.setReadOnly(True)#禁止更改實際日期輸入框內容
        #設定按鈕功能
        self.btn_update.clicked.connect(self.up)
        self.btn_real_date.clicked.connect(lambda:P.show_date(self,20,190,self.led_real_date))
        self.btn_cls.clicked.connect(self.cl)
        self.btn_ok.clicked.connect(lambda :P.ok(self,"確定要離開?",'通知'))
        self.btn_cancel.clicked.connect(lambda :P.exit(self))
        self.lbl_data.setAlignment(QtCore.Qt.AlignCenter)#內容置中
        self.lbl_data.setWordWrap(True)#自動換行
        self.num=0
        
      #生成修改的程式碼並執行
    def up(self):
        connection=None
        count=0
        try:
            #檢查金額的輸入內容是否數字跟大於0
            P.check(self.led_money.text(),'金額',blank_check=False,num_check=True)
            #生成條件式
            command_add=' set '
            if self.cmb_type.currentText() != '':
                command_add+=f"  類別 = '{self.cmb_type.currentText()}'"
                count=1
            if self.led_name.text() != '':
                if count == 1:
                    command_add+=f" and 名稱 = '{self.led_name.text()}'"
                else:
                    command_add+=f"  名稱 = '{self.led_name.text()}'"
                    count=1
            if self.led_real_date.text() != '':
                if count == 1:
                    command_add+=f" and 實際日期 = '{self.led_real_date.text()}'"
                else:
                    command_add+=f"  實際日期 = '{self.led_real_date.text()}'"
                    count=1
            if self.led_money.text() != '':
                if count == 1:
                    command_add+=f" and 金額 = {self.led_money.text()}"
                else:
                    command_add+=f"  金額 = {self.led_money.text()}"
                    count=1
            if self.led_note.text() != '':
                if count == 1:
                    command_add+=f" and 備註 = '{self.led_note.text()}'"
                else:
                    command_add+=f"  備註 = '{self.led_note.text()}'"
            connection = mysql.connector.connect(host=P.host,user=P.user ,password=P.password,database='moneydatas')
            cursor = connection.cursor()
            command='update moneydata'
            cursor.execute(command+command_add+f'  where id = {self.num}')
            connection.commit()
        
        except Exception as e:
                MessageBox.show(f'{e}!','通知',icon=1,btns=(QMessageBox.Ok),mode=False)
        finally:
            if connection != None:
                connection.close()
                MessageBox.show('修改成功!!','通知',icon=1,btns=(QMessageBox.Ok),mode=False)
    #清空修改區的內容
    def cl(self):
        self.led_money.setText('')
        self.led_name.setText('')
        self.led_note.setText('')
        self.cmb_type.setCurrentIndex(0)
        self.led_real_date.setText('')
    #
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=OneWindow()
    mainWindow.show()
    app.exec()