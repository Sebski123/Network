#!/usr/bin/env python3
# TCP server. Will listen and receive data until client closes connection
# Adapted by Per dahlstrøm
import socket       # Fetch the socket module
from time import sleep

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)
receivedData = []


def decode(s):
    return s.decode('utf-8')


def processData(lst):
    return list(map(decode, lst))


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Awaiting connection on IP: ', s.getsockname()[0],
          ' Port: ', s.getsockname()[1])
    connection, fromAddress = s.accept()  # Wait and create connection object
    print('Connection from:', fromAddress)
    while True:
        receivedData.append(connection.recv(1))
        if receivedData[-1].decode("utf-8") == "q":
            receivedData.pop()
            receivedData = processData(receivedData)
            print("".join(receivedData))
            receivedData = []


except Exception as e:
    print(e)
    connection.close()
    print('Connection closed')
    s.close()
    print('Socket closed')
