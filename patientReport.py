import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sqlite3
import mysql.connector 


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Patient Medical Report'
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        nameLabel = QLabel('Patient Name:', self)
        nameLabel.move(50, 50)

        self.nameInput = QLineEdit(self)
        self.nameInput.move(200, 50)

        getReportButton = QPushButton('Get Report', self)
        getReportButton.setToolTip('Get Patient Medical Report')
        getReportButton.move(200, 100)
        getReportButton.clicked.connect(self.showReport)

        self.reportOutput = QTextEdit(self)
        self.reportOutput.setGeometry(50,150,500,300)

        self.show()

    def showReport(self):
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        name = self.nameInput.text()

        c.execute("SELECT * FROM patient WHERE name=:name", {'name': name})
        patientData = c.fetchone()

        if patientData:
            report = f"Patient Name: {patientData[0]}\nAge: {patientData[1]}\nGender: {patientData[2]}\nMedical History: {patientData[3]}\nDiagnosis: {patientData[4]}"
            self.reportOutput.setText(report)
        else:
            self.reportOutput.setText("No patient found with that name.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
