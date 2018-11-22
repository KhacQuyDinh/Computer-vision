import cv2
import numpy as np

img = cv2.imread('/home/quy/rose.jpeg')

# BGR
px = img[100,100]
#print px

# accessing only blue pixel
blue = img[100,100,0] # also Green(1) and Red(2)
#print blue

img[100,100] = [255,255,255]
print img[100,100]
cv2.imshow('image', img)

while(True):
	if (cv2.waitKey(0) & 0xFF) == ord('q'):
		break;

cv2.destroyAllWindows()
