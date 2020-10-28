# @Time : 2020/6/21 11:47
# @Author : YLXY
# @File : callmain.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from main import Ui_XueXiQiangGuo
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
from urllib import parse

class MainWin(QWidget, Ui_XueXiQiangGuo):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        self.connecter()
        self.isTop = False

    def connecter(self):
        self.TopBtn.clicked.connect(self.change_top)
        self.FindBtn.clicked.connect(self.find_answer)

    def change_top(self):
        if self.isTop == False:
            self.TopBtn.setText('取 消 置 顶')
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.isTop = True
        else:
            self.TopBtn.setText('置 顶')
            self.setWindowFlags(Qt.Widget)
            self.isTop = False
        self.show()


    def keyPressEvent(self, event):
        key = event.key()
        if Qt.Key_Return == key or Qt.Key_Enter == key:
            self.find_answer()

    def find_answer(self):
        text = self.LineEdit.text()
        if text == '':
            reply = QMessageBox.warning(self, '注意！', '输入内容为空，请重新输入')
        else:
            try:
                self.textBrowser.clear()
                url_text = quote(text)
                rsp = requests.get('https://qiangguoshuo.com/search.php?q={}'.format(url_text))
                bs = BeautifulSoup(rsp.text, 'html.parser')
                data_len = len(list(list(bs.find_all(class_='list'))[0]))
                if data_len//2 == 0:
                    self.outputWritten('暂无匹配数据，换个题目试试？')
                else:
                    self.outputWritten("匹配题目个数：%d"%(data_len//2) + '\n')
                    j = 1
                    for i in range(data_len):
                        if i % 2 != 0:
                            self.outputWritten(str(j) + '、' + str(list(list(bs.find_all(class_='list'))[0])[i].text.split(' ')[-1]))
                            j += 1
            except BaseException as e:
                reply = QMessageBox.warning(self, '网络错误','网络连接失败，请检查网络连接')


    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text + '\n')
        # self.textBrowser.setTextCursor(cursor)
        # self.textBrowser.ensureCursorVisible()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MainWin()
    mainwin.show()
    sys.exit(app.exec_())
