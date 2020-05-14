from gtts import gTTS
import sqlite3
import os
import time
import shutil

conn = sqlite3.connect(r'database/smartdata.db')

c = conn.cursor()

sql = "SELECT alphabet,word_name from words"

c.execute(sql)

result = c.fetchall()

print(result)

for output in result:
    get = os.getcwd()
    location = "audio"
    path = os.path.join(get,location,output[0])
    #print("path - ",path)
    
    if(os.path.isdir(path)):
       shutil.rmtree(path)
    #print("else part")

for output in result:
    location = "audio"
    path = os.path.join(location,output[0])
    torf = os.path.isdir(path)
    if(torf == False):
       os.mkdir(path)
    filename = 'audio' + '/' + output[0] + '/' + output[1].lower() + '.mp3'
    #print(output[0])
    print("filename - ",filename)

    language = 'en'
    # use slow = False for fast pronounce of word
    # use slow = True for slow pronounce of word
    obj = gTTS(text=output[1], lang=language, slow = True)

    obj.save(filename)
