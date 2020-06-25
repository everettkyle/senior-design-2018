import subprocess

x=0
while(True):
	subprocess.call(["scp","-i","mykey","frame" + str(x) + ".jpg", "cc@192.5.87.45:/home/cc/"])
	x += 1
