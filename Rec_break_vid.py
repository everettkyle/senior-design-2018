import cv2
import numpy as np
import datetime
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./test.avi', fourcc, 20.0, (640, 480))
count = 0
while True:
	ret, frame = cap.read()
	out.write(frame)
	cv2.imwrite("./test_img/"+str(datetime.datetime.now())+".jpg",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cap.release()
out.release()

