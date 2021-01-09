
from gtts import gTTS 
from playsound import playsound
import os


mytext = 'Hello Rohit, Get well soon. Write your text whixh you want to concert into voice.'
mp3_file = "/home/developer/Desktop/output.mp3"

# Language we want to use 
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save(mp3_file) 

# You can play using two way, please use once at a time:-  
# 1
# os.system("start output.mp3")
# This playsound work for me in ubuntu.
# 2  
playsound(mp3_file)