import numpy as np
import cv2
import pygame
import pygame.locals
import matplotlib.pyplot as plt

ENTER = 13

img = cv2.imread('/home/quy/rose.jpeg', 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img);

while True:
	k = cv2.waitKey(0)
	if k == ENTER or k == ord('q'):
		cv2.destroyAllWindows()
		break
	elif k == ord('s'):        
		cv2.imwrite('gray_rose_2.jpeg', img)
		cv2.destroyAllWindows()
		break
	else:
		print('waiting command...')


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#to hide tick value on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()

