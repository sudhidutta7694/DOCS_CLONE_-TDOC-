# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sudhi-sundar-dutta/Desktop/DOCS_CLONE/ui/home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeScreen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_label = QtWidgets.QLabel(HomeScreen)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout.addWidget(self.welcome_label)

        self.retranslateUi(HomeScreen)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "HomeScreen"))