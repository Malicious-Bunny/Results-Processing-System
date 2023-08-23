#! /bin/python3

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StudentView(object):
    def setupUi(self, StudentView):
        StudentView.setObjectName("StudentView")
        StudentView.resize(1118, 556)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(11)
        StudentView.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        StudentView.setWindowIcon(icon)
        self.StudentResultsTable = QtWidgets.QTableWidget(parent=StudentView)
        self.StudentResultsTable.setGeometry(QtCore.QRect(240, 90, 661, 181))
        self.StudentResultsTable.setObjectName("StudentResultsTable")
        self.StudentResultsTable.setColumnCount(0)
        self.StudentResultsTable.setRowCount(0)
        self.label = QtWidgets.QLabel(parent=StudentView)
        self.label.setGeometry(QtCore.QRect(510, 40, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.LogoutStudent = QtWidgets.QPushButton(parent=StudentView)
        self.LogoutStudent.setGeometry(QtCore.QRect(500, 460, 171, 25))
        self.LogoutStudent.setObjectName("LogoutStudent")
        self.EmailStudentResults_2 = QtWidgets.QPushButton(parent=StudentView)
        self.EmailStudentResults_2.setGeometry(QtCore.QRect(500, 330, 171, 25))
        self.EmailStudentResults_2.setObjectName("EmailStudentResults_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=StudentView)
        self.commandLinkButton.setGeometry(QtCore.QRect(510, 390, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.widget = QtWidgets.QWidget(parent=StudentView)
        self.widget.setGeometry(QtCore.QRect(10, 360, 381, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.StudentMAtricule = QtWidgets.QLineEdit(parent=self.widget)
        self.StudentMAtricule.setObjectName("StudentMAtricule")
        self.horizontalLayout.addWidget(self.StudentMAtricule)

        self.EmailStudentResults_2.clicked.connect(self.ViewResultsOnTable)
        
        self.commandLinkButton.setVisible(False)
        self.LogoutStudent.clicked.connect(lambda:self.StackedWidget.setCurrentWidget(self.StackedWidget.widget(0)))
        self.retranslateUi(StudentView)
        QtCore.QMetaObject.connectSlotsByName(StudentView)

    def retranslateUi(self, StudentView):
        _translate = QtCore.QCoreApplication.translate
        StudentView.setWindowTitle(_translate("StudentView", "Student View"))
        self.label.setText(_translate("StudentView", "Welcome Student"))
        self.LogoutStudent.setText(_translate("StudentView", "Logout"))
        self.EmailStudentResults_2.setText(_translate("StudentView", "View Results"))
        self.commandLinkButton.setText(_translate("StudentView", "Viewing..."))
        self.label_2.setText(_translate("StudentView", "Enter Your Matricule:"))
        self.StudentMAtricule.setPlaceholderText(_translate("StudentView", "ICTU..."))
    def ViewResultsOnTable(self):
        import sqlite3
        
        sqlite=sqlite3.connect('../Database/ResultSystem.db')
        
        cursor=sqlite.cursor()
        
        #Getting Student Name with matricule from Student Table
        cursor.execute("SELECT Name FROM Students WHERE Matircule=?",(self.StudentMAtricule.text(),))
        
        studentName=cursor.fetchone()
        
        cursor.execute("SELECT * FROM Results WHERE StudentName=?",(studentName[0],))
        
        StudentResults=cursor.fetchall()
        
        #Fill the table with the results
        
        self.StudentResultsTable.setColumnCount(len(StudentResults))
        self.StudentResultsTable.setRowCount(1)
        

        
        CourseName=[]
        
        
        self.StudentResultsTable.setHorizontalHeaderLabels(CourseName)
        
        #Fill the table with the results
        
        Grades=[]
        
        for grade in StudentResults:
            Grades.append(grade[2])
            CourseName.append(grade[1])
        
        #Set Headers
        print(CourseName)
        
        self.StudentResultsTable.setHorizontalHeaderLabels(CourseName)
        
        self.StudentResultsTable.setVerticalHeaderLabels(["Grades"])
        
        #Fill the table with the results
        
        
        for i in range(len(Grades)):
            self.StudentResultsTable.setItem(0,i,QtWidgets.QTableWidgetItem(str(Grades[i])))
            
        self.commandLinkButton.setVisible(True)
            
        
    
        

