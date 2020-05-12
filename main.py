from tkinter import *
import sqlite3
#from functions import *
from gtts import gTTS
from playsound import *
from PIL import ImageTk, Image


def display():

	conn = sqlite3.connect(r'database/smartdata.db')

	c = conn.cursor()

	sql = "SELECT * from words"

	c.execute(sql)

	result = c.fetchone()

    print(result)

	#display individual items from list
	'''for var in result:
		print(var[0])
		print(var[1])
		print(var[2])
		print(var[3])

	#print all result together
	#print(result)

	L1 = Label(frame, text=var[0]).grid(rows=3,column=1)
	L2 = Label(frame, text=var[1]).grid(rows=4,column=1)
	L3 = Label(frame, text=var[2]).grid(rows=5,column=1)
	L4 = Label(frame, text=var[3]).grid(rows=6,column=1)

	img = ImageTk.PhotoImage(Image.open(var[4]))
	L5 = Label(frame, image = img).grid(rows=7,column=1)

	playsound(var[5])'''

	conn.commit()

	conn.close()

root = Tk()
root.title("Kindergarten Smart Learning")

frame = Frame(root).grid(rows=1,column=1)

Button1 = Button(frame, text="Click Me", command=display).grid(rows=2,column=1)

root.mainloop()

