from datetime import datetime
import mysql.connector
import sys 
from ppp import P
from ui.moneydata_ui_insertwindow import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QAbstractItemView,QMessageBox
from PyQt5.QtCore import Qt
from Ms import MessageBox
from PyQt5.QtGui import QFont
#輸入視窗
class InsWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.count=0#表格的計數器
        #設定按鈕功能
        self.btn_save.clicked.connect(self.save)
        self.btn_insert.clicked.connect(self.insert)
        self.btn_insert_cls.clicked.connect(self.icl)
        self.btn_cls.clicked.connect(self.cl)
        self.btn_real_date.clicked.connect(lambda:P.show_date(self,30,185,self.led_real_date))
        self.btn_cancel.clicked.connect(lambda :P.exit(self))
        self.btn_ok.clicked.connect(lambda :P.ok(self,f"{self.upload_num()},確定要離開?",'通知'))

        self.led_real_date.setReadOnly(True)#禁止更改實際日期輸入框內容
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止更改表格內容
    #將資料輸入區的資料設定倒帶上傳區
    def save(self):
        try:
            P.check(self.cmb_type.currentText(),name='類別',blank_check=True,num_check=False)
            P.check(self.led_name.text(),name="名稱",blank_check=True,num_check=False)
            P.check(self.led_money.text(),name="金額",blank_check=True,num_check=True)
            P.check(self.led_real_date.text(),name="實際日期",blank_check=True,num_check=False)
            #備註為空的情況下內容自動設定為 無
            if self.led_note.text()=='':
                note='無'
            else:
                note=self.led_note.text()
            #標頭加粗
            font = self.tableWidget.horizontalHeader().font()
            font.setBold(True)
            self.tableWidget.horizontalHeader().setFont(QFont("song", 12, QFont.Bold))
            #設定ROW的數量
            self.tableWidget.setRowCount(self.count+1)
            #設定表格內容
            for i,text in enumerate([self.led_name.text(),self.led_money.text(),self.led_real_date.text(),self.cmb_type.currentText(),note,'未上傳']):
                item=QTableWidgetItem(text)#生成物件
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)#內容置中
                self.tableWidget.setItem(self.count,i,item)#將物件設定置表格
            self.count+=1 
        except Exception as e:
            MessageBox.show(e,"警告",icon=2,btns=(QMessageBox.Ok),mode=False)
     #回報目前待上傳情報    
    def upload_num(self):
        count=0#未上傳計數器
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i,5).text() == '未上傳':
                count+=1
        if count >0:
            return f"待上傳區的未上傳的資料為{count}筆"
        elif count ==0 and self.tableWidget.rowCount() != 0:
            return f"待上傳區資料都已上傳"
        elif self.tableWidget.rowCount() ==0:
            return f"待上傳區資料並無資料"
    #將待上傳區的資料寫進資料庫
    def insert(self):
        now=datetime.now()
        datas=[]#總LIST
        connection=None
        try:
            if self.tableWidget.rowCount() == 0:#確認表格有沒有內容
                MessageBox.show('請先輸入資料再上傳',"警告",icon=2,btns=(QMessageBox.Ok),mode=False) 
            else:
                for i in range(self.tableWidget.rowCount()):
                    #d為要上傳的單筆資料形成的LIST
                    d=[now.strftime('%Y-%m-%d '),now.strftime('%H:%M:%S'),self.tableWidget.item(i,0).text()
                       ,self.tableWidget.item(i,1).text(),self.tableWidget.item(i,2).text(),self.tableWidget.item(i,3).text(),self.tableWidget.item(i,4).text()]
                    #確定是為上傳加到總LIST
                    if self.tableWidget.item(i,5).text() == '未上傳':
                        datas.append(d)
                connection = mysql.connector.connect(host=P.host,user=P.user ,password=P.password,database='moneydatas')
                cursor = connection.cursor()
                command='insert into moneydata (輸入日期,輸入時間,名稱,金額,實際日期,類別,備註) values (%s,%s,%s,%s,%s,%s,%s )'
                cursor.executemany(command,datas) 
                connection.commit()
                count=0#檢測上傳幾筆的計數器
                #將未上傳改為已上傳同時確認有幾筆
                for i in range(self.tableWidget.rowCount()):
                    if self.tableWidget.item(i,5).text() == '未上傳':
                        self.tableWidget.setItem(i,5,QTableWidgetItem('已上傳'))
                        count+=1
                MessageBox.show(f'{count}筆資料,以上傳成功',"通知",icon=1,btns=(QMessageBox.Ok),mode=False) 
        except Exception as e:
            MessageBox.show(e,"警告",icon=2,btns=(QMessageBox.Ok),mode=False)   
        finally:
            if connection != None:
                connection.close()
    #清除資料輸入區的內容
    def cl(self):
        self.led_money.setText('')
        self.led_name.setText('')
        self.led_note.setText('')
        self.led_real_date.setText('')
        self.cmb_type.setCurrentIndex(0)
    #將待上傳區的表格清空
    def icl(self):
        re=MessageBox.show('確定要清空待上傳區嗎?',"通知",icon=4,btns=(QMessageBox.Ok, QMessageBox.Cancel),mode=True)
        if re==QMessageBox.Ok:
            self.tableWidget.clear()#清空表格
            #清空表格只會清空文字內容所以需要進行下面的設定
            self.tableWidget.setRowCount(0)#設定ROW
            self.count=0#表格計數歸零
            self.tableWidget.setHorizontalHeaderLabels(["名稱","金額","實際日期","類別","備註","上傳資訊"])#設置標頭內容

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=InsWindow()
    mainWindow.show()
    app.exec()
