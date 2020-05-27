from threading import Thread
from tkinter import *
from tkinter import messagebox
import sqlite3
import random
from PIL import Image, ImageTk
import sys
import pyttsx3
from gtts import gTTS

from playsound import playsound
import time




class Word:
    audio = ""
    name = ""
    image = ""

    def setAudio(self,audio):
        self.audio = audio

    def setWordName(self, name):
        self.name = name

    def setImage(self, image):
        self.image = image





class takeTest:
    global count
    count = 1;
    global counter
    counter = 1;
    global allData
    allData = []
    global label2


    def exam(self,root):
        self.displayCenter(root)
        print("Hello exam")
        labelName = Label(root,text="TAKE EXAM ",font=("",20),pady=5)
        labelName.pack()
        frameExam = Frame(root)
        frameExam.pack()
        labelText = Label(frameExam,text="Organize Tests for your child ",font=("Times",20))
        labelText.grid(row=0,column=1)

        levelOptions = [1,2,3]

        selectedLevel = IntVar()
        selectedLevel.set(1)



        optionMenuLevel= OptionMenu(frameExam,selectedLevel,*levelOptions)
        optionMenuLevel.grid(row=1,column=0,padx=40)

        # levels = type(selectedLevel.get())
        # print(selectedLevel.get())
        # print()
        stopButton = Button(frameExam,text="Stop Test",font=("Times",12),justify=CENTER,fg="blue",width=10,height=2,command=lambda: root.destroy())
        stopButton.grid(row=1,column=1,padx=40)

        buttonUserDefined = Button(frameExam,text="Take Test",font=("Times",12),justify=CENTER,fg="blue",width=10,height=2,command=lambda: self.createExam(frameExam,selectedLevel.get(),count))
        buttonUserDefined.grid(row=1,column=2)
        buttonAuto = Button(frameExam,text="Let us configure for you!!!",font=("Times",12),justify=CENTER,fg="red",width=20,height=2,command=lambda: self.customisedExam(frameExam,counter))
        buttonAuto.grid(row=2,column=1,pady=10)

    def __fetch_data_for_level(self, level):
        conn = sqlite3.connect(r'database/smartdata.db')
        c = conn.cursor()
        sql = "select alphabet,word_name,image_loc,audio_loc FROM words WHERE level = ?"
        values = (level,)
        #sql = ("select alphabet,word_name,image_loc,audio_loc FROM words WHERE level = 'level'")
        c.execute(sql,values)
        result = c.fetchall()
        print(result)
        for row in result:
            word = Word()
            word.setWordName(row[1])
            word.setImage(row[2])
            word.setAudio(row[3])
            allData.append(word)

    @staticmethod
    def __display_word(frameExam, word):
        # print("In load image")
        image2 = Image.open(word.image)
        # print("After image open")
        image2 = image2.resize((600, 600), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        # print("After image resize")
        load2 = ImageTk.PhotoImage(image2)
        print("After Photoimage")
        labelImage = Label(frameExam, image=load2)
        print("After labelImage")
        labelImage.image = load2
        print("After Assigning labelImage")
        labelImage.grid(row=3, column=1, padx=30, columnspan=3)
        print("After Assigning labelImage.grid")

    def createExam(self, frameExam, level, count):
        print(type(level))
        self.__fetch_data_for_level(level)
        print("Fetch data from db complete")
        while count <= 10:
            number = random.randrange(0, len(allData))
            word = allData[number]

            self.__display_word(frameExam,word)
            t1 = Thread(target=playWordSound, args=("audio/text.mp3",0.5))
            t1.start()

            t2 = Thread(target=playWordSound, args=(word.audio, 5))
            t2.start()

            count = count + 1
            frameExam.update()
            frameExam.after(8000)
            #sys.exit()
        messagebox.askyesno("AUDIO EXAM","Did he answered all the question correctly??")
        messagebox.askyesno("AUDIO EXAM","Want to take the test again???")


    def __fetch_data_from_db(self):
        conn = sqlite3.connect(r'database/smartdata.db')
        c = conn.cursor()
        sql = "select alphabet,word_name,image_loc,audio_loc FROM words;"

        c.execute(sql)

        result = c.fetchall()
        print(result)
        for row in result:
            word = Word()
            word.setWordName(row[1])
            word.setImage(row[2])
            word.setAudio(row[3])
            allData.append(word)





    def customisedExam(self,frameExam,counter):
        self.__fetch_data_from_db()
        print("Fetch data from db complete")
        while counter <= 10:
            number = random.randrange(0, len(allData))
            word = allData[number]

            self.__display_word(frameExam, word)
            t1 = Thread(target=playWordSound, args=("audio/text.mp3", 0.5))
            t1.start()

            t2 = Thread(target=playWordSound, args=(word.audio, 5))
            t2.start()

            counter = counter + 1
            frameExam.update()
            frameExam.after(8000)
            # sys.exit()
        messagebox.askyesno("AUDIO EXAM", "Did he answered all the question correctly??")
        messagebox.askyesno("AUDIO EXAM", "Want to take the test again???")


        print("This button is working")







    def displayCenter(self,root):
        # Gets the requested values of the height and widht.
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        print(width)
        print(height)
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        print("X = ",x)
        print("Y = ",y)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def playWordSound(audioPath, delay):
    time.sleep(delay)
    print("after sleep")
    playsound(audioPath)
    print("Playing sound")



# class Words:
#
#     def setAudio(self,audio):
#         return self.audio
#
#     def setWordName(self,name):
#         return  self.name
#
#     def setImage(self,image):
#         return self.image



root = Tk()
root.geometry("1300x800")
root.title("KINDERGARTEN SMART LEARNING")
newUser = takeTest()
newUser.exam(root)
##root.resizable(False, False)



root.mainloop()
