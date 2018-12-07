#!/usr/bin/env python3
# TCP server. Will listen and receive data until client closes connection
# Adapted by Per dahlstrøm
import socket       # Fetch the socket module

HOST = ''  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)
DataCommingIn = True


def printData(lst):
    for i in range(0, len(lst), 10):
        for j in range(10):
            print(lst[i+j], end=" ")
        print()
    print("-" * 10)


def decode(s):
    return s.decode('utf-8')


def proccesData(lst):
    lst = list(map(decode, lst))
    printData(receivedData)


receivedData = []

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Awaiting connection on IP: ', s.getsockname()[0],
          ' Port: ', s.getsockname()[1])
    connection, fromAddress = s.accept()  # Wait and create connection object
    print('Connection from:', fromAddress)
    while DataCommingIn:
        receivedData.append(connection.recv(2))
        if receivedData[-1].decode('utf-8') == "qu":
            receivedData.pop()
            proccesData(receivedData)
            receivedData = []

        if receivedData[-1].decode('utf-8') == "it":
            DataCommingIn = False

    connection.close()
    print('Connection closed')
    s.close()
    print('Socket closed')
except:
    connection.close()
    print('Connection closed')
    s.close()
    print('Socket closed')
