#!/usr/bin/python
import serial
import time
import smtplib
import os,sys as sis
#import winsound
#import MySQLdb
import speech_recognition as sr
import facerecognition

'''ArduinoSerial = serial.Serial('com3',9600)
ArduinoSerial1 = serial.Serial('com4',9600)'''
time.sleep(2)
t = 9897550614153
r = 26390579686429
s = 73669285398244
u = 73669285449134

while 1:
        print ("Enter your choice")
        print ("1. For RFID card detection")
        print ("2. For dual security using face Recognition")
        print ("3. Exit")
        x = input()
        if(x=='1'):
                print ("")
                print ("Please present your RFID card")
                y= int(ArduinoSerial1.readline(),16)
           
                if (y == t):
                        print ("RFID found : Welcome Rishabh, Your ID is",y)
                        ArduinoSerial.write('1')
                        print ("Gate Unlocked")
                        time.sleep(1)
                        ArduinoSerial.write('0')
                        
                
                elif (y == r):
                        print ("RFID found :Welcome Saurabh, Your ID is",y)
                        ArduinoSerial.write('1')
                        print ("Gate Unlocked")
                        time.sleep(1)
                        ArduinoSerial.write('0')
                
                else:
                        print ("RFID Not found ")
                        winsound.Beep(1000,2000)
        if(x=='2'):
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
                y=y.lower()'''
                y='hello'
                if(y=='hello'):
                        print ("Yaay!!! Now it's time for face detection")
                        a = facerecognition.crt()
                        if a==1:
                                print ("Your Face is recognised!!!!")
                                print ("Welcome Home!!!")
                                #ArduinoSerial.write('1')
                                print ("Gate Unlocked")
                                time.sleep(3)
                        elif a==0:
                                print ("Face is not recognized")
        if(x=='3'):
                exit()
