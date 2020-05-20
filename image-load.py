import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import time
from gtts import gTTS
from playsound import playsound
import pyttsx3
#from playbg import *
import time


def playNow():
    conn = sqlite3.connect(r'database/smartdata.db')
    c = conn.cursor()
    sql = "SELECT * from words"
    c.execute(sql)
    result = c.fetchall()
    i = 0
    for output in result:
        
        print(output[1])
        print(i)
        i = i+1

        playsound(output[5])
        #pass_parameter = "'" + output[4] + "'"
        #print(pass_parameter)
        global image
        image2 = Image.open(output[4])
        image2 = image2.resize((450, 450), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        load2 = ImageTk.PhotoImage(image2)

        label1.config(text=output[1])
        label2.configure(image = load2)
        label2.image = load2


        root.update()
        root.after(2000)
        

        #label2.grid(row=4,column=1)
        #label1.destroy()
        #label2.destroy()
        
        #time.sleep(2)



###########################################



root = Tk()

button_autoplay = Button(root, text="Auto Play Now", command=playNow)
button_autoplay.grid(row=1,column=1)

button_play = Button(root, text="Play Selected Option")
button_play.grid(row=1,column=2)

var = IntVar()

radioButtonF = Radiobutton(root, text="Female Voice", variable=var, value=1)
radioButtonF.grid(row=1,column=3)
radioButtonM = Radiobutton(root, text="Male Voice", variable=var, value=2)
radioButtonM.grid(row=1,column=4)

clicksem = StringVar()
clicksem.set("A")

drop = OptionMenu(root, clicksem, "B", "C", "D", "Z")
drop.grid(row=2,column=1)

global label1
label1 = Label(root, text="Helllooo Worldddddddddd", font=("Helvetica",14))
label1.grid(row=3,column=1)

image = Image.open('images/atoz.png')
image = image.resize((450, 450), Image.ANTIALIAS) ## The (250, 250) is (height, width)
load = ImageTk.PhotoImage(image)

global label2
label2 = Label(root, image=load)
label2.grid(row=4,column=1,padx=30,columnspan=3)

#mainframe = LabelFrame(root,text="frame").grid(row=1,column=1)

#engine = pyttsx3.init()
#engine.setProperty('rate',90)
#engine.setProperty('volume', 0.7)
#playrn()


#engine.say(result[0][1])
#engine.runAndWait()


root.mainloop()
