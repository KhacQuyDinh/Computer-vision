import cv2
import numpy as np

img = cv2.imread('rose.jpeg')

px = img[100,100]

// It returns a tuple of number of rows, columns and channels (if image is color):
print img.shape

// Total number of pixels is accessed by img.size
print img.size

// Image datatype is obtained by img.dtype
print img.dtype

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))


