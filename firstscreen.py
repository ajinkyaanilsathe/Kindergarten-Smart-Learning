
from tkinter import *
from tkinter import simpledialog
import mysql.connector
from tkinter import messagebox
import os
import sendmail


def validateUser(localwindow):
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
            emailExist = mysqlcursor.rowcount

            outputs = mysqlcursor.fetchone()
            print("row count",mysqlcursor.rowcount)
            if not entryEmail.get() or not entryPassword.get():
            	messagebox.showwarning("Retry", "Please fill in Email id and Password")
            	print("Fill Details for login")
            else:
	            if mysqlcursor.rowcount == -1:
	            	messagebox.showwarning("Retry", "Wrong Email Id. Please Register")
	            	print("Wrong Email")
	            else:
	            	#print(outputs[0])
		            if outputs[0] == dbEntryPassword:
		            	if outputs[1] == 1 :
		            		print("Registered User !!")
		            		#imageload.main()
		            		
		            		#exec(open('image-load-test.py').read())
		            		#regWindow.destroy()
		            		
		            		localwindow.destroy() #localwindow.withdraw()
		            		os.system('image-load.py')
		            		
		            		return True
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
		            	messagebox.showwarning("Retry", "Wrong Password. Retry") 
		            	print("Wrong Password")
				        

	#quit()
	return False


def completeReg():
	print("Completing Registration")
	mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="kindergarten")

	if mysqldb.is_connected():
		print("Yes Connected")
		mysqlcursor = mysqldb.cursor()
		if not entryName.get() or not entryAge.get() or not entryFatherName.get() or not entryMotherName.get() or not entryMobile.get() or not entryEmailid.get() or not entryPass.get():
			print("no submite to db")
			messagebox.showwarning("Retry", "Please fill all details. Retry")
		else:
			sql = "INSERT INTO userinfo (child_name,child_age,father_name,mother_name,parent_mobile,parent_email,password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
			values = (entryName.get(),entryAge.get(),entryFatherName.get(),entryMotherName.get(),entryMobile.get(),entryEmailid.get(),entryPass.get())
			mysqlcursor.execute(sql,values)
			outputs = mysqlcursor.fetchone()
			print(outputs)
			print(mysqlcursor.rowcount)
			sendmail.main(entryEmailid.get())
			messagebox.showinfo("Success", "Registration Successfull. Check Email")
			
			return True
	#return

def regUser():
	print("register user")
	global regWindow
	regWindow = Toplevel(root)

	regWindow.title("Register for Kindergarten Smart Learning")
	regWindow.geometry("700x470")
	displayCenter(regWindow)

	global entryName,entryAge,entryFatherName,entryMotherName,entryMobile,entryEmailid,entryPass

	labelHeader = Label(regWindow, text="Kindergarten Smart Learning Signup Form", font=("Times", 20, "bold italic"),fg="blue", relief=RAISED, wraplength=350, justify=CENTER, padx=10,pady=5)
	labelHeader.grid(row=0,column=0,columnspan=2,padx=160)

	labelName = Label(regWindow,text="Please enter the name of child :",font=("Times",15,"italic"))
	labelName.grid(row=1,column=0,pady=10)

	entryName = Entry(regWindow, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryName.grid(row=1, column=1,ipady=6,padx=5)

	labelAge = Label(regWindow,text="Please enter the age of child :",font=("Times",15,"italic"))
	labelAge.grid(row=2,column=0,pady=10)

	entryAge = Entry(regWindow, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryAge.grid(row=2, column=1,ipady=6,padx=5)

	labelFatherName = Label(regWindow,text="Plese enter child's father name :",font=("Times",15,"italic"))
	labelFatherName.grid(row=3,column=0,pady=10)

	entryFatherName = Entry(regWindow, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryFatherName.grid(row=3, column=1,ipady=6,padx=5)

	labelMotherName = Label(regWindow,text="Plese enter child's mother name :",font=("Times",15,"italic"))
	labelMotherName.grid(row=4,column=0,pady=10)

	entryMotherName = Entry(regWindow, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryMotherName.grid(row=4, column=1,ipady=6,padx=5)

	labelMobile = Label(regWindow,text="Plese enter parents mobile no :",font=("Times",15,"italic"))
	labelMobile.grid(row=5,column=0,pady=10)

	entryMobile = Entry(regWindow, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryMobile.grid(row=5, column=1,ipady=6,padx=5)

	labelEmailid = Label(regWindow,text="Plese enter parents email id :",font=("Times",15,"italic"))
	labelEmailid.grid(row=6,column=0,pady=10)

	entryEmailid = Entry(regWindow, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryEmailid.grid(row=6, column=1,ipady=6,padx=5)

	labelPass = Label(regWindow,text="Plese enter you password :",font=("Times",15,"italic"))
	labelPass.grid(row=7,column=0,pady=10)

	entryPass = Entry(regWindow, width=50, show='*', font=("Helvica", 10, "bold italic"),relief=GROOVE)
	entryPass.grid(row=7, column=1,ipady=6,padx=5)


	regButton = Button(regWindow, width=40, text="Complete Registration!", font=("Helvica", 12, "bold"),relief=GROOVE,justify=CENTER,command=lambda: [completeReg(),regWindow.destroy()])
	regButton.grid(row=8,column=0,columnspan=2,pady=10)

	return


root = Tk()
root.geometry("600x320")
root.title("KINDERGARTEN SMART LEARNING")
root.resizable(False, False)

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



buttonSignup = Button(root, text="New User ? Sign Up Now..",font=("Times", 8, "bold"),command=regUser)
buttonSignup.grid(row=3,column=0)

buttonSignin = Button(root, text="Sign In",font=("Times",14,"bold"),command=lambda: [validateUser(root)])
buttonSignin.grid(row=3,column=1)

#####All the Entry Widgets


#entryPassword = Entry(frameLogin,width=50,font=("",10),relief=GROOVE)
#entryPassword.grid(row=1,column=1,pady=20,ipadx=8,ipady=8)







root.mainloop()
