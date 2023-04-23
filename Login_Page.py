import mysql.connector
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
def submit():
	user=username.get()
	passw=password.get()
	logindb(user,passw)
def logindb(usernme,passwd):
	con = mysql.connector.connect(
  	host="localhost",
  	user="root",
  	password="",
  	database="mini_project_2023"
  	)
	print("Connection Established Successfully")
	cur=con.cursor()
	savequery="select * from login"
	try:
		cur.execute(savequery)
		myresult=cur.fetchall()
		status=False
		for x in myresult:
			print(x[2],x[3])
			if x[2]==usernme and x[3]==passwd:
				status=True
				break
		if status:
			print("Login Successfull")
			cur.execute("select * from login where username=%s",(usernme,))
			myresults=cur.fetchall()
			for y in myresults:
				print(x[0])				
		else:
			print("Invalid Credentials")
	except:
	  print('An exception occurred')
	finally:
		if con:
			con.close()
			print("Resourses Released")
window = tk.Tk()
window.geometry("1080x520")
window.title("Login")
window.configure(bg="#FEFFB7")
login=tk.Label(window,text="Login",font=("Times New Roman",46),bg="#FEFFB7")
login.place(relx=0.5, rely=0.25, anchor="center")
myfont=("Times New Roman",20)
username_lbl=tk.Label(window,text="Username: ",font=("Times New Roman",24),bg="#FEFFB7")
username_lbl.place(relx=0.3,rely=0.5)
username=tk.Entry(window,font=(myfont))
username.place(relx=0.5,rely=0.5)

password_lbl=tk.Label(window,text="Password: ",font=("Times New Roman",24),bg="#FEFFB7")
password_lbl.place(relx=0.3,rely=0.6)
password=tk.Entry(window,font=(myfont),show="*")
password.place(relx=0.5,rely=0.6)

submit_btn=tk.Button(window,text="Submit",command=submit,bg="#B93030",fg="white",height=2,width=15)
submit_btn.place(relx=0.5,rely=0.8,anchor="center")

window.mainloop()