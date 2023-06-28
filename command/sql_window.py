# -*- coding:utf-8 -*-
from ui.moneydata_ui_sqlwindow import *
import mysql.connector
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from ppp import P
from Ms import MessageBox


class SqlWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.argee=False#使用許可
        #設定按鈕功能
        self.btn_cancel.clicked.connect(lambda :P.exit(self))
        self.btn_conn.clicked.connect(self.conn)
        self.led_password.setEchoMode(QtWidgets.QLineEdit.Password)#密碼欄文字替換成點
        
    def conn(self):
        connection=None
        try:
            connection = mysql.connector.connect(host=self.led_host.text(),user=str(self.led_user.text()).replace("'",""), password=str(self.led_password.text()).replace("'",""))
            cursor = connection.cursor()
            re=MessageBox.show("是否使用這組資訊進行後續動作","使用許可",icon=4,btns=(QMessageBox.Ok, QMessageBox.Cancel),mode=True)
            if re==QMessageBox.Ok:
                self.argee=True         
                self.lbl_conn.setText('連線成功')
                cursor.execute('show databases')
                records = cursor.fetchall()
                #沒有資料庫時自動新增
                if ('moneydatas',) not in [ r for r in records]:
                    cursor.execute("CREATE SCHEMA `moneydatas`  DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;")
                    connection.commit()
                cursor.execute("USE `moneydatas`")
                connection.commit()
                cursor.execute('show tables')
                records = cursor.fetchall()
                #沒有table時自動新增
                if ('moneydata',) not in [ r for r in records]:
                    cursor.execute("CREATE TABLE `moneydatas`.`moneydata` (`id` INT NOT NULL AUTO_INCREMENT,`名稱` VARCHAR(45) NOT NULL,`金額` INT NOT NULL,`類別`\
                                    VARCHAR(2) NOT NULL,`實際日期` DATE NOT NULL,`輸入日期` DATE NOT NULL,`輸入時間` TIME NOT NULL,`備註` TEXT NULL,PRIMARY KEY (`id`))\
                                    ENGINE = InnoDB\
                                    DEFAULT CHARACTER SET = utf8\
                                    COLLATE = utf8_unicode_ci;")
                    connection.commit()
        except Exception as e:
            self.lbl_conn.setText('連線失敗')
            MessageBox.show(f'{e}!','通知',icon=1,btns=(QMessageBox.Ok),mode=False)
        finally:
            if connection !=None:
                connection.close()
