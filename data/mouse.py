import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

# mouse callback function
#def draw_circle(event, x, y, flags, param):
#	if event == cv2.EVENT_LBUTTONDBLCLK:
#		cv2.circle(img, (x,y), 100, (255,0,0), -1)

drawing = False
mode = True
ix,iy = -1,-1

def draw_circle(event, x, y, flags, param):
	#define use global vars
	global ix, iy, drawing, mode
	
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
			else:
				cv2.circle(img, (x,y), 5, (0,0,255), -1)
	
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		#if mode == True:
			#cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
#		else:
			#cv2.circle(img, (x,y), 5, (0,0,255), -1)	
		

# create a black image, a window and bind the function to window
# np.zeros returns an array of shape (512,512,3) and type uint8
img = np.zeros((512,512,3), np.uint8)
# create a window named 'image'
cv2.namedWindow('image')
# name; callback_func
cv2.setMouseCallback('image', draw_circle)

while(True):
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF		
	if k == ord('m'):
		mode = not mode
	elif k == 13:
		break

cv2.destroyAllWindows()


