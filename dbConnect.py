import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import time
from gtts import gTTS
from playsound import playsound


def showall():

	conn = sqlite3.connect(r'database/smartdata.db')

	c = conn.cursor()

	sql = "SELECT * from words where alphabet='A'"

	c.execute(sql)

	result = c.fetchall()

	print(result)
	'''
	#display individual items from list
	for var in result:
		print(var[0])
		print(var[1])
		print(var[2])
		print(var[3])
		print(var[4])
		print(var[5])

		loc = 'images/A/apple.png'''
		
	image = Image.open(result[0][4])
	image = image.resize((150, 150), Image.ANTIALIAS) ## The (250, 250) is (height, width)
	load = ImageTk.PhotoImage(image)

	label1 = Label(root, text="aas")
	label2 = Label(root, image = load)
		#label2 = Label(root, image = load)
	label1.pack()
	label2.pack()
	playsound(result[0][5])

	conn.commit()

	conn.close()


 ####################################
root = Tk()


ButtonPlay = Button(root, text="Play Now", command=showall).pack()
#frame1 = Frame(root, width=700, height=700, background="bisque").grid(rows=2,column=1)

root.mainloop()