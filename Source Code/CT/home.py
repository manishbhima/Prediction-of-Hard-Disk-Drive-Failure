# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Sentiment2019Copy\home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


from adminloginaction import AdminLoginCheck
from adminhome import AdminHome
from signup import Signup
from userloginaction import UserLoginCheck
from userhome import UserHome


class Home(object):

    def userlogin(self):
        try:
            print("ulogin")
            uid = self.uid.text()
            upwd = self.upwd.text()
            self.uid.setText("")
            self.upwd.setText("")
            ul = UserLoginCheck()
            res = ul.datacheck(uid, upwd)
            if res:
                self.showAlertBox("Alert", "Fill the Fields")
            elif UserLoginCheck.logincheck(uid, upwd):
                self.uu = QtWidgets.QMainWindow()
                self.uui = UserHome()
                self.uui.setupUi(self.uu)
                self.uu.show()
                print('userhome')
           
                

            else:
                self.showAlertBox("Login Alert", "Login Fail")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def adminlogin(self):
        print("adminlogin")
        auidvar = self.aid.text()
        apwdvar = self.apwd.text()
        self.aid.setText("")
        self.apwd.setText("")
        al = AdminLoginCheck()
        res = al.datacheck(auidvar, apwdvar)
        if res:
            self.showAlertBox("Alert", "Fill the Fields")
        elif AdminLoginCheck.logincheck(auidvar, apwdvar):
            self.u = QtWidgets.QMainWindow()
            self.ui = AdminHome()
            self.ui.setupUi(self.u)
            self.u.show()
            

        else:
            self.showAlertBox("Login Alert", "Login Fail")

    def signup(self):
    
        try:
            print("signup")
            rname = self.rname.text()
            remail = self.remail.text()
            rph = self.rph.text()
            rpwd = self.rpwd.text()

            Signup.store(rname,remail,rph,rpwd)

            self.remail.setText("")
            self.rpwd.setText("")
            self.rph.setText("")
            self.rname.setText("")
            self.showAlertBox("Registration", "Registration Success")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


            
    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 585)
        Dialog.setStyleSheet("background-color: rgb(28, 79, 94);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 721, 591))
        self.tabWidget.setStyleSheet("background-color: rgb(28, 79, 94);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 730, 570))
        self.frame.setStyleSheet("border-image: url(March6_2018-1024x683.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.apwd = QtWidgets.QLineEdit(self.tab_4)
        self.apwd.setGeometry(QtCore.QRect(230, 260, 290, 40))
        self.apwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.apwd.setText("")
        self.apwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apwd.setObjectName("apwd")
        self.aid = QtWidgets.QLineEdit(self.tab_4)
        self.aid.setGeometry(QtCore.QRect(230, 210, 290, 40))
        self.aid.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.aid.setText("")
        self.aid.setObjectName("aid")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(280, 140, 191, 61))
        self.label.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 650, 81))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.alogin = QtWidgets.QPushButton(self.tab_4)
        self.alogin.setGeometry(QtCore.QRect(230, 310, 120, 40))
        self.alogin.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.alogin.setObjectName("alogin")
        #-----------------------------------------------
        self.alogin.clicked.connect(self.adminlogin)
        #-----------------------------------------------

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 650, 81))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.ulogin = QtWidgets.QPushButton(self.tab_2)
        self.ulogin.setGeometry(QtCore.QRect(230, 320, 120, 40))
        self.ulogin.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.ulogin.setObjectName("ulogin")
        #-----------------------------------------------
        self.ulogin.clicked.connect(self.userlogin)
        #-----------------------------------------------

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(270, 150, 191, 61))
        self.label_3.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label_3.setObjectName("label_3")
        self.upwd = QtWidgets.QLineEdit(self.tab_2)
        self.upwd.setGeometry(QtCore.QRect(230, 270, 290, 40))
        self.upwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.upwd.setText("")
        self.upwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.upwd.setObjectName("upwd")
        self.uid = QtWidgets.QLineEdit(self.tab_2)
        self.uid.setGeometry(QtCore.QRect(230, 220, 290, 40))
        self.uid.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.uid.setText("")
        self.uid.setObjectName("uid")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.rph = QtWidgets.QLineEdit(self.tab_3)
        self.rph.setGeometry(QtCore.QRect(250, 280, 290, 40))
        self.rph.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.rph.setText("")
        self.rph.setObjectName("rph")
        self.rname = QtWidgets.QLineEdit(self.tab_3)
        self.rname.setGeometry(QtCore.QRect(250, 230, 290, 40))
        self.rname.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.rname.setText("")
        self.rname.setObjectName("rname")
        self.remail = QtWidgets.QLineEdit(self.tab_3)
        self.remail.setGeometry(QtCore.QRect(250, 330, 290, 40))
        self.remail.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.remail.setText("")
        self.remail.setObjectName("remail")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 650, 81))
        self.label_7.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.ulogin_2 = QtWidgets.QPushButton(self.tab_3)
        self.ulogin_2.setGeometry(QtCore.QRect(250, 430, 120, 40))
        self.ulogin_2.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.ulogin_2.setObjectName("ulogin_2")
        #-----------------------------------------------
        self.ulogin_2.clicked.connect(self.signup)
        #-----------------------------------------------


        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(290, 160, 221, 61))
        self.label_4.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label_4.setObjectName("label_4")
        self.rpwd = QtWidgets.QLineEdit(self.tab_3)
        self.rpwd.setGeometry(QtCore.QRect(250, 380, 290, 40))
        self.rpwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.rpwd.setText("")
        self.rpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rpwd.setObjectName("rpwd")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.apwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.aid.setPlaceholderText(_translate("Dialog", "Enter Login ID"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Admin Login</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#e30c3b;\">Prediction of Hard Disk Drive Failure</span></p></body></html>"))
        self.alogin.setText(_translate("Dialog", "Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Admin"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#e30c3b;\">Prediction of Hard Disk Drive Failure</span></p></body></html>"))
        self.ulogin.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">User Login</span></p></body></html>"))
        self.upwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.uid.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "User"))
        self.rph.setPlaceholderText(_translate("Dialog", "Enter Contact"))
        self.rname.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.remail.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#e30c3b;\">Prediction of Hard Disk Drive Failure</span></p></body></html>"))
        self.ulogin_2.setText(_translate("Dialog", "Register"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">User Registration</span></p></body></html>"))
        self.rpwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "User Signup"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
