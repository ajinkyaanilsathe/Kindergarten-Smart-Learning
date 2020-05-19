
from tkinter import *
from tkinter import simpledialog
import mysql.connector
from tkinter import messagebox


def validateUser():
	print("validate user")

	dbEntryEmail = entryEmail.get()
	dbEntryPassword = entryPassword.get()

	#print(dbEntryEmail)
	#print(dbEntryPassword)

	mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="kindergarten"
    )

	if mysqldb.is_connected():
            print("Yes Connected to MySQL")

            mysqlcursor = mysqldb.cursor()
            sql = "SELECT password,account_valid FROM userinfo WHERE parent_email = %s"
            values = (dbEntryEmail, )
            mysqlcursor.execute(sql,values)
            outputs = mysqlcursor.fetchone()

            #print(outputs[0])
            
            if outputs[0] == dbEntryPassword :
            	if outputs[1] == 1 :
            		print("Registered User !!")
            	else:
            		print("Not Registered User.")
            		s = simpledialog.askstring("License Key","Please Enter you License key.")
            		print(s)
            		if s == 'FREEUSER':
            			sql = "UPDATE userinfo SET account_valid = 1 WHERE parent_email = %s"
            			values = (dbEntryEmail,)
            			mysqlcursor.execute(sql,values)
            			resultrow = mysqlcursor.rowcount
            			if resultrow == 1 :
            				print("Account Acticated")
            				messagebox.showinfo("Registration Info", "License Key Validation Sucessfull !!")

            else:
            	print("Wrong Password")
	#quit()
	return

root = Tk()
root.geometry("600x320")
root.title("KINDERGARTEN SMART LEARNING")

def displayCenter(makeCenter):
	windowWidth = makeCenter.winfo_reqwidth()
	windowHeight = makeCenter.winfo_reqheight()
	print("Width", windowWidth, "Height", windowHeight)

	# Gets both half the screen width/height and window width/height
	positionRight = int(makeCenter.winfo_screenwidth() / 3 - windowWidth / 4)
	positionDown = int(makeCenter.winfo_screenheight() / 3 - windowHeight / 4)

	# Positions the window in the center of the page.
	makeCenter.geometry("+{}+{}".format(positionRight, positionDown))


displayCenter(root)

labelLogin = Label(root, text="Welcome to Kindergarten Smart Learning", font=("Times", 20, "bold italic"),fg="blue", relief=RAISED, wraplength=350, justify=CENTER)
labelLogin.grid(row=0,column=0,columnspan=2,padx=110,pady=20,ipadx=40,ipady=10)

####All the Labels
labelEmail = Label(root,text="Email Id : ",font=("Times",17,"bold"))
labelEmail.grid(row=1,column=0,padx=(30,10),pady=20)

entryEmail = Entry(root,width=50,font=("Helvica",10,"bold italic"),relief=GROOVE)
entryEmail.grid(row=1,column=1,ipadx=8,ipady=8)


labelPassword = Label(root,text="Password : ",font=("Times",17,"bold"))
labelPassword.grid(row=2,column=0,padx=(30,10),pady=20)

entryPassword = Entry(root,width=50,show='*',font=("Helvica",10,"bold italic"),relief=GROOVE)
entryPassword.grid(row=2,column=1,ipadx=8,ipady=8)


def regUser():
	print("register user")
	return




buttonSignup = Button(root, text="New User ? Sign Up Now..",font=("Times", 8, "bold"),command=regUser)
buttonSignup.grid(row=3,column=0)

buttonSignin = Button(root, text="Sign In",font=("Times",14,"bold"),command=validateUser)
buttonSignin.grid(row=3,column=1)

#####All the Entry Widgets


#entryPassword = Entry(frameLogin,width=50,font=("",10),relief=GROOVE)
#entryPassword.grid(row=1,column=1,pady=20,ipadx=8,ipady=8)










root.mainloop()
