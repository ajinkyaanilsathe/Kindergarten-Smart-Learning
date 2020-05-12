from tkinter import *
import sqlite3
from gtts import gTTS
from playsound import playsound


def display():

	conn = sqlite3.connect(r'database/smartdata.db')

	c = conn.cursor()

	sql = "SELECT * from words"
	c.execute(sql)

	result = c.fetchall();

	#display individual items from list
	for var in result:
		print(var[0])
		print(var[1])
		print(var[2])
		print(var[3])

		#print all result together
		#print(result)

	L1 = Label(frame, text=var[0]).grid(rows=0,column=1)
	L2 = Label(frame, text=var[1]).grid(rows=1,column=1)
	L3 = Label(frame, text=var[2]).grid(rows=2,column=1)
	L4 = Label(frame, text=var[3]).grid(rows=3,column=1)

	img = ImageTk.PhotoImage(Image.open(var[4]))
	L5 = Label(frame, image = img).grid(rows=4,column=1)
	playsound(var[4])

	conn.commit()

	conn.close()