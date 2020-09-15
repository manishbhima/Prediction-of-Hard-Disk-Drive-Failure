# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\userhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from RandomForestPrediction import Prediction

class UserHome(object):
    def browsefile(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File",
                                                                "G://",
                                                                "*.csv")
            print(fileName)
            self.testfile.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)
    

    def predictiondef(self):
        rf = Prediction()
        file=self.testfile.text()
        res=rf.accuracy(file)
        print(res)
        self.resultname.setText("Result:")
        self.resultname_2.setText(str(res))





        

    def setupUi(self, box):
        box.setObjectName("box")
        box.resize(888, 611)
        box.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(box)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 640))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.frame = QtWidgets.QFrame(self.Home)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 630))
        self.frame.setStyleSheet("background-image: url(bg2.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.Home, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 881, 571))
        self.tableView.setStyleSheet("background-image: url(bg.jpg);")
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(70, 190, 281, 40))
        self.label.setStyleSheet("font: 12pt \"MS PGothic\";")
        self.label.setObjectName("label")
        self.resultname_2 = QtWidgets.QLabel(self.tab)
        self.resultname_2.setGeometry(QtCore.QRect(680, 260, 170, 41))
        self.resultname_2.setStyleSheet("font: 75 16pt \"Levenim MT\";")
        self.resultname_2.setObjectName("resultname_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 280, 110, 30))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.tab)
        self.pushButton2.setGeometry(QtCore.QRect(70, 280, 110, 30))
        self.pushButton2.setObjectName("pushButton2")
        #------------------------------
        
        self.pushButton.clicked.connect(self.predictiondef)


        self.testfile = QtWidgets.QLineEdit(self.tab)
        self.testfile.setGeometry(QtCore.QRect(70, 240, 310, 30))
        self.testfile.setText("")
        self.testfile.setObjectName("testfile")
        self.pushButton2.clicked.connect(self.browsefile)
        self.resultname = QtWidgets.QLabel(self.tab)
        self.resultname.setGeometry(QtCore.QRect(500, 260, 121, 41))
        self.resultname.setStyleSheet("font: 75 16pt \"Levenim MT\";")
        self.resultname.setObjectName("resultname")
        self.tabWidget.addTab(self.tab, "")
        box.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(box)
        self.statusbar.setObjectName("statusbar")
        box.setStatusBar(self.statusbar)

        self.retranslateUi(box)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(box)

    def retranslateUi(self, box):
        _translate = QtCore.QCoreApplication.translate
        box.setWindowTitle(_translate("box", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("box", "Home"))
        self.label.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Upload Test File</span></p></body></html>"))
        #self.resultname_2.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Non</span></p></body></html>"))
        self.pushButton.setText(_translate("box", "Prediction"))
        self.pushButton2.setText(_translate("box", "Browse"))
        #self.resultname.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Result:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("box", "Prediction"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = UserHome()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
