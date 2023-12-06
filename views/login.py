# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 889)
        MainWindow.setStyleSheet("background-color: rgba(249,230,230,1)")
        MainWindow.setIconSize(QtCore.QSize(28, 28))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(590, 260, 421, 341))
        self.image.setStyleSheet("image {\n"
"    border: black 1px solid\n"
"}")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("ui/../resources/images/reshot-illustration-website-design-U3PZXDSEVY 1.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #474BCA; font-size: 28px; word-wrap: break-word    \n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("Qlabel {\n"
"color: black; font-size: 48px; font-family: Inter; font-weight: 700; word-wrap: break-word;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 220, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButtonGoogle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGoogle.setGeometry(QtCore.QRect(80, 270, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGoogle.setFont(font)
        self.pushButtonGoogle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonGoogle.setStyleSheet("QPushButton {\n"
"width: 100%; height: 100%; background: #FFA3BE; border-radius: 5px; color: white;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../resources/images/flat-color-icons_google.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGoogle.setIcon(icon)
        self.pushButtonGoogle.setIconSize(QtCore.QSize(28, 28))
        self.pushButtonGoogle.setObjectName("pushButtonGoogle")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 340, 431, 17))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setStyleSheet("QLabel { color: gray}")
        self.label_6.setObjectName("label_6")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(80, 390, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 520, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.lineEditEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(80, 430, 431, 51))
        self.lineEditEmail.setStyleSheet("QLineEdit {\n"
"width: 100%; height: 100%; background: #FFA3BE; border-radius: 5px; padding-left: 20px;\n"
"}")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(80, 560, 431, 51))
        self.lineEditPassword.setStyleSheet("QLineEdit {\n"
"width: 100%; height: 100%; background: #FFA3BE; border-radius: 5px; padding-left: 20px;\n"
"}")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonEmail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEmail.setGeometry(QtCore.QRect(80, 670, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        self.pushButtonEmail.setFont(font)
        self.pushButtonEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonEmail.setStyleSheet("QPushButton {\n"
"width: 100%; height: 100%; background: #474BCA; border-radius: 5px; color: white; font-family: \"Inter\";\n"
"}")
        self.pushButtonEmail.setObjectName("pushButtonEmail")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 730, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.createAccountLabel = QtWidgets.QLabel(self.centralwidget)
        self.createAccountLabel.setGeometry(QtCore.QRect(260, 730, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.createAccountLabel.setFont(font)
        self.createAccountLabel.setOpenExternalLinks(True)
        self.createAccountLabel.setObjectName("createAccountLabel")
        self.signUpLabel = QtWidgets.QLabel(self.centralwidget)
        self.signUpLabel.setGeometry(QtCore.QRect(400, 730, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.signUpLabel.setFont(font)
        self.signUpLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signUpLabel.setOpenExternalLinks(True)
        self.signUpLabel.setObjectName("signUpLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Docs Clone"))
        self.label_2.setText(_translate("MainWindow", "Login now"))
        self.label_3.setText(_translate("MainWindow", "Hi, welcome back"))
        self.pushButtonGoogle.setText(_translate("MainWindow", "Login with Google"))
        self.label_6.setText(_translate("MainWindow", "---------------------------------------   or Login with Email   ----------------------------------------"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.lineEditEmail.setPlaceholderText(_translate("MainWindow", "Enter your Email Id"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.pushButtonEmail.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "Not Registered Yet?"))
        self.createAccountLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5555ff;\">Create an account </span></p></body></html>"))
        self.signUpLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff557f;\">Sign Up</span></p></body></html>"))
# import reshot-illustration-website-design-U3PZXDSEVY 1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
