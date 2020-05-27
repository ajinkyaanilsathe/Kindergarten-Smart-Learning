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
import fiximage
import random
from threading import Thread
import os
 

def playNow():
    alphaGet = clickalpha.get()
    voiceGet = var.get()
    levelGet = clicklevel.get()
    fireLevel = 0
    insideif = 0

    result = ""

    if levelGet == 'Easy':
        fireLevel = 1
    elif levelGet == 'Medium':
        fireLevel = 2
    elif levelGet == 'Hard':
        fireLevel = 3

    conn = sqlite3.connect(r'database/smartdata.db')
    c = conn.cursor()

    if alphaGet == 'ALL' and levelGet == 'AUTO':
        insideif = 1
        #print("inside 1")
        sql = "SELECT * from words"
        c.execute(sql)
        result = c.fetchall()
    elif alphaGet == 'ALL' and (levelGet == 'Easy' or levelGet == 'Medium' or levelGet =='Hard'):
        insideif = 2
        #print("inside 2")
        #sql = "SELECT * from words WHERE level = ?" #fireLevel
        #print("fire levle is ",fireLevel)
        #values = (fireLevel, )
        c.execute("SELECT * from words WHERE level = :fire_level" , {'fire_level':fireLevel})
        result = c.fetchall()
    elif alphaGet != 'ALL' and levelGet == 'AUTO':
        insideif = 3
        #print("inside 3")
        #sql = "SELECT * FROM words WHERE alphabet = %s" #alphaGet
        #values = (fireLevel, )
        c.execute("SELECT * FROM words WHERE alphabet = :alpha_get",{'alpha_get':alphaGet})
        rowCount = c.rowcount
        result = c.fetchall()
    elif alphaGet != 'ALL' and levelGet != 'AUTO':
        insideif = 4
        #print("inside 4")
        #sql = "SELECT * FROM words WHERE alphabet = %s AND level = %s" #alphaGet , fireLevel
        #values = (alphaGet, fireLevel, )
        c.execute("SELECT * FROM words WHERE alphabet = :alpha_get AND level = :fire_level",{'alpha_get':alphaGet,'fire_level':fireLevel})
        rowCount = c.rowcount
        result = c.fetchall()
    

    
    print(result)
    global engine
    engine = pyttsx3.init()
    engine.setProperty('rate',90)
    engine.setProperty('volume', 0.9)

    if insideif == 1 or insideif == 2:
        for output in result:
            print(output[1])

            #pass_parameter = "'" + output[4] + "'"
            #print(pass_parameter)
            global image
            

            image2 = Image.open(output[4])
            image2 = image2.resize((650, 650), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            load2 = ImageTk.PhotoImage(image2)

            label1.config(text=output[1])
            label2.configure(image = load2)
            label2.image = load2

            audioThread = Thread(target=playWordSoundOne, args=(output[5], output[1], voiceGet))
            audioThread.start()

            mframe.update()
            mframe.after(4000)

    elif insideif == 3 or insideif ==4:
        #print("Row count is ",len(result))
        #print(result[0])
        #print(result[0][1])
        randomOrder = random.sample(range(len(result)), len(result))
        #print(randomOrder)
        for x in randomOrder:
            global image
            image2 = Image.open(result[x][4])
            image2 = image2.resize((650, 650), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            load2 = ImageTk.PhotoImage(image2)

            label1.config(text=result[x][1])
            label2.configure(image = load2)
            label2.image = load2

            print("--",result[x][5]," ",result[x][1]," ",voiceGet)

            #engine.startLoop(False)

            audioThread = Thread(target=playWordSoundTwo, args=(result[x][5], result[x][1], voiceGet))
            audioThread.start()
            #engine.runAndWait()

            #engine.endLoop()

            '''
            if voiceGet == 1:
                playsound(result[x][5])
            else:
                engine.say(result[x][1])
                engine.runAndWait()'''

            mframe.update()
            mframe.after(4000)
        


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

def takeTestNow():
    os.system('taketest.py')
    return

def fixAudio():
    print("Fixing Audio")
    fixsound.fixSoundNow()
    return

def fixImage():
    print("Fixing Image")
    fiximage.fixImageNow()
    return

def playWordSoundOne(audioOutput,word,choice):
    if choice == 1:
        playsound(audioOutput)
    else:
        engine.startLoop(False)
        engine.say(word)
        engine.iterate()
        # while engine.isBusy():
        #     time.sleep(1)
        #engine.runAndWait()
        engine.endLoop()

def playWordSoundTwo(audioPath,word,choice):
    if choice == 1:
        playsound(audioPath)
    else:
        engine.startLoop(False)
        engine.say(word)
        engine.iterate()
        # while engine.isBusy():
        #     time.sleep(1)
        #engine.runAndWait()
        engine.endLoop()

###########################################



root = Tk()
#root.geometry("800x600")
root.title("KINDERGARTEN SMART LEARNING")
root.attributes('-fullscreen', True)
root.state('zoomed')
root.bind("<Escape>", lambda e: e.widget.attributes('-fullscreen', False))

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

mframe = LabelFrame(root, text="Learn")
mframe.pack(fill="both",expand="yes")

button_autoplay = Button(mframe, text="Play Now", command=playNow)
button_autoplay.grid(row=1,column=0,columnspan="2",sticky="WE",padx=40)

button_play = Button(mframe, text="Save Configuration",command=getSave)
button_play.grid(row=1,column=2,columnspan="2",sticky="WE",padx=40)

button_play = Button(mframe, text="Stop Playing")
button_play.grid(row=1,column=4,columnspan="2",sticky="WE",padx=40)

takeTest = Button(mframe, text="Take Test",command=takeTestNow)
takeTest.grid(row=1,column=6,columnspan="2",sticky="WE",padx=10)

infoEsc = Label(mframe, text="Press Esc to Exit Full Screen", font=("Helvetica 14 italic"))
infoEsc.grid(row=1,column=8,columnspan="2",sticky="WE",padx=10)



var = IntVar()
var.set(1)

labelAlpha = Label(mframe, text="Select Alphabet : ", font=("Helvetica",14))
labelAlpha.grid(row=2,column=0,padx=10,pady=10)

clickalpha = StringVar()
clickalpha.set("ALL")
drop = OptionMenu(mframe, clickalpha,"ALL","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
drop.grid(row=2,column=1,sticky="WE",padx=10,pady=10)

labelLevel = Label(mframe, text="Select Level : ", font=("Helvetica",14))
labelLevel.grid(row=2,column=2,padx=10,pady=10)

clicklevel = StringVar()
clicklevel.set("AUTO")
dropLevel = OptionMenu(mframe, clicklevel,"AUTO","Easy","Medium","Hard")
dropLevel.grid(row=2,column=3,sticky="WE",padx=10,pady=10)

labelVoice = Label(mframe, text="Select Voice : ", font=("Helvetica",14))
labelVoice.grid(row=2,column=4,padx=10,pady=10)

radioButtonF = Radiobutton(mframe, text="Female Voice", variable=var, value=1)
radioButtonF.grid(row=2,column=5,sticky="WE",padx=10,pady=10)
radioButtonM = Radiobutton(mframe, text="Male Voice", variable=var, value=2)
radioButtonM.grid(row=2,column=6,sticky="WE",padx=10,pady=10)

labelTroubleShoot = Label(mframe, text="Troubleshoot : ", font=("Helvetica",14))
labelTroubleShoot.grid(row=2,column=7,sticky="WE",padx=10,pady=10)

fixAudioButton = Button(mframe, text="Fix Audio",command=fixAudio)
fixAudioButton.grid(row=2,column=8,sticky="WE",padx=10,pady=10)

fixImageButton = Button(mframe, text="Fix Image",command=fixImage)
fixImageButton.grid(row=2,column=9,sticky="WE",padx=10,pady=10)


global label1
label1 = Label(mframe, text="Let the teaching for toddler begin...",font=("Helvetica 30 bold"))
label1.grid(row=3,column=1,sticky="WE",columnspan=9,pady=10)

image = Image.open('images/A/atoz.png')
image = image.resize((650, 650), Image.ANTIALIAS) ## The (250, 250) is (height, width)
load = ImageTk.PhotoImage(image)

global label2
label2 = Label(mframe, image=load)
label2.grid(row=4,column=1,padx=30,columnspan=9,sticky="WE")

#mainframe = LabelFrame(root,text="frame").grid(row=1,column=1)

#engine = pyttsx3.init()
#engine.setProperty('rate',90)
#engine.setProperty('volume', 0.7)
#playrn()


#engine.say(result[0][1])
#engine.runAndWait()


root.mainloop()
