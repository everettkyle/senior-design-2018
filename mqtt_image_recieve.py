import pika

i=0
def callback(ch, method, properties, body):
	global i
	f=open("./collected_data/Allo_images/image"+str(i)+".jpg", "wb")
	f.write(body)
	f.close()
	i = i+1

credentials = pika.PlainCredentials('remote_server', 'toor')
parameters = pika.ConnectionParameters('172.24.111.250', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()


