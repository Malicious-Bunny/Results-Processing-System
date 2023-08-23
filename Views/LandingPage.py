#! /bin/python3

from PyQt6 import QtCore, QtGui, QtWidgets

from StudentView import Ui_StudentView
from Lecturerview import Ui_LecturerFillResults
from AdminView import Ui_AdminView

from StudentLogin import Ui_StudentLogin
from LecturerLogin import Ui_LecturerLogin
from AdminLogin import Ui_AdminLogin

class Ui_LandingPage_2(object):
    def setupUi(self, LandingPage_2):
        LandingPage_2.setObjectName("LandingPage_2")
        LandingPage_2.resize(1304, 807)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LandingPage_2.setWindowIcon(icon)
        self.LandingPage = QtWidgets.QStackedWidget(parent=LandingPage_2)
        self.LandingPage.setGeometry(QtCore.QRect(-1, -1, 1341, 811))
        self.LandingPage.setStyleSheet("background-color: qlineargradient(x1:3, y1:0, x2:0, y2:0, stop:0 #E57352, stop:1 #240C4A);\n"
"color:white;\n"
"")
        self.LandingPage.setObjectName("LandingPage")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.line = QtWidgets.QFrame(parent=self.page)
        self.line.setGeometry(QtCore.QRect(660, 320, 118, 3))
        self.line.setStyleSheet("background-color:white;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(parent=self.page)
        self.label_4.setGeometry(QtCore.QRect(640, 580, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(13)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"border:none;\n"
"\n"
"background-color:none;")
        self.label_4.setObjectName("label_4")
        self.StudentLanding = QtWidgets.QToolButton(parent=self.page)
        self.StudentLanding.setGeometry(QtCore.QRect(360, 400, 161, 151))
        self.StudentLanding.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.StudentLanding.setStyleSheet("border-radius:50%;\n"
"\n"
"border:none;\n"
"\n"
"background-color:none;\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/vibrent_21.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.StudentLanding.setIcon(icon1)
        self.StudentLanding.setIconSize(QtCore.QSize(300, 300))
        self.StudentLanding.setObjectName("StudentLanding")
        self.LecturerLanding = QtWidgets.QToolButton(parent=self.page)
        self.LecturerLanding.setGeometry(QtCore.QRect(600, 400, 161, 151))
        self.LecturerLanding.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LecturerLanding.setStyleSheet("border-radius:50%;\n"
"\n"
"\n"
"border:none;\n"
"\n"
"background-color:none;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/vibrent_1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.LecturerLanding.setIcon(icon2)
        self.LecturerLanding.setIconSize(QtCore.QSize(300, 300))
        self.LecturerLanding.setObjectName("LecturerLanding")
        self.label_6 = QtWidgets.QLabel(parent=self.page)
        self.label_6.setGeometry(QtCore.QRect(610, 750, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"border:none;\n"
"\n"
"background-color:none;")
        self.label_6.setObjectName("label_6")
        self.AdminLanding = QtWidgets.QToolButton(parent=self.page)
        self.AdminLanding.setGeometry(QtCore.QRect(820, 400, 161, 151))
        self.AdminLanding.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AdminLanding.setStyleSheet("border-radius:50%;\n"
"\n"
"border:none;\n"
"\n"
"background-color:none;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/vibrent_8.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.AdminLanding.setIcon(icon3)
        self.AdminLanding.setIconSize(QtCore.QSize(300, 300))
        self.AdminLanding.setObjectName("AdminLanding")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(560, 240, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-weight:100px;\n"
"\n"
"border:none;\n"
"\n"
"background-color:none;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 201))
        self.label.setStyleSheet("background-color:#240C4A;\n"
"border: 3px solid #4B4453")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(parent=self.page)
        self.label_5.setGeometry(QtCore.QRect(880, 580, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(13)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"border:none;\n"
"\n"
"background-color:none;")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.page)
        self.label_3.setGeometry(QtCore.QRect(410, 580, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(13)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"border:none;\n"
"\n"
"background-color:none;")
        self.label_3.setObjectName("label_3")
        self.LandingPage.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.LandingPage.addWidget(self.page_2)
        
        self.AdminLanding.clicked.connect(self.showAdminLogin)
        self.StudentLanding.clicked.connect(self.ShowStudentLogin)
        self.LecturerLanding.clicked.connect(self.showLecturerLogin)
        
        self.retranslateUi(LandingPage_2)
        QtCore.QMetaObject.connectSlotsByName(LandingPage_2)
    def ShowStudentLogin(self):
        self.StudentLogin = QtWidgets.QWidget()
        self.ui = Ui_StudentLogin()
        self.ui.setupUi(self.StudentLogin)
        self.StudentLogin.show()
    def showLecturerLogin(self):
        self.LecturerLogin = QtWidgets.QWidget()
        self.ui = Ui_LecturerLogin()
        self.ui.setupUi(self.LecturerLogin)
        self.LecturerLogin.show()
    def showAdminLogin(self):
            self.AdminLogin=QtWidgets.QWidget()
            self.ui=Ui_AdminLogin()
            self.ui.setupUi(self.AdminLogin)
            self.AdminLogin.show()
    def retranslateUi(self, LandingPage_2):
        _translate = QtCore.QCoreApplication.translate
        LandingPage_2.setWindowTitle(_translate("LandingPage_2", "Form"))
        self.label_4.setText(_translate("LandingPage_2", "Lecturer"))
        self.StudentLanding.setText(_translate("LandingPage_2", "Student"))
        self.LecturerLanding.setText(_translate("LandingPage_2", "Lecturer"))
        self.label_6.setText(_translate("LandingPage_2", "MaliciousBunny © "))
        self.AdminLanding.setText(_translate("LandingPage_2", "Admin"))
        self.label_2.setText(_translate("LandingPage_2", "Choose Access Mode:"))
        self.label_5.setText(_translate("LandingPage_2", "Admin"))
        self.label_3.setText(_translate("LandingPage_2", "Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LandingPage_2 = QtWidgets.QWidget()
    ui = Ui_LandingPage_2()
    ui.setupUi(LandingPage_2)
    LandingPage_2.setWindowTitle("Landing Page")
    LandingPage_2.show()
    sys.exit(app.exec())
