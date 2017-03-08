#!/usr/bin/python

from socket import *
serverName = "83.152.1.178"
serverPort = 21
clientSocket = socket(AF_INET, SOCK_STREAM)
while 1:
	clientSocket.connect((serverName,serverPort))
	sentence = raw_input("Input lowercase sentence:")
	clientSocket.send(sentence)
	modifiedSentence = clientSocket.recv(1024)
	print "From Server:", modifiedSentence

clientSocket.close()
