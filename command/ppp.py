
# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMessageBox,QCalendarWidget
from Ms import MessageBox
class P():
    conn=False
    host=None
    user=None
    password=None
    sw=True
    
    @staticmethod
    def setdata(host,user,password):
        P.conn=True
        P.host=host
        P.user=user
        P.password=password
    @staticmethod
    def zero():
        P.conn=False
        P.host=None
        P.user=None
        P.password=None
    #顯示日期小工具
    @staticmethod
    def show_date(s,x,y,o):    
        if P.sw:
            P.calendar = QCalendarWidget(s)
            P.calendar.setGeometry(x,y,248,183)#設定座標
            P.calendar.clicked.connect(lambda x:P.get_date(o,qDate=x))#x 為本身元件點擊回傳的 qDate值
                
            P.calendar.show()
            P.sw=False
        else:
            P.calendar.close()#關閉小工具
            P.sw=True
    #點擊小工具將日期反饋進輸入框
    @staticmethod
    def get_date(o,qDate):
        o.setText('{0}-{1}-{2}'.format(qDate.year(),qDate.month(), qDate.day() ))

        
    @staticmethod
    def check(thing,name='',blank_check=True,num_check=True):
        
        if blank_check:
            if thing == '':
                raise Exception(f'{name}不可為空')
        if num_check:
            if thing != '':
                try: 
                    h=int(thing)
                except Exception :
                    raise Exception(f'{name}只能輸入數字')
                else:
                    if h < 0:
                        raise Exception(f'{name}的數字不可小於0')
    @staticmethod
    def ok(window,txt,title):
        re=MessageBox.show(txt,title,icon=4,btns=(QMessageBox.Ok, QMessageBox.Cancel),mode=True)
        if re==QMessageBox.Ok:
           window.close()#關閉視窗
    @staticmethod
    def exit(window):
        window.close()
        