#! /bin/python3


from PyQt6 import QtCore, QtGui, QtWidgets

from StudentView import Ui_StudentView

class Ui_StudentLogin(object):
    def setupUi(self, StudentLogin):
        StudentLogin.setObjectName("StudentLogin")
        StudentLogin.resize(745, 515)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        StudentLogin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        StudentLogin.setWindowIcon(icon)
        StudentLogin.setStyleSheet("background-color: qlineargradient(x1:3, y1:0, x2:0, y2:0, stop:0 #E57352, stop:1 #240C4A);\n"
"")
        self.label = QtWidgets.QLabel(parent=StudentLogin)
        self.label.setGeometry(QtCore.QRect(300, 60, 181, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/vibrent_21.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=StudentLogin)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=StudentLogin)
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
        self.pushButton = QtWidgets.QPushButton(parent=StudentLogin)
        self.pushButton.setGeometry(QtCore.QRect(350, 460, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(parent=StudentLogin)
        self.frame.setGeometry(QtCore.QRect(180, 310, 411, 123))
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
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"border-radius:1px;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:white;\n"
"border-radius:1px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)

        #Go back to LandingPage
        
        #increase button size
        
        self.pushButton.clicked.connect(self.SuccessfulLogin)
        
        self.retranslateUi(StudentLogin)
        QtCore.QMetaObject.connectSlotsByName(StudentLogin)
    def SuccessfulLogin(self):
        import sqlite3
        sqlite=sqlite3.connect("../Database/ResultSystem.db")
        
        cursor=sqlite.cursor()
        
        #Validate the user
        
        name=self.lineEdit.text()
        matricule=self.lineEdit_2.text()
        email=self.lineEdit_3.text()
        
        #Check if the user is in the database
        try:
                cursor.execute("SELECT * FROM Students WHERE Name=? AND Matircule=? AND Email=?",(name,matricule,email))
                
        except Exception as e:
                print(e)
                QtWidgets.QMessageBox.critical(self,"Error","An error occured while trying to login")
                
        
        self.pushButton.setText("Done")
        
        #Changing Mainwindow to StudentView
       
        self.Studentview=QtWidgets.QMainWindow()
        self.ui=Ui_StudentView()
        self.ui.setupUi(self.Studentview)
        self.Studentview.show()
        
        
        

    def retranslateUi(self, StudentLogin):
        _translate = QtCore.QCoreApplication.translate
        StudentLogin.setWindowTitle(_translate("StudentLogin", "Login"))
        self.label_2.setText(_translate("StudentLogin", "Welcome"))
        self.label_4.setText(_translate("StudentLogin", "Enter Your Info to login"))
        self.pushButton.setText(_translate("StudentLogin", "Login"))
        self.label_3.setText(_translate("StudentLogin", "Name:"))
        self.lineEdit.setPlaceholderText(_translate("StudentLogin", "Name"))
        self.label_5.setText(_translate("StudentLogin", "Matricule:"))
        self.lineEdit_2.setPlaceholderText(_translate("StudentLogin", "ICTU..."))
        self.label_6.setText(_translate("StudentLogin", "Email:"))
        self.lineEdit_3.setPlaceholderText(_translate("StudentLogin", "Email@ictuniversity.edu.cm"))


