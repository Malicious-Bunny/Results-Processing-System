#! /bin/python3
from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_LecturerFillResults(object):
    def setupUi(self, LecturerFillResults):
        LecturerFillResults.setObjectName("LecturerFillResults")
        LecturerFillResults.resize(1114, 866)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(12)
        LecturerFillResults.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ict-university-461753.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LecturerFillResults.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(parent=LecturerFillResults)
        self.label.setGeometry(QtCore.QRect(490, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(parent=LecturerFillResults)
        self.scrollArea.setGeometry(QtCore.QRect(9, 90, 1101, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1099, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1080, 0, 21, 521))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.StudentFillLecturer = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
        self.StudentFillLecturer.setGeometry(QtCore.QRect(0, 0, 1081, 521))
        self.StudentFillLecturer.setObjectName("StudentFillLecturer")
        self.StudentFillLecturer.setColumnCount(0)
        self.StudentFillLecturer.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.PublishLecturer = QtWidgets.QPushButton(parent=LecturerFillResults)
        self.PublishLecturer.setGeometry(QtCore.QRect(510, 650, 131, 31))
        self.PublishLecturer.setObjectName("PublishLecturer")
        self.LogOutLecturer = QtWidgets.QPushButton(parent=LecturerFillResults)
        self.LogOutLecturer.setGeometry(QtCore.QRect(520, 800, 111, 31))
        self.LogOutLecturer.setObjectName("LogOutLecturer")
        self.PublishLecturerSuccess = QtWidgets.QCommandLinkButton(parent=LecturerFillResults)
        self.PublishLecturerSuccess.setGeometry(QtCore.QRect(500, 720, 168, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PublishLecturerSuccess.setIcon(icon1)
        self.PublishLecturerSuccess.setObjectName("PublishLecturerSuccess")
        self.PublishLecturereFailed = QtWidgets.QCommandLinkButton(parent=LecturerFillResults)
        self.PublishLecturereFailed.setGeometry(QtCore.QRect(510, 720, 168, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PublishLecturereFailed.setIcon(icon2)
        self.PublishLecturereFailed.setObjectName("PublishLecturereFailed")
        self.widget = QtWidgets.QWidget(parent=LecturerFillResults)
        self.widget.setGeometry(QtCore.QRect(20, 650, 361, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.SelectCourseCombo = QtWidgets.QComboBox(parent=self.widget)
        self.SelectCourseCombo.setObjectName("SelectCourseCombo")
        self.horizontalLayout.addWidget(self.SelectCourseCombo)
        
        self.PublishLecturer.clicked.connect(self.PublishResults)
        
        self.PublishLecturereFailed.setVisible(False)
        self.PublishLecturerSuccess.setVisible(False)
        
        self.PopulateTableWithRows()
        
        self.FillCourseCombo()

        self.LogOutLecturer.clicked.connect(lambda:self.close())
        
        self.retranslateUi(LecturerFillResults)
        QtCore.QMetaObject.connectSlotsByName(LecturerFillResults)
    def PopulateTableWithRows(self):
        #Making a spreadsheet editor from QTableWidget so lecturers can fill in results
        
        import sqlite3
        
        sqlite=sqlite3.connect("../Database/ResultSystem.db")
        
        #Get the number of students in the database
        
        cursor=sqlite.cursor()
        
        
        cursor.execute("SELECT COUNT(*) FROM Students")
        
        studentNo=cursor.fetchone()
        
        #Get Student names and make them row headers
        
        cursor.execute("SELECT Name FROM Students")
        
        listOfStudents=cursor.fetchall()
        
        self.StudentFillLecturer.setRowCount(studentNo[0])
        self.StudentFillLecturer.setColumnCount(1)
        
        self.StudentFillLecturer.setHorizontalHeaderLabels(["Marks"])
        
        headers=[]
        
        for tupl in listOfStudents:
            headers.append(tupl[0])
        
        self.StudentFillLecturer.setVerticalHeaderLabels(headers)
        
        for i in range(studentNo[0]):
            for j in range(1):
                self.StudentFillLecturer.setItem(i,j,QtWidgets.QTableWidgetItem())

    def retranslateUi(self, LecturerFillResults):
        _translate = QtCore.QCoreApplication.translate
        LecturerFillResults.setWindowTitle(_translate("LecturerFillResults", "Lecturer View"))
        self.label.setText(_translate("LecturerFillResults", "Welcome Lecturer"))
        self.PublishLecturer.setText(_translate("LecturerFillResults", "Publish"))
        self.LogOutLecturer.setText(_translate("LecturerFillResults", "Log Out"))
        self.PublishLecturerSuccess.setText(_translate("LecturerFillResults", "Published"))
        self.PublishLecturereFailed.setText(_translate("LecturerFillResults", "Failed"))
        self.label_2.setText(_translate("LecturerFillResults", "Select Course:"))
    
    def FillCourseCombo(self):
        import sqlite3
        sqlite=sqlite3.connect("../Database/ResultSystem.db")
        
        cursor=sqlite.cursor()
        
        cursor.execute("SELECT Name FROM Courses")
        
        courses=cursor.fetchall()
        
        courselist=[]
        
        for course in courses:
            courselist.append(course[0])
            
        for course in courselist:
            self.SelectCourseCombo.addItem(course)
    
    def ConvertMarksToGrades(self,Mark):
        if Mark=="":
            Mark=0
        Mark=int(Mark)
        if(Mark>=80):
            return "A"
        elif(Mark>=70):
            return "B"
        elif(Mark>=60):
            return "C"
        elif(Mark>=50):
            return "D"
        elif(Mark>=40):
            return "E"
        elif(Mark>=30):
            return "F"
        else:
            return "U"
        
        
    
    def PublishResults(self):
        import sqlite3
        
        sqlite=sqlite3.connect("../Database/ResultSystem.db")
        
        cursor=sqlite.cursor()
        
        #Reading data from cells of QTableWidget
        
        listofmarks=[]
        
        for i in range(self.StudentFillLecturer.rowCount()):
            listofmarks.append(self.StudentFillLecturer.item(i,0).text())
        
        #Get the course name from the combo box
        
        course=self.courseName=self.SelectCourseCombo.currentText()
        
        #Get the students names from the row headers
        
        studentNames=[]
        
        for student in range(self.StudentFillLecturer.rowCount()):
            studentNames.append(self.StudentFillLecturer.verticalHeaderItem(student).text())
        
        #Fill the student names and marks in results table
        
        for i in range(len(studentNames)):
            print(studentNames[i],course,self.ConvertMarksToGrades(listofmarks[i]))
            cursor.execute("INSERT INTO Results (StudentName,Course,Grade) VALUES (?,?,?)",(studentNames[i],course,self.ConvertMarksToGrades(listofmarks[i])))

        
        cursor.close()
        sqlite.commit()
        sqlite.close()
        
        self.PublishLecturerSuccess.setVisible(True)


