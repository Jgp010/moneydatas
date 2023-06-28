# -*- coding:utf-8 -*-
from ins_window import InsWindow
from sql_window import SqlWindow
from up_window import OneWindow
from fileExprot_window import FileWindow
from ppp import P
import mysql.connector
from ui.moneydata_ui_mainwindow import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QAbstractItemView,QMessageBox, QMenu, QAction
import pandas as pd
from Ms import MessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QIcon

#主視窗
class MoneySqlMainWindow(QMainWindow,Ui_mainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #設定按鈕功能
        self.btn_in.clicked.connect(self.in_window)
        self.btn_load.clicked.connect(self.load)
        self.btn_file_exprot.clicked.connect(self.file_exprot)
        self.btn_cls.clicked.connect(self.cl)
        self.btn_sql_clear.clicked.connect(self.sql_cl)
        self.btn_sql.clicked.connect(self.sqlconn)  
        self.btn_start.clicked.connect(lambda: P.show_date(self,360,70,self.led_date_start))
        self.btn_end.clicked.connect(lambda: P.show_date(self,615,70,self.led_date_end))
        self.btn_start_rl.clicked.connect(lambda: P.show_date(self,400,115,self.led_date_start_rl))
        self.btn_end_rl.clicked.connect(lambda: P.show_date(self,655,115,self.led_date_end_rl))
        self.sort=False
        self.sort_values=0
        self.led_date_start.setReadOnly(True)#禁止更改起始日期輸入框內容
        self.led_date_end.setReadOnly(True)#禁止更改結束日期輸入框內容
        self.led_date_start_rl.setReadOnly(True)#禁止更改實際日期輸入框內容
        self.led_date_end_rl.setReadOnly(True)
        self.twt.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止更改表格內容
        self.disableUI(self.btn_sql)
    #開啟SQL輸入視窗
    def sqlconn(self):
        self.sqlw=SqlWindow()
        self.sqlw.show()
        #設定SQL視窗確認鍵功能
        self.sqlw.btn_ok.clicked.connect(lambda: self.ok(self.sqlw,f"目前連線結果為{self.sqlw.lbl_conn.text()},確定要離開?","連線狀態"))
    #ok鍵功能
    def ok(self,window,text,title):
        re=MessageBox.show(text,title,icon=4,btns=(QMessageBox.Ok, QMessageBox.Cancel),mode=True)
        if self.sqlw.argee:
            P.setdata(self.sqlw.led_host.text(),str(self.sqlw.led_user.text()),str(self.sqlw.led_password.text()))
            self.lbl_sql_2.setText(f'host:{P.host}   user:{P.user}   database:moneydatas')#將SQL連線資訊設定在主視窗
            self.enableUI()
        if re==QMessageBox.Ok:
           window.close()#關閉視窗
       
    #開啟輸入資料視窗
    def in_window(self): 
        self.insretw=InsWindow() 
        self.insretw.show()
        x = self.insretw.pos().x()       # 取得輸入資料目前 x 座標
        y = self.insretw.pos().y()       # 取得輸入資料目前 y 座標
        self.insretw.move(x+100, y+100) #x,y座標各移動100

    #清空表格
    def cl_tw(self):
        self.twt.clear()
        self.twt.setColumnCount(0)
        self.twt.setRowCount(0)
        self.lbl_in.setText('')
        self.lbl_out.setText('')
        self.lbl_total.setText('')
     #根據條件讀取資料庫  
    def load(self):
        self.cl_tw()
        connection=None
        try:
            connection = mysql.connector.connect(host=P.host,user=P.user ,password=P.password,database='moneydatas')
            cursor = connection.cursor()
            command_add=self.load_cmd()#獲取條件式
            command='select  * from moneydata'
            cursor.execute(command+command_add)
            rs=cursor.fetchall()#讀取內容
            command_num='select  count(*) from moneydata'
            cursor.execute(command_num+command_add)
            r=cursor.fetchall()#讀取內容筆數
            if rs==[]:
                MessageBox.show('查無資料!!','通知',icon=1,btns=(QMessageBox.Ok),mode=False)
            else:
                re=MessageBox.show(f"符合條件的資料為{str(r[0]).replace(',','').replace('(','').replace(')','')}筆,要顯示嗎?",
                                    '通知',icon=4,btns=(QMessageBox.Ok, QMessageBox.Cancel),mode=True)
                if re==QMessageBox.Ok:
                    self.set_tw(rs)
        except Exception as e:
            MessageBox.show(e,"警告",icon=2,btns=(QMessageBox.Ok),mode=False)   
            
        finally:
            if connection != None:
                connection.close()
    #根據主視窗的條件欄內容 生成讀取要用的程式碼
    def load_cmd(self):
        command=''
        command_add=''
        count=0
        #檢查id跟金額的輸入內容是否數字跟大於0
        P.check(self.led_id.text(),name="ID",blank_check=False,num_check=True)
        P.check(self.led_money.text(),name="金額",blank_check=False,num_check=True)
        #檢查日期 兩邊都有資料或都沒有
        if self.led_date_start.text() == "" and self.led_date_end.text() !="":
            raise Exception("請選擇輸入日期的起始日期")
        elif self.led_date_start.text() != "" and self.led_date_end.text() =="":
            raise Exception("請選擇輸入日期的結束日期")
        if self.led_date_start_rl.text() == "" and self.led_date_end_rl.text() !="":
            raise Exception("請選擇實際日期的起始日期")
        elif self.led_date_start_rl.text() != "" and self.led_date_end_rl.text() =="":
            raise Exception("請選擇實際日期的結束日期")
        #產生條件式 count為確認是否有其他條件式
        if self.led_id.text() != '':
            command+=f"  id = {self.led_id.text()}"
            count=1
        if self.led_name.text() != '':
            if count == 1:
                command+=f" and 名稱 = '{self.led_name.text()}'"
            else:
                command+=f"  名稱 = '{self.led_name.text()}'"
                count=1
        if self.led_money.text() != '':
            if count == 1:
                command+=f" and 金額 = {self.led_money.text()}"
            else:
                command+=f"  金額 = '{self.led_money.text()}'"
                count=1
        if self.cmb_type.currentText() != '':
            if count == 1:
                command+=f" and 類別 = '{self.cmb_type.currentText()}'"
            else:
                command+=f"  類別 = '{self.cmb_type.currentText()}'"
                count=1
        if self.led_note.text() != '':
            if count == 1:
                command+=f" and 備註 like '%{self.led_note.text()}%'"
            else:
                command+=f"  備註 like '%{self.led_note.text()}%'"
                count=1
        if self.led_date_start.text() != "" and self.led_date_end.text() !="":
            if count == 1:
                command+=f" and 輸入日期 between '{self.led_date_start.text()}' and '{self.led_date_end.text()}'"
            else:
                command+=f"  輸入日期 between  '{self.led_date_start.text()}' and '{self.led_date_end.text()}'"
                count=1

        if self.led_date_start_rl.text() != "" and self.led_date_end_rl.text() !="":
            if count == 1:
                command+=f" and 實際日期 between '{self.led_date_start_rl.text()}' and '{self.led_date_end_rl.text()}'"
            else:
                command+=f"   實際日期 between  '{self.led_date_start_rl.text()}' and '{self.led_date_end_rl.text()}'"
                count=1
        #讀取筆數條件式
        if self.cmb_num.currentIndex() !=0:
            if self.cmb_num.currentIndex()  in [1,2,3,4,5,6,7]:
                command_add+= f' order by id  LIMIT {self.cmb_num.currentText()[1:]} '
            elif self.cmb_num.currentIndex() in [8,9,10,11,12,13,14]:
                command_add += f' order by id desc LIMIT {self.cmb_num.currentText()[1:]}'
        if command != "":
            command = " where "+command
        return command +command_add
    def set_sort(self):
        if self.cmb_sort.currentIndex() ==0:
            self.sort=False
        else:
            self.sort=True
        if self.cmb_sort_values.currentIndex() ==0:
            self.sort_values=0
        elif self.cmb_sort_values.currentIndex() ==1:
            self.sort_values=2
        elif self.cmb_sort_values.currentIndex() ==2:
            self.sort_values=4
        else:
            self.sort_values=5    
    #生成表格內容
    def set_tw(self,rs):
        #根據勾選內容 來決定更新修改列的生成
        if self.chb_Revise.isChecked():
            columnCount=9
            title=['id','名稱','金額','類別','實際日期','輸入日期','輸入時間','備註','修改或刪除']
        else:
            columnCount=8
            title=['id','名稱','金額','類別','實際日期','輸入日期','輸入時間','備註']
        #設定表格
        self.twt.setColumnCount(columnCount)
        self.twt.setRowCount(len(rs))
        self.twt.setHorizontalHeaderLabels(title)#設定標頭
        #標頭粗體化
        font = self.twt.horizontalHeader().font()
        font.setBold(True)
        self.twt.horizontalHeader().setFont(QFont("song", 12, QFont.Bold))
        #金額參數
        money_in=0
        money_out=0
        money_total=0
        #排序rs
        self.set_sort()
        rs=sorted(rs,key=lambda x:x[self.sort_values],reverse=self.sort)
        #設定表格
        for i in range( len(rs)):
            #修改更新列設定
            if self.chb_Revise.isChecked():
                p=str(rs[i][0])#擷取id資訊
                btn=QtWidgets.QPushButton()#生成按鈕
                menu = QMenu()#生成表單
                update= QAction(QIcon("menu.ico"),f"修改id={p}",menu)#生成修改
                delete=QAction(QIcon("menu.ico"),f"刪除id={p}",menu)#生成刪除
                menu.addActions([update,delete] )#將修改刪除加進表單
                update.triggered.connect(self.id_update)#設定修改功能
                delete.triggered.connect(self.id_del)#設定刪除功能
                btn.setText('下拉進行更動')#設定按鈕文字
                btn.setMenu(menu)#將選單加到按鈕
            #設定表格內容
            for j in range(8):
                item=QTableWidgetItem(str(rs[i][j]))#建立物件
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)#內容置中
                self.twt.setItem(i,j,item)#添加到表格
            #根據收入支出計算金額
            if rs[i][3] =="收入":
                money_in+=int(rs[i][2])
            else:
                money_out+=int(rs[i][2])
            #添加修改更新列
            if self.chb_Revise.isChecked():
                self.twt.setCellWidget(i,8,btn)
            #將金額設定到主畫面
            money_total=money_in-money_out
            self.lbl_in.setText(str(money_in))
            self.lbl_out.setText(str(money_out))
            self.lbl_total.setText(str(money_total))
    #修改刪除列的刪除功能(刪除選擇列的資料)
    def id_del(self):
        connection=None
        re=MessageBox.show(f'要刪除的內容為:  [id:{self.twt.item(self.twt.currentRow(),0).text()},名稱:{self.twt.item(self.twt.currentRow(),1).text()},\
                           金額:{self.twt.item(self.twt.currentRow(),2).text()},類別:{self.twt.item(self.twt.currentRow(),3).text()},\
                            際日期{self.twt.item(self.twt.currentRow(),4).text()},輸入日期:{self.twt.item(self.twt.currentRow(),5).text()},\
                                輸入時間:{self.twt.item(self.twt.currentRow(),6).text()},,備註:{self.twt.item(self.twt.currentRow(),7).text()}],確定要刪除嗎? '
                                ,'刪除警示',icon=1,btns=(QMessageBox.Ok, QMessageBox.Cancel),mode=True)
        if re==QMessageBox.Ok:
            try:
                connection = mysql.connector.connect(host=P.host,user=P.user ,password=P.password,database='moneydatas')
                cursor = connection.cursor()
                command=f'delete from moneydata where id ={self.twt.item(self.twt.currentRow(),0).text()}'
                cursor.execute(command)
                connection.commit()
            except Exception as e:
                MessageBox.show(f'{e}!','通知',icon=1,btns=(QMessageBox.Ok),mode=False)
            finally:
                if connection != None:
                    connection.close()
                    MessageBox.show('刪除成功!!','通知',icon=1,btns=(QMessageBox.Ok),mode=False)
    #修改刪除列的修改功能(生成修改視窗)
    def id_update(self):
        self.ow=OneWindow()
        self.ow.num=self.twt.item(self.twt.currentRow(),0).text()
        self.ow.lbl_data.setText(f'id:{self.twt.item(self.twt.currentRow(),0).text()},名稱:{self.twt.item(self.twt.currentRow(),1).text()},\
                                 金額:{self.twt.item(self.twt.currentRow(),2).text()}\n,類別:{self.twt.item(self.twt.currentRow(),3).text()},\
                                    實際日期{self.twt.item(self.twt.currentRow(),4).text()}\n,輸入日期:{self.twt.item(self.twt.currentRow(),5).text()},\
                                        \n輸入時間:{self.twt.item(self.twt.currentRow(),6).text()},備註:{self.twt.item(self.twt.currentRow(),7).text()}')
        self.ow.show()
  
    #清空主視窗的條件欄內容           
    def cl(self):
        self.led_date_end.setText('')
        self.led_date_start.setText('')
        self.led_money.setText('')
        self.led_name.setText('')
        self.led_note.setText('')
        self.led_id.setText('')
        self.led_date_end_rl.setText('')
        self.led_date_start_rl.setText('')
        self.cmb_type.setCurrentIndex(0)
        self.cmb_num.setCurrentIndex(0)
        self.cmb_sort.setCurrentIndex(0)
        self.cmb_sort_values.setCurrentIndex(0)
        self.lbl_in.setText('')
        self.lbl_out.setText('')
        self.lbl_total.setText('')
        self.chb_Revise.setChecked(False)
    #清空SQL資訊
    def sql_cl(self):
        self.lbl_sql_2.setText("無")
        P.zero()
        self.disableUI(self.btn_sql)
   #匯出檔案
    def file_exprot(self):
        self.filew=FileWindow()
        if self.twt.rowCount() !=0:
            datas=[]
            #把表格內的資列整合成2維陣列
            for i in range(self.twt.rowCount()) :
                data=[]
                for j in range (self.twt.columnCount()):
                    data.append(self.twt.item(i,j).text())
                datas.append(data)
            #轉成pd的dateaframe檔方便等下轉檔
            datas=pd.DataFrame(datas,columns=['id','名稱','金額','類別','實際日期','輸入日期','輸入時間','備註'])
            #將id設置成第一排
            datas.set_index('id' ,inplace=True)
            self.filew.data=datas
            self.filew.show()
        else:
            MessageBox.show('請先讀取資料再匯出檔案','警告',icon=2,btns=(QMessageBox.Ok),mode=False)
    #關閉按鈕
    def disableUI(self,ex):
        self.btn_sql_clear.setEnabled(False)
        self.btn_start.setEnabled(False)
        self.btn_end.setEnabled(False)
        self.btn_start_rl.setEnabled(False)
        self.btn_end_rl.setEnabled(False)
        self.btn_cls.setEnabled(False)
        self.btn_file_exprot.setEnabled(False)
        self.btn_in.setEnabled(False)
        self.btn_load.setEnabled(False)
        self.btn_sql.setEnabled(False)
        ex.setEnabled(True)
    #開啟按鈕
    def enableUI(self):
        self.btn_sql_clear.setEnabled(True)
        self.btn_start.setEnabled(True)
        self.btn_end.setEnabled(True)
        self.btn_start_rl.setEnabled(True)
        self.btn_end_rl.setEnabled(True)
        self.btn_cls.setEnabled(True)
        self.btn_file_exprot.setEnabled(True)
        self.btn_in.setEnabled(True)
        self.btn_load.setEnabled(True)
        self.btn_sql.setEnabled(True)

if __name__ == '__main__':
#執行視窗程式
    app=QApplication(sys.argv)
    mainWindow=MoneySqlMainWindow()
    mainWindow.show()
    app.exec()
