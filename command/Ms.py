# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMessageBox
class MessageBox():
    @staticmethod
    def show(msg, title='',icon=1, btns=None,mode=True):
        dialog=QMessageBox()
        dialog.setWindowTitle(title)
        dialog.setText(str(msg))
        dialog.setIcon(icon)
        if btns is not None:
            if mode:
                for btn in btns:
                    dialog.addButton(btn)
            else:
                dialog.addButton(btns)
        return dialog.exec()
