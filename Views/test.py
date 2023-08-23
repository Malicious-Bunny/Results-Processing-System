#! /bin/python3

################################################################################
## Form generated from reading UI file 'AdminLoginCZeqwu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_AdminLogin(object):
    def setupUi(self, AdminLogin):
        if not AdminLogin.objectName():
            AdminLogin.setObjectName(u"AdminLogin")
        AdminLogin.resize(745, 515)
        font = QFont()
        font.setFamilies([u"Hack Nerd Font"])
        font.setPointSize(10)
        AdminLogin.setFont(font)
        icon = QIcon()
        icon.addFile(u":/resources/ict-university-461753.jpg", QSize(), QIcon.Normal, QIcon.Off)
        AdminLogin.setWindowIcon(icon)
        AdminLogin.setStyleSheet(u"background-color: qlineargradient(x1:3, y1:0, x2:0, y2:0, stop:0 #E57352, stop:1 #240C4A);\n"
"")
        self.label = QLabel(AdminLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 60, 181, 171))
        self.label.setPixmap(QPixmap(u":/resources/vibrent_8.png"))
        self.label_2 = QLabel(AdminLogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 20, 111, 16))
        font1 = QFont()
        font1.setFamilies([u"Hack Nerd Font"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: none;\n"
"\n"
"color:white;")
        self.label_4 = QLabel(AdminLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 270, 191, 17))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: none;\n"
"\n"
"color:white;")
        self.pushButton = QPushButton(AdminLogin)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 460, 80, 25))
        font2 = QFont()
        font2.setFamilies([u"Hack Nerd Font"])
        font2.setPointSize(11)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color:white;")
        self.frame = QFrame(AdminLogin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(180, 310, 411, 91))
        self.frame.setStyleSheet(u"background-color: #E57352;\n"
"\n"
"color:black;\n"
"\n"
"\n"
"\n"
"border-radius:9px;")
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Hack Nerd Font"])
        font3.setPointSize(12)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"\n"
"border-radius:1px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color:white;\n"
"background-color:white;\n"
"border-radius:1px;")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"\n"
"border-radius:1px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"background-color:white;\n"
"border-radius:1px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.retranslateUi(AdminLogin)
        self.pushButton.clicked.connect(self.VerifyAdminLogin)

        QMetaObject.connectSlotsByName(AdminLogin)
    # setupUi

    def VerifyAdminLogin(self):
        
        name=self.lineEdit.text()
        password=self.lineEdit_2.text()
        
        if name=="Admin" and password=="Admin":
            self.Adminview=QtWidgets.QWidget()
            self.ui-Ui_AdminView()
            self.ui.setupUi(self.AdminView)
            self.Adminview.show()
        else:
                QtWidgets.QMessageBox.warning(self.lineEdit,"Error","Wrong Name or Password")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
    def retranslateUi(self, AdminLogin):
        AdminLogin.setWindowTitle(QCoreApplication.translate("AdminLogin", u"Login", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("AdminLogin", u"Welcome Admin", None))
        self.label_4.setText(QCoreApplication.translate("AdminLogin", u"Enter Your Info to login", None))
        self.pushButton.setText(QCoreApplication.translate("AdminLogin", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("AdminLogin", u"Name:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("AdminLogin", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("AdminLogin", u"Password", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("AdminLogin", u"Password", None))
    # retranslateUi


if __name__=="__main__":
    #make UI
    import sys
    #make UI
    app=QApplication(sys.argv)
    Admin=QWidget()
    ui=Ui_AdminLogin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec())