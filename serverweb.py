#!/usr/bin/python

from socket import *
serverPort = 8081
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept()
	request = connectionSocket.recv(1024)
	url=request.split(" ")
	page=url[1]
	page=page[1:]
	f=open(page,"r+t")
	#connectionSocket.send(request)
	connectionSocket.send(f.read())
	connectionSocket.close()