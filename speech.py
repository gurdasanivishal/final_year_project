# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 


def TextToSpeech(text):
    mytext = text
    myobj = gTTS(text=mytext, lang='en', slow=False) 
    myobj.save("text.mp3") 
    os.system("mpg321 text.mp3")
    os.system("sudo rm -rf ~/Desktop/project/opencv/facerecg/text.mp3")
    

TextToSpeech("welcome to my world")   
    
    
    
