# importing the pyttsx library 
import pyttsx3 

# initialisation 
engine = pyttsx3.init() 

# set voice id to the key from os
#voice_id =

#set speed of playing word
engine.setProperty('rate',90)

# Use custom voice 
#converter.setProperty('voice', voice_id)

# Set volume 0-1 
engine.setProperty('volume', 0.7) 

word1 = 'Apple'
word2 = 'Ball'
# testing 
engine.say(word1) 
engine.say(word2) 
engine.runAndWait()


# to find out installed voices in computer
'''
voices = engine.getProperty('voices') 
  
for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) 
'''