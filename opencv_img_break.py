import cv2
import numpy as np
import os


cap = cv2.VideoCapture('output1.avi')

try:
	if not os.path.exists('data1'):
		os.makedirs('data1')
except OSError:
	print('Error')

currentFrame=0

while True:

	ret, frame = cap.read()


	name = './data1/frame' + str(currentFrame) + '.jpg'
	print('Creating...' + name)
	cv2.imwrite(name, frame)
	
	currentFrame += 1

cap.release()
cv2.destoryAllWindows()
