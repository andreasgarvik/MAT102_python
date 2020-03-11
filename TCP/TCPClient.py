from socket import *

serverName = '192.168.10.183'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence1 = input("Skriv inn en tekst: ")
clientSocket.send(sentence1.encode())
modSentence1 = clientSocket.recv(1024)
print(modSentence1.decode())
clientSocket.close()
