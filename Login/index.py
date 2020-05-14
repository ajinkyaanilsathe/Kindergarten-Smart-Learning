
from tkinter import *


class NewUser:


    def loginForm(self,root):
        #displayCenter()
        self.displayCenter()
        #To display the login window in the center of the screen

        labelLogin = Label(root, text="Welcome to Kindergarten Smart Learning", font=("Times", 20, "bold italic"),
                       fg="blue", relief=RAISED, wraplength=350, justify=CENTER, padx=10)
        labelLogin.pack(pady=10,ipadx=10)

        frameLogin = Frame(root)
        frameLogin.pack(padx=20,pady=20)

        ####All the Labels
        labelUserName = Label(frameLogin,text="Username ",font=("Times",17,"bold"))
        labelUserName.grid(row=0,column=0)
        labelPassword = Label(frameLogin,text="Password",font=("Times",17,"bold"))
        labelPassword.grid(row=1,column=0,pady=8)


        #####All the Entry Widgets
        entryUserName = Entry(frameLogin,width=50,font=("Helvica",10,"bold italic"),relief=GROOVE)
        entryUserName.grid(row=0,column=1,ipadx=8,ipady=8)

        entryPassword = Entry(frameLogin,width=50,font=("",10),relief=GROOVE)
        entryPassword.grid(row=1,column=1,pady=20,ipadx=8,ipady=8)
        #root.resizable(TRUE,TRUE)
        #######BUTTONS
        btnSubmit = Button(frameLogin,width=10,text="SUBMIT", command=lambda: self.alphabet(frameLogin),font=("Times",17,"bold"))
        btnSubmit.grid(row=2,column=1)
        btnNewUser = Button(frameLogin, text="Create New User ?", command=lambda: self.createUser(frameLogin),
                             font=("Times", 8, "bold"))
        btnNewUser.grid(row=3, column=0)

    def createUser(self,frameLogin):
        #frameLogin = frameLogin
        # label = Label(frameLogin,text="Hello ")
        # label.grid(row=3,column=1)


        print("HELLO ..ITS WORKING")
        top = Toplevel()
        top.title("SIGN UP FORM")
        top.geometry("1450x700")
        labelHeader = Label(top, text="Kindergarten Smart Learning Signup Form", font=("Times", 20, "bold italic"),
                           fg="blue", relief=RAISED, wraplength=350, justify=CENTER, padx=10,pady=5)
        labelHeader.place(x=0,y=0,relwidth=1)
        #labelHeader.pack()
        print("HELLO")
        frameChild = LabelFrame(top,text="Tell us About your child",font=("Times",18,"bold"),bd=3,labelanchor="n")
        #frameChild.place(x=20,y=100)
        frameChild.pack(pady=80,ipadx=100)
        #label2 = Label(frameChild,text="Frame created.")
        #label2.grid(row=0,column=0)

        #########LABELS##############
        labelName = Label(frameChild,text="Please enter the name ",font=("Times",15,"italic"),padx=20)
        labelName.grid(row=0,column=0,pady=20)
        labelAge = Label(frameChild, text="Please enter Age ", font=("Times", 15, "italic"), padx=20)
        labelAge.grid(row=1, column=0, pady=20)
        labelToy = Label(frameChild, text="Please enter your favourite toy ", font=("Times", 15, "italic"), padx=20)
        labelToy.grid(row=2, column=0, pady=20)
        labelFatherName = Label(frameChild, text="Please enter Father's name ", font=("Times", 15, "italic"), padx=20)
        labelFatherName.grid(row=3, column=0, pady=20)
        labelMotherName = Label(frameChild, text="Please enter Mother's name ", font=("Times", 15, "italic"), padx=20)
        labelMotherName.grid(row=4, column=0, pady=20)
        labelMobile = Label(frameChild, text="Please enter your Mobile Number ", font=("Times", 15, "italic"), padx=20)
        labelMobile.grid(row=5, column=0, pady=20)
        labelEmail = Label(frameChild, text="Please enter the email-id ", font=("Times", 15, "italic"), padx=20)
        labelEmail.grid(row=6, column=0, pady=20)


        ############ENTRY BOXES##########
        entryName = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"),relief=GROOVE)
        entryName.grid(row=0, column=1,ipady=6,padx=10)
        entryAge = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        entryAge.grid(row=1, column=1, ipady=6,padx=10)
        entryToy = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        entryToy.grid(row=2, column=1, ipady=6,padx=10)
        entryFatherName = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        entryFatherName.grid(row=3, column=1, ipady=6,padx=10)
        entryMotherName = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        entryMotherName.grid(row=4, column=1, ipady=6,padx=10)
        entryMobile = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        entryMobile.grid(row=5, column=1, ipady=6,padx=10)
        entryEmail = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        entryEmail.grid(row=6, column=1, ipady=6,padx=10)
        # entryUserName = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        # entryUserName.grid(row=6, column=1, ipady=6)
        # entryUserName = Entry(frameChild, width=50, font=("Helvica", 10, "bold italic"), relief=GROOVE)
        # entryUserName.grid(row=7, column=1, ipady=6)





        frameDetails = Frame(top)
        frameDetails.pack()
        label2 = Label(top,text="Frame created.",font=20,bd=4)
        label2.pack(side = LEFT,ipady=50)











    def displayCenter(self):
        # Gets the requested values of the height and widht.
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(root.winfo_screenwidth() / 3 - windowWidth / 4)
        positionDown = int(root.winfo_screenheight() / 3 - windowHeight / 4)

        # Positions the window in the center of the page.
        root.geometry("+{}+{}".format(positionRight, positionDown))








root = Tk()
root.geometry("600x320")
root.title("KINDERGARTEN SMART LEARNING")
newUser = NewUser()
newUser.loginForm(root)
root.mainloop()



# root = Tk()
# root.geometry("400x400")
#
# Label(root,text="hello trying").pack()



