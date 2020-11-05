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
import re

class MainWin(QWidget, Ui_XueXiQiangGuo):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        self.connecter()
        self.isTop = False
        self.data = ''
        self.get_from_csv()
        self.answer = []
        self.LineEdit.setClearButtonEnabled(True)

    def connecter(self):
        self.TopBtn.clicked.connect(self.change_top)
        self.FindBtn.clicked.connect(self.find_answer)
        self.OffFindButton.clicked.connect(self.find_answer_off)

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
        if Qt.Key_Enter == key:
            self.find_answer()
        elif Qt.Key_Return == key:
            self.find_answer_off()
        elif Qt.Key_Alt == key:
            self.LineEdit.clear()



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
                    self.LineEdit.clear()
                    j = 1
                    for i in range(data_len):
                        if i % 2 != 0:
                            self.outputWritten(str(j) + '、' + str(list(list(bs.find_all(class_='list'))[0])[i].text.split(' ')[-1]))
                            j += 1
            except BaseException as e:
                reply = QMessageBox.warning(self, '网络错误','网络连接失败，请检查网络连接')

    # 离线搜索
    def find_answer_off(self):
        self.textBrowser.clear()
        self.answer = []
        text = self.LineEdit.text()
        if text == '':
            reply = QMessageBox.warning(self, '注意！', '输入内容为空，请重新输入')
        else:
            s = self.KMP()
            for i in self.data:
                if s.kmp(i[0], text) != -1:
                    self.answer.append(i)
            if len(self.answer) == 0:
                self.outputWritten("暂无匹配数据，换个题目试试？")
                return False
            else:
                self.outputWritten("匹配题目个数：%d" % (len(self.answer)) + '\n')
                self.LineEdit.clear()
                for i in self.answer:
                    self.outputWritten(i[0] + '\n')
                return True

    class KMP:
        # 获取next数组
        def get_next(self, T):
            i = 0
            j = -1
            next_val = [-1] * len(T)
            while i < len(T) - 1:
                if j == -1 or T[i] == T[j]:
                    i += 1
                    j += 1
                    # next_val[i] = j
                    if i < len(T) and T[i] != T[j]:
                        next_val[i] = j
                    else:
                        next_val[i] = next_val[j]
                else:
                    j = next_val[j]
            return next_val

        # KMP算法
        def kmp(self, S, T):
            i = 0
            j = 0
            next = self.get_next(T)
            while i < len(S) and j < len(T):
                if j == -1 or S[i] == T[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if j == len(T):
                return i - j
            else:
                return -1

    # 从本地题库中获取数据
    def get_from_csv(self):
        if self.data == '':
            with open('data.csv', 'r', encoding='utf-8') as f:
                content = f.readlines()
            data = []
            for i in content:
                tmp = i.strip()
                if tmp == '':
                    continue
                elif tmp != '' and re.match(r"\d", tmp[0]):
                    data.append(tmp.split(r"[.、]"))
                else:
                    data.append(tmp)
            self.data = data
            return True
        else:
            return False


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
