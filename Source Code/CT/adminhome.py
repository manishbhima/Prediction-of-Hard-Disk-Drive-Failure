# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Sentiment2019Copy\adminhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SVM import SVM
from Naive import Naive
from RandomForest import RandomForest
from AccuracyStore import AccuracyStore
import time
from Graphs import view


class AdminHome(object):


    def browsefile(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File",
                                                                "G://",
                                                                "*.csv")
            print(fileName)
            self.trainfile.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def graphdef(self):
        view()

    def svmdef(self):
        print("SVM Start")
        self.trainname.setText("SVM")
        file = self.trainfile.text()
        print(file)
        start = time.time()
        s = SVM()
        a=s.accuracy(file)
        
        end = time.time()
        t = (end - start)

        self.traintime.setText(str(round(t,2)) + " (sec)")
        
        self.label_4.setText("Accuracy")
        self.trainstatus.setText(str(round(a,3)))
        AccuracyStore.store('svm',a)

    def nbdef(self):
        print("NB Start")
        self.trainname.setText("Naive Bayees")
        file = self.trainfile.text()
        print(file)
        start = time.time()
        s = Naive()
        a=s.accuracy(file)
        
        end = time.time()
        t = (end - start)

        self.traintime.setText(str(round(t,2)) + " (sec)")
        self.label_4.setText("Accuracy")
        self.trainstatus.setText(str(round(a,3)))
        AccuracyStore.store('naive',a)


    def rfdef(self):
        print("RF Start")
        self.trainname.setText("RandomForest")
        file = self.trainfile.text()
        print(file)
        start = time.time()
        s = RandomForest()
        a=s.accuracy(file)
        
        end = time.time()
        t = (end - start)

        self.traintime.setText(str(round(t,2)) + " (sec)")
        self.label_4.setText("Accuracy")
        self.trainstatus.setText(str(round(a,3)))
        AccuracyStore.store('rf',a)


        






    def setupUi(self, box):
        box.setObjectName("box")
        box.resize(899, 610)
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
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 591))
        self.frame.setStyleSheet("background-image: url(bg.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.Home)
        self.label_5.setGeometry(QtCore.QRect(70, 120, 231, 41))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.Home, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 891, 581))
        self.tableView.setStyleSheet("background-image: url(bg.jpg);")
        self.tableView.setObjectName("tableView")
        self.trainrf = QtWidgets.QPushButton(self.tab_2)
        self.trainrf.setGeometry(QtCore.QRect(40, 250, 380, 30))
        self.trainrf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.trainrf.setObjectName("trainrf")

        self.trainrf.clicked.connect(self.rfdef)



        self.trainsvm = QtWidgets.QPushButton(self.tab_2)
        self.trainsvm.setGeometry(QtCore.QRect(40, 330, 380, 30))
        self.trainsvm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.trainsvm.setObjectName("trainsvm")
        #-----------------------------
        self.trainsvm.clicked.connect(self.svmdef)
        #-----------------------------




        self.browse = QtWidgets.QToolButton(self.tab_2)
        self.browse.setGeometry(QtCore.QRect(380, 200, 40, 30))
        self.browse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse.setObjectName("browse")

        #-----------------------------
        self.browse.clicked.connect(self.browsefile)
        #-----------------------------




        self.trainnb = QtWidgets.QPushButton(self.tab_2)
        self.trainnb.setGeometry(QtCore.QRect(40, 290, 380, 30))
        self.trainnb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"FangSong\";")
        self.trainnb.setObjectName("trainnb")
        self.trainnb.clicked.connect(self.nbdef)




        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 150, 261, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS PGothic\";")
        self.label.setObjectName("label")
        self.trainfile = QtWidgets.QLineEdit(self.tab_2)
        self.trainfile.setGeometry(QtCore.QRect(40, 200, 330, 30))
        self.trainfile.setObjectName("trainfile")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(500, 220, 140, 40))
        self.label_2.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(500, 260, 140, 40))
        self.label_3.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(500, 300, 140, 40))
        self.label_4.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.label_4.setObjectName("label_4")
        self.trainname = QtWidgets.QLabel(self.tab_2)
        self.trainname.setGeometry(QtCore.QRect(660, 220, 210, 40))
        self.trainname.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.trainname.setObjectName("trainname")
        self.traintime = QtWidgets.QLabel(self.tab_2)
        self.traintime.setGeometry(QtCore.QRect(660, 260, 210, 40))
        self.traintime.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.traintime.setObjectName("traintime")
        self.trainstatus = QtWidgets.QLabel(self.tab_2)
        self.trainstatus.setGeometry(QtCore.QRect(660, 300, 210, 40))
        self.trainstatus.setStyleSheet("color: rgb(255, 80, 112);\n"
"font: 14pt \"Eras Medium ITC\";")
        self.trainstatus.setObjectName("trainstatus")
        self.buttonaccuracy_2 = QtWidgets.QPushButton(self.tab_2)
        self.buttonaccuracy_2.setGeometry(QtCore.QRect(380, 430, 180, 30))
        self.buttonaccuracy_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"FangSong\";")

        self.buttonaccuracy_2.setObjectName("buttonaccuracy_2")
        self.buttonaccuracy_2.clicked.connect(self.graphdef)





        self.tabWidget.addTab(self.tab_2, "")
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
        self.label_5.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Welcome Admin</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("box", "Home"))
        self.trainrf.setText(_translate("box", "Random Forest"))
        self.trainsvm.setText(_translate("box", "Support Vector Machine"))
        self.browse.setText(_translate("box", "..."))
        self.trainnb.setText(_translate("box", "Naive Bayes"))
        self.label.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Training Dataset </span></p></body></html>"))
        self.trainfile.setPlaceholderText(_translate("box", "Upload Training File"))
        self.label_2.setText(_translate("box", "<html><head/><body><p><span style=\" font-weight:600;\">Algorithm:</span></p></body></html>"))
        self.label_3.setText(_translate("box", "<html><head/><body><p><span style=\" font-weight:600;\">Process Time:</span></p></body></html>"))
        self.label_4.setText(_translate("box", "<html><head/><body><p><span style=\" font-weight:600;\">Status:</span></p></body></html>"))
        self.trainname.setText(_translate("box", "<html><head/><body><p><span style=\" font-weight:600;\">non</span></p></body></html>"))
        self.traintime.setText(_translate("box", "<html><head/><body><p><span style=\" font-weight:600;\">non</span></p></body></html>"))
        self.trainstatus.setText(_translate("box", "<html><head/><body><p><span style=\" font-weight:600;\">non</span></p></body></html>"))
        self.buttonaccuracy_2.setText(_translate("box", "Accuracy Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("box", "Training Classifications"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = AdminHome()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
