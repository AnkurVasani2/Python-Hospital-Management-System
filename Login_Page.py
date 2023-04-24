import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import datetime
def submit(username,password,window_frame,root):
    
    user = username.get()
    passw = password.get()
    status,name= logindb(user, passw)
    
    if status:
        window_frame.destroy()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        next_frame = tk.Frame(root, bg="#FEFFB7")
        next_frame.pack(fill="both", expand=True)

        welcome_label = tk.Label(next_frame, text=f"Welcome, {name}", font=("Times New Roman", 20), bg="#FEFFB7")
        welcome_label.pack(pady=50)
        welcome_label.place(relx=0.05,rely=0.05)

        users_btn=tk.Button(next_frame,text="Users",font=('Times New Roman',16),bg="#feffb7",fg="black",height=2,width=7)
        users_btn.pack()
        users_btn.place(relx=0.5,rely=0.05)

        patients_btn=tk.Button(next_frame,text="Search Patients[F2]",font=('Times New Roman',16),bg="#feffb7",fg="black",height=2,width=15)
        patients_btn.pack()
        patients_btn.place(relx=0.6,rely=0.05)
        def tick():
            current_time=datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')
            clock_label.config(text="Date & Time: "+ current_time)
            clock_label.after(1000,tick)
        

        clock_label=tk.Label(next_frame,font=("times new roman",16),background="#feffb7",fg="black")
        clock_label.pack()
        clock_label.place(relx=0.77,rely=0.07)
        tick()

        image_staff = tk.PhotoImage(file="D:\\Python_Design\\Staff.png")
        img_label_staff = tk.Label(next_frame, image=image_staff, bg="#FEFFB7", bd=2, relief="solid")
        img_label_staff.image = image_staff  # keep a reference to the image object
        img_label_staff.pack(side=LEFT,padx=15,pady=50)

        add_staff_btn=tk.Button(img_label_staff, text="Add Staff",bg="#B93030", fg="white", height=2, width=15)
        add_staff_btn.place(relx=0.5,rely=0.5,anchor="center")

        img_patient = tk.PhotoImage(file="D:\\Python_Design\\Patient.png")
        img_label_patient = tk.Label(next_frame, image=img_patient, bg="#FEFFB7", bd=2, relief="solid")
        img_label_patient.image = img_patient  # keep a reference to the image object
        img_label_patient.pack(side=LEFT,padx=15,pady=50)

        add_patient_btn=tk.Button(img_label_patient, text="Add Patient",bg="#B93030", fg="white", height=2, width=15)
        add_patient_btn.place(relx=0.5,rely=0.5,anchor="center")
        
        img_appo = tk.PhotoImage(file="D:\\Python_Design\\appointment.png")
        img_label_appo = tk.Label(next_frame, image=img_appo, bg="#FEFFB7", bd=2, relief="solid")
        img_label_appo.image = img_appo  # keep a reference to the image object
        img_label_appo.pack(side=LEFT,padx=15,pady=50)

        add_appo_btn=tk.Button(img_label_appo, text="Manage Appointment",bg="#B93030", fg="white", height=2, width=18)
        add_appo_btn.place(relx=0.5,rely=0.5,anchor="center")

        img_bill = tk.PhotoImage(file="D:\\Python_Design\\bills.png")
        img_label_bill = tk.Label(next_frame, image=img_bill, bg="#FEFFB7", bd=2, relief="solid")
        img_label_bill.image = img_bill  # keep a reference to the image object
        img_label_bill.pack(side=LEFT,padx=15,pady=50)

        accounts_btn=tk.Button(img_label_bill, text="Accounts",bg="#B93030", fg="white", height=2, width=15)
        accounts_btn.place(relx=0.5,rely=0.5,anchor="center")



        next_frame.update()
        next_frame.config(width=root.winfo_width(), height=root.winfo_height())




def logindb(usernme, passwd):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mini_project_2023"
    )
    print("Connection Established Successfully")
    cur = con.cursor()
    savequery = "select * from login"
    
    try:
        cur.execute(savequery)
        myresult = cur.fetchall()
        status = False
        name=""
        for x in myresult:
            print(x[2], x[3])
            if x[2] == usernme and x[3] == passwd:
                status = True
                name==x[0]
                break
        if status:
            print("Login Successfull")
            cur.execute("select * from login where username=%s", (usernme,))
            myresults = cur.fetchall()
            if myresults:
                name=myresults[0][0]                
            for y in myresults:
                print(y[0])
        else:
            print("Invalid Credentials")
    except:
        print('An exception occurred')
    finally:
        if con:
            con.close()
            print("Resourses Released")
    return status,name

def main_win():
    root = tk.Tk()
    root.geometry("1080x520")
    root.title("Login")

    window_frame = tk.Frame(root, width=1080, height=520, bg="#FEFFB7")
    window_frame.pack(expand=True)

    login = tk.Label(window_frame, text="Login", font=("Times New Roman", 46), bg="#FEFFB7")
    login.place(relx=0.5, rely=0.25, anchor="center")

    myfont = ("Times New Roman", 20)
    username_lbl = tk.Label(window_frame, text="Username: ", font=("Times New Roman", 24), bg="#FEFFB7")
    username_lbl.place(relx=0.3, rely=0.5)
    username = tk.Entry(window_frame, font=myfont)
    username.place(relx=0.5, rely=0.5)

    password_lbl = tk.Label(window_frame, text="Password: ", font=("Times New Roman", 24), bg="#FEFFB7")
    password_lbl.place(relx=0.3, rely=0.6)
    password = tk.Entry(window_frame, font=myfont, show="*")
    password.place(relx=0.5, rely=0.6)

    submit_btn = tk.Button(window_frame, text="Submit", command=lambda: submit(username, password,window_frame,root), bg="#B93030", fg="white", height=2, width=15)
    submit_btn.place(relx=0.5, rely=0.8, anchor="center")

    next_frame = tk.Frame(root, width=1080, height=520, bg="#FEFFB7")
    label = Label(next_frame, text="Welcome tothe next frame!")
    label.pack()
    next_frame.pack_forget()

    root.mainloop()


a=main_win()