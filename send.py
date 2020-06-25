import pika 
import logging
import numpy as np
import os
import cv2

img = cv2.imread('/data/frame200.jpg')
img = np.array(img)

logging.basicConfig()
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=img.all())
print(" [x] Sent 'Hello World!' ")

connection.close()
