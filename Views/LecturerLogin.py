#! /bin/python3

from PyQt6 import QtCore, QtGui, QtWidgets

from Lecturerview import Ui_LecturerFillResults

class Ui_LecturerLogin(object):
    def setupUi(self, LecturerLogin):
        LecturerLogin.setObjectName("LecturerLogin")
        LecturerLogin.resize(745, 515)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        LecturerLogin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LecturerLogin.setWindowIcon(icon)
        LecturerLogin.setStyleSheet("background-color: qlineargradient(x1:3, y1:0, x2:0, y2:0, stop:0 #E57352, stop:1 #240C4A);\n"
"")
        self.label = QtWidgets.QLabel(parent=LecturerLogin)
        self.label.setGeometry(QtCore.QRect(300, 60, 181, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/vibrent_1.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=LecturerLogin)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=LecturerLogin)
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
        self.pushButton = QtWidgets.QPushButton(parent=LecturerLogin)
        self.pushButton.setGeometry(QtCore.QRect(350, 460, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(parent=LecturerLogin)
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
        
        self.pushButton.clicked.connect(self.LecturerLogin)

        self.retranslateUi(LecturerLogin)
        QtCore.QMetaObject.connectSlotsByName(LecturerLogin)

    def LecturerLogin(self):
        import sqlite3
        sqlite=sqlite3.connect("../Database/ResultSystem.db")
        
        cursor=sqlite.cursor()
        name=self.lineEdit.text()
        code=self.lineEdit_2.text()
        level=self.lineEdit_3.text()
        try:
                cursor.execute("SELECT * FROM Courses WHERE Lecturer=? AND Code=? AND Level=?",(name,code,level))
        except Exception as e:
                print(e)
                QtWidgets.QMessageBox.warning(self,"Error","Error Occured")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
        self.Lecturerview=QtWidgets.QWidget()
        self.ui=Ui_LecturerFillResults()
        self.ui.setupUi(self.Lecturerview)
        self.Lecturerview.show()
    def retranslateUi(self, LecturerLogin):
        _translate = QtCore.QCoreApplication.translate
        LecturerLogin.setWindowTitle(_translate("LecturerLogin", "Login"))
        self.label_2.setText(_translate("LecturerLogin", "Welcome Lecturer"))
        self.label_4.setText(_translate("LecturerLogin", "Enter Your Info to login"))
        self.pushButton.setText(_translate("LecturerLogin", "Login"))
        self.label_3.setText(_translate("LecturerLogin", "Name:"))
        self.lineEdit.setPlaceholderText(_translate("LecturerLogin", "Name"))
        self.label_5.setText(_translate("LecturerLogin", "Course"))
        self.lineEdit_2.setPlaceholderText(_translate("LecturerLogin", "Course Name"))
        self.label_6.setText(_translate("LecturerLogin", "Level"))
        self.lineEdit_3.setPlaceholderText(_translate("LecturerLogin", "Level 1, Level 2..."))

