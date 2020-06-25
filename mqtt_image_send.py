import pika
import logging
import numpy as np
import os
import cv2

TRAIN_DIR = './collected_vid/Allo_images'

i = 0
 
for img in os.listdir(TRAIN_DIR):
	f=open(str(img),"rb")
	j = f.read()
	logging.basicConfig()
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='hello')
	channel.basic_publish(exchange='', routing_key='hello', body=j)
	i=i+1
	print(" [x] Sent " + "img" + str(i))
connection.close()

