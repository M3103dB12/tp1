#!/usr/bin/python
from socket import*

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
clientPort = 13000
clientName = "localhost"
clientSocket = socket(AF_INET, SOCK_DGRAM)
print "The server is ready to receive"

while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.upper()
        clientSocket.sendto(modifiedMessage, (clientName, clientPort))
        serverSocket.sendto(modifiedMessage, clientAddress)

