import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import time
from gtts import gTTS
from playsound import playsound
import pyttsx3
#from playbg import *
import time
import fixsound


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
def getSave():
    print("Configuration : ")
    print("Voice Gender : ",var.get())
    print("Alpha Select : ",clickalpha.get())
    print("Level : ",clicklevel.get())
    return

def fixAudio():
    print("Fixing Audio")
    fixsound.fixSoundNow()
    return



###########################################



root = Tk()
#root.geometry("800x600")
root.title("KINDERGARTEN SMART LEARNING")

def displayCenter(makeCenter):
    windowWidth = makeCenter.winfo_reqwidth()
    windowHeight = makeCenter.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(makeCenter.winfo_screenwidth() / 3 - windowWidth / 4)
    positionDown = int(makeCenter.winfo_screenheight() / 3 - windowHeight / 4)

    # Positions the window in the center of the page.
    makeCenter.geometry("+{}+{}".format(positionRight, positionDown-100))

displayCenter(root)

button_autoplay = Button(root, text="Play Now", command=playNow)
button_autoplay.grid(row=1,column=1)

button_play = Button(root, text="Save Configuration",command=getSave)
button_play.grid(row=1,column=2)

var = IntVar()
var.set(1)

radioButtonF = Radiobutton(root, text="Female Voice", variable=var, value=1)
radioButtonF.grid(row=1,column=3)
radioButtonM = Radiobutton(root, text="Male Voice", variable=var, value=2)
radioButtonM.grid(row=1,column=4)

clickalpha = StringVar()
clickalpha.set("ALL")

drop = OptionMenu(root, clickalpha,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
drop.grid(row=2,column=1)

clicklevel = StringVar()
clicklevel.set("AUTO")

dropLevel = OptionMenu(root, clickalpha,"Easy","Medium","Hard")
dropLevel.grid(row=2,column=2)

fixButton = Button(root, text="Fix Audio",command=fixAudio)
fixButton.grid(row=2,column=3)

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
