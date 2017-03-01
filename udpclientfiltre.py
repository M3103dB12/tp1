#!/usr/bin/python
from socket import *

serverName = "localhost"
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto('?',(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

