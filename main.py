# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XueXiQiangGuo(object):
    def setupUi(self, XueXiQiangGuo):
        XueXiQiangGuo.setObjectName("XueXiQiangGuo")
        XueXiQiangGuo.resize(433, 581)
        XueXiQiangGuo.setMinimumSize(QtCore.QSize(200, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前缀/pic/touxiang.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        XueXiQiangGuo.setWindowIcon(icon)
        XueXiQiangGuo.setAutoFillBackground(False)
        XueXiQiangGuo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(XueXiQiangGuo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.FindBtn = QtWidgets.QPushButton(XueXiQiangGuo)
        self.FindBtn.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.FindBtn.setFont(font)
        self.FindBtn.setStyleSheet("background-color: rgb(233, 1, 18);\n"
"color: rgb(255, 255, 255);")
        self.FindBtn.setObjectName("FindBtn")
        self.gridLayout.addWidget(self.FindBtn, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.LineEdit = QtWidgets.QLineEdit(XueXiQiangGuo)
        self.LineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.LineEdit.setStyleSheet("gridline-color: rgb(232, 2, 17);")
        self.LineEdit.setObjectName("LineEdit")
        self.gridLayout.addWidget(self.LineEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(XueXiQiangGuo)
        self.label.setMinimumSize(QtCore.QSize(200, 100))
        self.label.setStyleSheet("image: url(:/新前缀/pic/OIP.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(XueXiQiangGuo)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 1)
        self.TopBtn = QtWidgets.QPushButton(XueXiQiangGuo)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.TopBtn.setFont(font)
        self.TopBtn.setStyleSheet("background-color: rgb(233, 1, 18);\n"
"color: rgb(255, 255, 255);")
        self.TopBtn.setObjectName("TopBtn")
        self.gridLayout.addWidget(self.TopBtn, 0, 0, 1, 5)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(XueXiQiangGuo)
        QtCore.QMetaObject.connectSlotsByName(XueXiQiangGuo)

    def retranslateUi(self, XueXiQiangGuo):
        _translate = QtCore.QCoreApplication.translate
        XueXiQiangGuo.setWindowTitle(_translate("XueXiQiangGuo", "学习强国搜题神器"))
        self.FindBtn.setText(_translate("XueXiQiangGuo", "搜  索"))
        self.TopBtn.setText(_translate("XueXiQiangGuo", "置    顶"))
import pic_rc
