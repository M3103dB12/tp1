#!/usr/bin/python

from socket import *
serverPort = 12000
clientPort = 13000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.bind(("",clientPort))
	clientSocket.listen(1)
	print "The server is ready to send"
	connectionSocket, addr = clientSocket.accept()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
