import socket
import threading
import shutil
import os
import datetime
import subprocess
import cv2


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./test.avi', fourcc, 20.0, (640, 480))

curr_tp = "0"
last_tp = "0"
Dir = '/home/pi/senior_design/src/test_img/'

while True:

	ret, frame = cap.read()
	out.write(frame)
	cv2.imwrite("./"+str(datetime.datetime.now())+".jpg", frame)
	#if cv2.waitkey(1) & 0xFF == ord('q'):
	#	break
	
	file = open("../data.txt", "r")
	if last_tp == "0":
		curr_tp = file.read()
		curr_tp = curr_tp[-9:-7]
		#last_tp = curr_tp
	else:
        	curr_tp = file.read()
        	curr_tp = curr_tp[-9:-7]

	if curr_tp != last_tp:
		for img in os.listdir(Dir):
			if img.endswith(".jpg"):
				if curr_tp == '':
					break

				#finding imgs of shooting algo
				temp_img = int(img[-13:-11])
				temp_curr_tp = int(curr_tp) - 1
				#temp_curr_tp1 = float(curr_tp) - 0.7

				if (temp_curr_tp == temp_img):
					print img
					print "moved"        				
					shutil.move(str(img), "/home/pi/senior_design/src/ready_img/")
		for item in os.listdir(Dir):
			if item.endswith(".jpg") or item.endswith(".avi"):
				os.remove(item)
		last_tp = curr_tp
	
	#ALGORITHM TO CLEAR PICTURES AFTER A CERTAIN AMOUNT OF TIME
	#NEEDS WORK
	#if count == 3600:
	#	for item in os.listdir(Dir):
	#		if item.endswith(".jpg"):
	#			os.remove(item)
	#for item in os.listdir(Dir):
	#	count += 1
			
	file.close()
cap.release()
out.release()

