#! /bin/python3

from PyQt6 import QtCore, QtGui, QtWidgets

from AdminView import *

class Ui_AdminLogin(object):
            
    def setupUi(self, AdminLogin):
        
        if not AdminLogin.objectName():
            AdminLogin.setObjectName(u"AdminLogin")
        
        AdminLogin.setObjectName("AdminLogin")
        AdminLogin.resize(745, 515)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        AdminLogin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AdminLogin.setWindowIcon(icon)
        AdminLogin.setStyleSheet("background-color: qlineargradient(x1:3, y1:0, x2:0, y2:0, stop:0 #E57352, stop:1 #240C4A);\n"
        "")
        self.label = QtWidgets.QLabel(parent=AdminLogin)
        self.label.setGeometry(QtCore.QRect(300, 60, 181, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/vibrent_8.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=AdminLogin)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=AdminLogin)
        self.label_4.setGeometry(QtCore.QRect(300, 270, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;\n"
"\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=AdminLogin)
        self.pushButton.setGeometry(QtCore.QRect(350, 460, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(parent=AdminLogin)
        self.frame.setGeometry(QtCore.QRect(180, 310, 411, 91))
        self.frame.setStyleSheet("background-color: #E57352;\n"
"\n"
"color:black;\n"
"\n"
"\n"
"\n"
"border-radius:9px;")
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"border-radius:1px;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:white;\n"
"background-color:white;\n"
"border-radius:1px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"border-radius:1px;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
"border-radius:1px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        
        self.pushButton.clicked.connect(self.VerifyAdminLogin)

        self.retranslateUi(AdminLogin)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)
        
    def VerifyAdminLogin(self):
        print("Login")
        name=self.lineEdit.text()
        password=self.lineEdit_2.text()
        
        if name=="admin" and password=="admin":
                self.adminview=QtWidgets.QWidget()
                self.ui=Ui_AdminView()
                self.ui.setupUi(self.adminview)
                self.adminview.show()
        else:
                QtWidgets.QMessageBox.warning(self.lineEdit,"Error","Wrong Credentials")
        
        
      
    def retranslateUi(self, AdminLogin):
        _translate = QtCore.QCoreApplication.translate
        AdminLogin.setWindowTitle(_translate("AdminLogin", "Login"))
        self.label_2.setText(_translate("AdminLogin", "Welcome Admin"))
        self.label_4.setText(_translate("AdminLogin", "Enter Your Info to login"))
        self.pushButton.setText(_translate("AdminLogin", "Login"))
        self.label_3.setText(_translate("AdminLogin", "Name:"))
        self.lineEdit.setPlaceholderText(_translate("AdminLogin", "Name"))
        self.label_5.setText(_translate("AdminLogin", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("AdminLogin", "Password"))

     

