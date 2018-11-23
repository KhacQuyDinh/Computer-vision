import numpy as np
import cv2

#codec problem
#-------------

#create VideoCapture object
#take video from the camera.
#cap = cv2.VideoCapture(0)

#take video from a file
cap = cv2.VideoCapture('video.mp4')

#Define the codec and create VideoWriter object
#In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)  DIVX (More to be tested and added)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	#print(ret)
	
	if ret == True:
		#operation to change brg picture to gray one.	
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		#show image
		cv2.imshow('frame', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		#write the flipped frame
		new_gray = cv2.flip(gray, 0)
		out.write(new_gray)		
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()
	
