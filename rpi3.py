#!/usr/bin/python
from firebase import firebase
import datetime
FBConn= firebase.FirebaseApplication('https://home-database-96e2f.firebaseio.com/',None)

while True:
    time = datetime.datetime.now()
    data_to_upload = {
        'time': time,
        'member':"rishabh anand"
        
        }
    result = FBConn.post('/MyTestData/',data_to_upload)
    print(result)
    
'''
import urllib
import cv2
import numpy as np

url='https://56.91.76.217:8080/shot.jpg'

while True:
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.unit8)
    img=cv2.imdecode(imgNp,-1)
    #if cv2.waitkey(10)
'''
