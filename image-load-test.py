import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import time
from gtts import gTTS
from playsound import playsound
import pyttsx3
from playbg import *


root = Tk()

mainframe = LabelFrame(root,text="frame").pack()

engine = pyttsx3.init()
engine.setProperty('rate',90)
engine.setProperty('volume', 0.7)
playrn()
conn = sqlite3.connect(r'database/smartdata.db')

c = conn.cursor()

sql = "SELECT * from words where alphabet='A'"

c.execute(sql)

result = c.fetchall()

print(result[0][4])
		
image = Image.open(result[0][4])
image = image.resize((150, 150), Image.ANTIALIAS) ## The (250, 250) is (height, width)
load = ImageTk.PhotoImage(image)

label1 = Label(root, text="aas")
label2 = Label(root, image = load)

label1.pack()
label2.pack()


#engine.say(result[0][1])
#engine.runAndWait()



root.mainloop()
