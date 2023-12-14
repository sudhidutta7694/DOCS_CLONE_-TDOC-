# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sudhi-sundar-dutta/Desktop/DOCS_CLONE/ui/signup.ui'
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
        self.image.setGeometry(QtCore.QRect(480, 300, 421, 341))
        self.image.setStyleSheet("image {\n"
"    border: black 1px solid\n"
"}")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("/home/sudhi-sundar-dutta/Desktop/DOCS_CLONE/ui/../resources/images/reshot-illustration-website-design-U3PZXDSEVY 1.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #474BCA; font-size: 36px; word-wrap: break-word    \n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 191, 61))
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
        self.label_3.setGeometry(QtCore.QRect(30, 270, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 431, 50))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setStyleSheet("QLabel {\n"
"    color: #474BCA; font-size: 26px; word-wrap: break-word    \n"
"}")
        self.label_6.setObjectName("label_6")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(30, 510, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 610, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.lineEditEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(30, 540, 431, 51))
        self.lineEditEmail.setStyleSheet("QLineEdit {\n"
"width: 100%; height: 100%; background: #FFA3BE; border-radius: 5px; padding-left: 20px;\n"
"}")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(30, 640, 431, 51))
        self.lineEditPassword.setStyleSheet("QLineEdit {\n"
"width: 100%; height: 100%; background: #FFA3BE; border-radius: 5px; padding-left: 20px;\n"
"}")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonEmail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEmail.setGeometry(QtCore.QRect(30, 730, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        self.pushButtonEmail.setFont(font)
        self.pushButtonEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonEmail.setStyleSheet("QPushButton {\n"
"width: 100%; height: 100%; background: #474BCA; border-radius: 5px; color: white; font-family: \"Inter\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"}")
        self.pushButtonEmail.setObjectName("pushButtonEmail")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 780, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.accountLabel = QtWidgets.QLabel(self.centralwidget)
        self.accountLabel.setGeometry(QtCore.QRect(210, 780, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.accountLabel.setFont(font)
        self.accountLabel.setOpenExternalLinks(True)
        self.accountLabel.setObjectName("accountLabel")
        self.logInLabel = QtWidgets.QLabel(self.centralwidget)
        self.logInLabel.setGeometry(QtCore.QRect(350, 780, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.logInLabel.setFont(font)
        self.logInLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logInLabel.setOpenExternalLinks(True)
        self.logInLabel.setObjectName("logInLabel")
        self.fullName = QtWidgets.QLabel(self.centralwidget)
        self.fullName.setGeometry(QtCore.QRect(30, 410, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fullName.setFont(font)
        self.fullName.setObjectName("fullName")
        self.lineEditFullName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFullName.setGeometry(QtCore.QRect(30, 440, 431, 51))
        self.lineEditFullName.setStyleSheet("QLineEdit {\n"
"width: 100%; height: 100%; background: #FFA3BE; border-radius: 5px; padding-left: 20px;\n"
"}")
        self.lineEditFullName.setObjectName("lineEditFullName")
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
        self.label.setText(_translate("MainWindow", "DOCIFY"))
        self.label_2.setText(_translate("MainWindow", "Sign Up "))
        self.label_3.setText(_translate("MainWindow", "Hi, welcome to DOCIFY!"))
        self.label_6.setText(_translate("MainWindow", "SignUp with Email"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.lineEditEmail.setPlaceholderText(_translate("MainWindow", "Enter your Email Id"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.pushButtonEmail.setText(_translate("MainWindow", "Sign Up"))
        self.label_4.setText(_translate("MainWindow", "Already Registered?"))
        self.accountLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5555ff;\">Having an account </span></p></body></html>"))
        self.logInLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff557f;\">Log In</span></p></body></html>"))
        self.fullName.setText(_translate("MainWindow", "Full Name"))
        self.lineEditFullName.setPlaceholderText(_translate("MainWindow", "Enter your Full Name"))
