from gtts import gTTS
import os
import time

word1 = "Apple"
word2 = "Ball"

language = 'en'
# use slow = False for fast pronounce of word
# use slow = True for slow pronounce of word
obj1 = gTTS(text=word1, lang=language, slow = True)

obj1.save("apple.mp3")

os.system("start apple.mp3")

time.sleep(5)

obj2 = gTTS(text=word2, lang=language, slow = True)

obj2.save("ball.mp3")

os.system("start ball.mp3")
