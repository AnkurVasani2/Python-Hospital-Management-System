import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sqlite3

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Doctor Appointment Schedule'
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        nameLabel = QLabel('Doctor Name:', self)
        nameLabel.move(50, 50)

        self.nameInput = QLineEdit(self)
        self.nameInput.move(200, 50)

        getScheduleButton = QPushButton('Get Schedule', self)
        getScheduleButton.setToolTip('Get Doctor Appointment Schedule')
        getScheduleButton.move(200, 100)
        getScheduleButton.clicked.connect(self.showSchedule)

        self.scheduleOutput = QTextEdit(self)
        self.scheduleOutput.setGeometry(50,150,500,300)

        self.show()

    def showSchedule(self):
        conn = sqlite3.connect('appointments.db')
        c = conn.cursor()

        doctorName = self.nameInput.text()

        c.execute("SELECT * FROM appointments WHERE doctor_name=:doctorName", {'doctorName': doctorName})
        appointmentData = c.fetchall()

        if appointmentData:
            schedule = "Date\t\tTime\t\tPatient Name\n"
            for appointment in appointmentData:
                schedule += f"{appointment[0]}\t{appointment[1]}\t{appointment[2]}\n"
            self.scheduleOutput.setText(schedule)
        else:
            self.scheduleOutput.setText("No appointments found for that doctor.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
