import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/media/pi/Seagate\ Backup\ Plus\ Drive/output.avi', fourcc, 20.0, (640, 480))

while True:
	ret, frame = cap.read()
	out.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
