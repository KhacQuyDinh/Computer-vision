import numpy as np
import cv2
import matplotlib.pyplot as plt

ENTER = 13

#1 = cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#0 = cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#-1 = cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

img = cv2.imread('download.jpeg', 0)

plt.imshow(img)
#to hide tick value on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()

