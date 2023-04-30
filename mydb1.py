import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

# Get input from user for 10 doctors
doctors_data = []
for i in range(10):
    name = input("Enter doctor's name: ")
    shift_start_str = input("Enter shift start time (HH:MM:SS): ")
    shift_end_str = input("Enter shift end time (HH:MM:SS): ")
    doctors_data.append((name, shift_start_str, shift_end_str))

# Insert doctors' details into database
mycursor = mydb.cursor()
sql = "INSERT INTO doctors (name, shift_start, shift_end) VALUES (%s, %s, %s)"
mycursor.executemany(sql, doctors_data)
mydb.commit()