from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NOVAUI(object):
    cpath =""
    def setupUi(self, NOVAUI):
        NOVAUI.setObjectName("NOVAUI")
        NOVAUI.resize(2000, 1000)
        self.centralwidget = QtWidgets.QWidget(NOVAUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, -50, 1981, 1091))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\download.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1700, 950, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 136, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1580, 950, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1200, 50, 181, 51))
        self.textBrowser.setStyleSheet("background:transparent;\n"
        "border-radius:skyblue;\n"
        "color : white;\n"
        "font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1400, 50, 181, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
        "border-radius:skyblue;\n"
        "color : white;\n"
        "font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
    
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1000, 180, 241, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\hello.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
      
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1170, 260, 631, 601))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\fram1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(625, 700, 641, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\lines1.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1266, 200, 251, 471))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\hello.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1610, 120, 221, 321))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\circle.gif"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1160, 10, 191, 91))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\frame10.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1350, 10, 191, 91))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\frame10.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(-30, 780, 201, 111))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\powersource.gif"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
       
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1210, 20, 91, 31))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);\n"
        "font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1390, 20, 91, 31))
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);\n"
        "font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(325, 200 , 251, 471))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\hello.gif"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
       
        self.label_7.raise_()
        self.label_8.raise_()
      
        self.label_16.raise_()
        NOVAUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(NOVAUI)
        QtCore.QMetaObject.connectSlotsByName(NOVAUI)

    def retranslateUi(self, NOVAUI):
        _translate = QtCore.QCoreApplication.translate
        NOVAUI.setWindowTitle(_translate("NOVAUI", "MainWindow"))
        self.pushButton_3.setText(_translate("NOVAUI", "EXIT"))
        self.pushButton_4.setText(_translate("NOVAUI", "RUN"))
        self.label_14.setText(_translate("NOVAUI", "    DATE"))
        self.label_15.setText(_translate("NOVAUI", "      TIME"))
    
    def __init__(self, path):
        self.cpath = path


if __name__ == "__main__":
    import sys
    import os
    
    current_path = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    NOVAUI = QtWidgets.QMainWindow()
    ui = Ui_NOVAUI(path=current_path)
    ui.setupUi(NOVAUI)
    NOVAUI.show()
    sys.exit(app.exec_())
