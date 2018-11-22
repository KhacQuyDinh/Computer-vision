import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
if not os.path.exists('./recognizer'):
	os.makedirs('./recognizer')

def getImagesWithID(path):
	#connect dir + image_name = image_paths
	#a list of imagepath
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
	faces = []
	IDs = []
	for imagePath in imagePaths:
		#open image and rotate to left
		faceImg = Image.open(imagePath).convert('L')
		#convert faceImg to uint8 = type
		faceNp = np.array(faceImg, 'uint8')
		
		#get the ID of the image
		ID = int(os.path.split(imagePath)[-1].split('.')[1])

		faces.append(faceNp)
		IDs.append(ID)
		cv2.imshow("training", faceNp)
		cv2.waitKey(10)
	return np.array(IDs), faces

Ids, faces = getImagesWithID(path)
recognizer.train(faces, Ids)
recognizer.write('recognizer/trainingData.yml')
cv2.destroyAllWindows()
