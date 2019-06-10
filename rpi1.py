#!/usr/bin/python
import time
import commands, os
from gtts import gTTS 
import serial
import smtplib,ssl
import RPi.GPIO as GPIO
from firebase import firebase
import datetime
from time import sleep
import speech_recognition as sr
import facerecognition
GPIO.setmode(GPIO.BOARD)    
Motor1A = 16
Motor1B = 18
#Motor1E = 22    
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
FBConn= firebase.FirebaseApplication('https://home-database-96e2f.firebaseio.com/',None)
time = datetime.datetime.now()
flagr=0
flags=0

#function for text to speech
def TextToSpeech(text):
    mytext = text
    myobj = gTTS(text=mytext, lang='en', slow=False) 
    myobj.save("text.mp3") 
    os.system("mpg321 text.mp3")
    os.system("sudo rm -rf ~/Desktop/project/opencv/facerecg/text.mp3")
    return
def Speech():
   r = sr.Recognizer()                                                                                   
   with sr.Microphone() as source:
      audio = r.listen(source)   
      word = r.recognize_google(audio)
      return word
    
data = serial.Serial(
                    port='/dev/ttyS0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)
print (" ")
          
try:     
   while 1:
         s=Speech()
         if s=='open':
            #x=data.readline()#print the whole data at once
            #x=data.read()#print single data at once
            TextToSpeech ("Enter your choice 1. For RFID card detection2. For dual security using face Recognition 3. Exit") 
            #TextToSpeech ("1. For RFID card detection")
            #TextToSpeech ("2. For dual security using face Recognition")
            #TextToSpeech ("3. Exit")
            y = raw_input()
            if(y=='1'):
               TextToSpeech ("Place the card")
               x=data.read(12) 
                           
               print(x)
            
               if x==b'090073FD0E89':
                   print ("Card No - ",x)
                   TextToSpeech ("Welcome Rishabh")
                   #commands.getoutput('echo "welcome Rishab" | festival --tts')
                   print (" ")
                   if flagr==0:
                      GPIO.output(Motor1A,GPIO.HIGH)
                      GPIO.output(Motor1B,GPIO.LOW)
                      sleep(.25)
                      GPIO.output(Motor1A,GPIO.LOW)
                      GPIO.output(Motor1B,GPIO.LOW)
                      sleep(.25)
                      flagr=1
                      #GPIO.cleanup()
                      server = smtplib.SMTP('smtp.gmail.com',587)
                      server.starttls()
                      server.login("projectanand19@gmail.com","project@19")
                      server.sendmail("projectanand19@gmail.com","vishalgurdasani.ece19@jecrc.ac.in","Hi Admin, Rishabh has left your house")
                      #server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                      server.quit()
                      data_to_upload = {
                        'time': time,
                        'member':"Rishabh Anand left"
                        }
                      result = FBConn.post('/MyTestData/',data_to_upload)
                                              
                   elif flagr==1:
                      GPIO.output(Motor1A,GPIO.LOW)
                      GPIO.output(Motor1B,GPIO.HIGH)
                         
                      sleep(.25)
                      GPIO.output(Motor1A,GPIO.LOW)
                      GPIO.output(Motor1B,GPIO.LOW)
                      flagr=0  
                      #GPIO.cleanup()
                      server = smtplib.SMTP('smtp.gmail.com',587)
                      server.starttls()
                      server.login("projectanand19@gmail.com","project@19")
                      server.sendmail("projectanand19@gmail.com","vishalgurdasani.ece19@jecrc.ac.in","Hi Admin, Rishabh has entered your house")
                      #server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                      server.quit()
                      data_to_upload = {
                         'time': time,
                         'member':"Rishabh Anand entered"
                         }
                      result = FBConn.post('/MyTestData/',data_to_upload)
                                  
               elif x==b'4300779646E4':
                  print ("Card No - ",x)
                  TextToSpeech ("Welcome Shipra")
                  print (" ")
                  if flags==0:
                     GPIO.output(Motor1A,GPIO.HIGH)
                     GPIO.output(Motor1B,GPIO.LOW)
                         
                     sleep(.25)
                     GPIO.output(Motor1A,GPIO.LOW)
                     GPIO.output(Motor1B,GPIO.LOW)
                     sleep(.25)
                     flags=1
                     #GPIO.cleanup()
                     server = smtplib.SMTP('smtp.gmail.com',587)
                     server.starttls()
                     server.login("projectanand19@gmail.com","project@19")
                     server.sendmail("projectanand19@gmail.com","vishalgurdasani.ece19@jecrc.ac.in","Hi Admin, Shipra has left your house")
                     #server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                     server.quit()
                     data_to_upload = {
                        'time': time,
                        'member':"Shipra left"
                        }
                     result = FBConn.post('/MyTestData/',data_to_upload)
                           
                  elif flags==1:
                     
                      
                     GPIO.output(Motor1A,GPIO.LOW)
                     GPIO.output(Motor1B,GPIO.HIGH)
                     
                     sleep(.25)
                     GPIO.output(Motor1A,GPIO.LOW)
                     GPIO.output(Motor1B,GPIO.LOW)
                     flag=0  
                     #GPIO.cleanup()
                     server = smtplib.SMTP('smtp.gmail.com',587)
                     server.starttls()
                     server.login("projectanand19@gmail.com","project@19")
                     server.sendmail("projectanand19@gmail.com","vishalgurdasani.ece19@jecrc.ac.in","Hi Admin, Shipra has entered your house")
                     #server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                     server.quit()
                     data_to_upload = {
                        'time': time,
                        'member':"Shipra entered"
                        }
                     result = FBConn.post('/MyTestData/',data_to_upload)
                      
                   
               else:
                  TextToSpeech ("Wrong Card.....")
                  print (" ")        
               
                  #print x
            if(y=='2'):
                   '''r = sr.Recognizer()                                                                                   
                   with sr.Microphone() as source:                                                                       
                       print("Speak:")                                                                                   
                       audio = r.listen(source)   
                   try:
                       y = r.recognize_google(audio)
                       print("You said " + y)
                   except sr.UnknownValueError:
                       print("Could not understand audio")
                   except sr.RequestError as e:
                       print("Could not request results; {0}".format(e))
                   z=z.lower()'''
                   z='hello'
                   if(z=='hello'):
                      TextToSpeech ("Yaay!!! Now it's time for face detection")
                      a = facerecognition.crt()
                      if a==1:
                         TextToSpeech ("Your Face is recognised!!!!")
                         #print ("Welcome Home!!!")
                         TextToSpeech ("Gate Unlocked")
                         time.sleep(3)
                         TextToSpeech ("Welcome Rishabh")
                   #commands.getoutput('echo "welcome Rishab" | festival --tts')
                         print (" ")
                         if flagr==0:
                            GPIO.output(Motor1A,GPIO.HIGH)
                            GPIO.output(Motor1B,GPIO.LOW)
                            sleep(.25)
                            GPIO.output(Motor1A,GPIO.LOW)
                            GPIO.output(Motor1B,GPIO.LOW)
                            sleep(.25)
                            flagr=1
                            #GPIO.cleanup()
                            server = smtplib.SMTP('smtp.gmail.com',587)
                            server.starttls()
                            server.login("projectanand19@gmail.com","project@19")
                            server.sendmail("projectanand19@gmail.com","vishalgurdasani.ece19@jecrc.ac.in","Hi Admin, Rishabh has left your house")
                            #server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                            server.quit()
                            data_to_upload = {
                                      'time': time,
                                      'member':"Rishabh Anand left"
                                      }
                            result = FBConn.post('/MyTestData/',data_to_upload)
                                                                
                         elif flagr==1:
                            GPIO.output(Motor1A,GPIO.LOW)
                            GPIO.output(Motor1B,GPIO.HIGH)
                            sleep(.25)
                            GPIO.output(Motor1A,GPIO.LOW)
                            GPIO.output(Motor1B,GPIO.LOW)
                            flagr=0  
                            #GPIO.cleanup()
                            server = smtplib.SMTP('smtp.gmail.com',587)
                            server.starttls()
                            server.login("projectanand19@gmail.com","project@19")
                            server.sendmail("projectanand19@gmail.com","vishalgurdasani.ece19@jecrc.ac.in","Hi Admin, Rishabh has entered your house")
                            #server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                            server.quit()
                            data_to_upload = {
                                           'time': time,
                                           'member':"Rishabh Anand entered"
                                           }
                            result = FBConn.post('/MyTestData/',data_to_upload)
                      elif a==0:
                         TextToSpeech ("Face is not recognized")
            if(y=='3'):
                   exit()

except KeyboardInterrupt:
       data.close()
