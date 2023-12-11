# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/navbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonRedo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRedo.setGeometry(QtCore.QRect(350, 0, 51, 21))
        self.pushButtonRedo.setObjectName("pushButtonRedo")
        self.pushButtonUndo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUndo.setGeometry(QtCore.QRect(300, 0, 51, 21))
        self.pushButtonUndo.setObjectName("pushButtonUndo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 0, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 0, 31, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 0, 31, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 0, 201, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setIndent(1)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 49, 1131, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButtonColour = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonColour.setGeometry(QtCore.QRect(580, 0, 89, 21))
        self.pushButtonColour.setStyleSheet("QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButtonColour.setObjectName("pushButtonColour")
        self.pushButtonFont = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFont.setGeometry(QtCore.QRect(400, 0, 89, 21))
        self.pushButtonFont.setObjectName("pushButtonFont")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(0, 0, 31, 25))
        self.pushButtonBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../resources/images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBack.setIcon(icon)
        self.pushButtonBack.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonShare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShare.setGeometry(QtCore.QRect(220, 0, 80, 25))
        self.pushButtonShare.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 85, 255);\n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../resources/images/share.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonShare.setIcon(icon1)
        self.pushButtonShare.setObjectName("pushButtonShare")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuInsert = QtWidgets.QMenu(self.menubar)
        self.menuInsert.setObjectName("menuInsert")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuExtensions = QtWidgets.QMenu(self.menubar)
        self.menuExtensions.setObjectName("menuExtensions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAccess = QtWidgets.QMenu(self.menubar)
        self.menuAccess.setObjectName("menuAccess")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInsert = QtWidgets.QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionImage = QtWidgets.QAction(MainWindow)
        self.actionImage.setObjectName("actionImage")
        self.actionTable = QtWidgets.QAction(MainWindow)
        self.actionTable.setObjectName("actionTable")
        self.actionChart = QtWidgets.QAction(MainWindow)
        self.actionChart.setObjectName("actionChart")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setStatusTip("")
        self.actionsave.setObjectName("actionsave")
        self.actionConvert_to_pdf = QtWidgets.QAction(MainWindow)
        self.actionConvert_to_pdf.setObjectName("actionConvert_to_pdf")
        self.actionRestricted = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/../resources/images/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestricted.setIcon(icon2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.actionRestricted.setFont(font)
        self.actionRestricted.setObjectName("actionRestricted")
        self.actionReadable = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/../resources/images/read.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReadable.setIcon(icon3)
        self.actionReadable.setObjectName("actionReadable")
        self.actionWritable_2 = QtWidgets.QAction(MainWindow)
        self.actionWritable_2.setObjectName("actionWritable_2")
        self.actionWritable = QtWidgets.QAction(MainWindow)
        self.actionWritable.setObjectName("actionWritable")
        self.actionWritable_3 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/../resources/images/write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWritable_3.setIcon(icon4)
        self.actionWritable_3.setObjectName("actionWritable_3")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setWhatsThis("")
        self.actionRename.setObjectName("actionRename")
        self.actionConvert_to_PDF = QtWidgets.QAction(MainWindow)
        self.actionConvert_to_PDF.setObjectName("actionConvert_to_PDF")
        self.menuFile.addAction(self.actionRename)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConvert_to_PDF)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionPaste)
        self.menuInsert.addAction(self.actionImage)
        self.menuInsert.addAction(self.actionTable)
        self.menuAccess.addAction(self.actionRestricted)
        self.menuAccess.addSeparator()
        self.menuAccess.addSeparator()
        self.menuAccess.addAction(self.actionReadable)
        self.menuAccess.addAction(self.actionWritable_3)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuExtensions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAccess.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonRedo.setText(_translate("MainWindow", "Redo"))
        self.pushButtonUndo.setText(_translate("MainWindow", "Undo"))
        self.pushButton.setText(_translate("MainWindow", "B"))
        self.pushButton_2.setText(_translate("MainWindow", "I"))
        self.pushButton_3.setText(_translate("MainWindow", "U"))
        self.pushButton_6.setText(_translate("MainWindow", " Untitled Doc"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:normal; color:#1803ff;\">Hello, XYZ</span></p></body></html>"))
        self.pushButtonColour.setText(_translate("MainWindow", "Colour"))
        self.pushButtonFont.setText(_translate("MainWindow", "Font"))
        self.pushButtonShare.setText(_translate("MainWindow", "Share"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuInsert.setTitle(_translate("MainWindow", "Insert"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuExtensions.setTitle(_translate("MainWindow", "Extensions"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAccess.setTitle(_translate("MainWindow", "Access"))
        self.actionInsert.setText(_translate("MainWindow", "Insert"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "creates a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "opens a file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionTable.setText(_translate("MainWindow", "Link"))
        self.actionChart.setText(_translate("MainWindow", "Chart"))
        self.actionsave.setText(_translate("MainWindow", "Save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionConvert_to_pdf.setText(_translate("MainWindow", "Convert to pdf"))
        self.actionRestricted.setText(_translate("MainWindow", "Restricted"))
        self.actionReadable.setText(_translate("MainWindow", "Readable"))
        self.actionWritable_2.setText(_translate("MainWindow", "Writable"))
        self.actionWritable.setText(_translate("MainWindow", "Writable"))
        self.actionWritable_3.setText(_translate("MainWindow", "Writable"))
        self.actionRename.setText(_translate("MainWindow", "Rename"))
        self.actionRename.setStatusTip(_translate("MainWindow", "Rename a File"))
        self.actionRename.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionConvert_to_PDF.setText(_translate("MainWindow", "Convert to PDF"))
        self.actionConvert_to_PDF.setStatusTip(_translate("MainWindow", "Converts text to PDF"))
        self.actionConvert_to_PDF.setShortcut(_translate("MainWindow", "Ctrl+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
