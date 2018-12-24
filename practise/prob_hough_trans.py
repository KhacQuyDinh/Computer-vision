import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('building.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect edges in the input image.
edges = cv2.Canny(gray,50,150,apertureSize = 3)
# Minimum length of line. Line segments shorter than this are rejected.
minLineLength = 100
#Maximum allowed gap between line segments to treat them as single line.
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,2*np.pi/180,100,minLineLength,maxLineGap)

if np.size(lines) > 1:
   for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

#cv2.imshow('dst',img)
#if cv2.waitKey(0) & 0xff == 27:
#    cv2.destroyAllWindows()
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

