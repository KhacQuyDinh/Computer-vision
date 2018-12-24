import cv2
import numpy as np
import sys
from scipy import sum, average
from matplotlib import pyplot as plt

def to_grayscale(arr):
#it is the same as function cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    "If arr is a color image (3D array, 1D for color band), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        print arr
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

#read an image like the following way will make some changes in the color.
img = cv2.imread('download.jpeg')
gray_scale_img = to_grayscale(img)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(gray_scale_img)
plt.title('Gray_scale Image'), plt.xticks([]), plt.yticks([])

#plt.subplot(122),plt.imshow(gray_img)
#plt.title('Gray Image'), plt.xticks([]), plt.yticks([])

plt.show()
