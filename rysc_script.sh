#!/bin/bash
while true
do
	rsync -e 'ssh -p 22' -avzp /home/pi/senior_design/src/ready_img cc@192.5.87.106:/home/cc/testing_algo/
done
