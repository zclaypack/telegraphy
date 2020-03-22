'''
Telegraphy - Client
Python 3.7.4
Client/Server Chat made in Python
'''

#Import Statements
import socket

#Enter Sever Info
serverAddress = input(str("Please enter the IP of the server: "))
connectionPort = int(input("Please enter the port number of the server: "))

#Create Sock and Connection
sock = socket.socket()
sock.connect((serverAddress,connectionPort))
print("You have succsessfully connected to {}'s chatroom!".format(serverAddress))

#Chat Interface
while True:
            incomingMessage = sock.recv(1024)
            incomingMessage = incomingMessage.decode()
            print("Them: ", incomingMessage)
            print("")
            outboundMessage = input(str("You: "))
            outboundMessage = outboundMessage.encode()
            sock.send(outboundMessage)
            print("Your message has been delivered!")
            print("")