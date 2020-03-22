'''
Telegraphy - Server
Python 3.7.4
Client/Server Chat made in Python
'''

#Import Statements
import socket
import resolve

#Create Socket and Get Server Info
sock = socket.socket()

#Resolve the Server Address (See README for more info)
serverAddress = resolve.resolveIP()

#Print Confirmation of Server
print("Server will start on {}".format(serverAddress))
port = int(input("Please enter a port number to run your server on: "))
sock.bind((serverAddress,port))

#Print Server Info + Awaiting Connetions
print()
print("Successful binding! Server: {} has been binded to Port: {}".format(serverAddress,port))
print()
print("Server is waiting/listening for incoming connections!")
print()

#Allow server to listen for connections, and print who connects
sock.listen(1)
connection, client = sock.accept()
print("{} has connected to the server!".format(client))
print("")

#Chat Interface
while True:
            outboundMessage = input(str("You: "))
            outboundMessage = outboundMessage.encode()
            connection.send(outboundMessage)
            print("Your message has been sent!")
            print()
            incomingMessage = connection.recv(1024)
            incomingMessage = incomingMessage.decode()
            print("Them: ", incomingMessage)
            print()
