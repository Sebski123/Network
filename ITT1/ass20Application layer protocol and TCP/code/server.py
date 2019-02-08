#!/usr/bin/env python3
# TCP server. Will listen and receive data until client closes connection
# Adapted by Per dahlstrøm
import socket       # Fetch the socket module

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
DataCommingIn = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Awaiting connection on IP: ', s.getsockname()[0],
      ' Port: ', s.getsockname()[1])
connection, fromAddress = s.accept()  # Wait and create connection object
print('Connection from:', fromAddress)
while DataCommingIn:
    receivedData = connection.recv(16)
    print(receivedData.decode('utf-8'))
    if not receivedData:
        DataCommingIn = False
connection.close()
print('Connection closed')
s.close()
print('Socket closed')
