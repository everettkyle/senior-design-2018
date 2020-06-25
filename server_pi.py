# -*- coding: utf-8 -*-
import socket
import threading
import time
import datetime

bind_ip = '172.24.111.250'
bind_port = 9999
#ts = datetime.datetime.now()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

#print 'Listening on {}:{}'.format(bind_ip, bind_port)


def handle_client_connection(client_socket):
	request = client_socket.recv(1024)
	if request == '1':
		file = open("data.txt","wb") 
		file.write(str(datetime.datetime.now()))
		file.close()
		#print '{},{}'.format(request,datetime.datetime.now())
	client_socket.close()

print("Server from main_pi ready:")
while True:
	client_sock, address = server.accept()
       #	print 'Accepted connection from {}:{}'.format(address[0], address[1])
	client_handler = threading.Thread(
	target=handle_client_connection,
	args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
	)
	client_handler.start()
