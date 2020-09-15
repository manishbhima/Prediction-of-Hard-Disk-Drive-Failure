# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Sentiment2019Copy\userhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_box(object):
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
        self.frame.setStyleSheet("background-image: url(:/newPrefix/C:/Users/SJ/Desktop/bg.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.Home, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 130, 261, 51))
        self.label.setObjectName("label")
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
        self.label.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Welcome User</span></p></body></html>"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = Ui_box()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
