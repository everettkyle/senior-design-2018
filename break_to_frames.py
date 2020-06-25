import cv2

vidcap=cv2.VideoCapture('Allo.avi')

success, image = vidcap.read()

count = 0 
while success:
	success,image = vidcap.read()
	#can save frame in dir
	cv2.imwrite("./Allo_images/frame%d.jpg" % count, image)     # save frame as JPEG file
	if cv2.waitKey(10) == 27:                     # exit if Escape is hit
		break
	count += 1

