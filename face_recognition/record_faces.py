import cv2
import numpy as np
import sqlite3
import os

conn = sqlite3.connect('database.db')
#if don't have dataset then create new one.
if not os.path.exists('./dataset'):
	os.makedirs('./dataset')

c = conn.cursor()

#using haarcascade method.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#using the front camera of my computer.
cap = cv2.VideoCapture(0)

uname = input("Enter your name: ")

#name of the person you've recorded the face.
c.execute('INSERT INTO users (name) VALUES (?)', (uname,))

uid = c.lastrowid

sampleNum = 0

while True:
	ret, frame = cap.read()
	if ret == True:	
		#convert to gray image.
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#detect face in the image
		faces = face_cascade.detectMultiScale(
	   gray,
	   scaleFactor=1.1,
	   minNeighbors=5)
		#(top,left) = (x,y) to w(width) and h(height).
		#store the recorded image.
		for (x,y,w,h) in faces:
			print("Run #37")
			sampleNum = sampleNum + 1
			#save the image to *.jpg .
			cv2.imwrite('dataset/User.' + str(uid) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
			#draw a red rectangle
			cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0), 2)
			#wait for keyboard.
		        cv2.waitKey(100)
		
		print(sampleNum)
		cv2.imshow('image',gray)
		cv2.waitKey(1)
		if sampleNum > 20:
			break

cap.release()
#save the name to db, but the face recognition images is stored in a dir.
conn.commit()
conn.close()
cv2.destroyAllWindows()
