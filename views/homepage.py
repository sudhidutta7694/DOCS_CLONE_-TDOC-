# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuck.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from nav import Ui_MainWindow

class Ui_HomeWindow(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("")) #add logo
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 0, 67, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(50, 100, 151, 221))
        font = QtGui.QFont()
        font.setPointSize(67)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 161, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 360, 121, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 551, 25))
        self.lineEdit.setObjectName("lineEdit")
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "HomeWindow"))
        self.label_2.setText(_translate("HomeWindow", "Docify"))
        self.label_4.setText(_translate("HomeWindow", "Hello XYZ"))
        self.pushButton.setText(_translate("HomeWindow", "+"))
        self.label_3.setText(_translate("HomeWindow", "Create new Document"))
        self.label_5.setText(_translate("HomeWindow", "My Documents"))
        self.lineEdit.setPlaceholderText(_translate("HomeWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())