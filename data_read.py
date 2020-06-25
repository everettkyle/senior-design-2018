import os
count = 0
temp_tp = "0"
last_tp = "0"
temp2_tp = "0"
while True:
	file = open("data.txt", "r")
	if last_tp == "0":
		curr_tp = file.read()
	else:
		curr_tp = file.read()
		temp_tp = curr_tp[-9:-7]

	if curr_tp != last_tp:
		print(curr_tp)
		last_tp = curr_tp
	
	file.close()
