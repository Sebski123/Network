#!/usr/bin/env python3
# python ssl socket test client
# The client sends user input to the server encrypted
# Server and client keep TCP/IP connection open until closed by client
# By Per Dahsltroem pda@ucl.dk UCL University College
# 30-11-2018

import socket
import ssl

HOST = '127.0.0.1'      # The server's hostname or IP address
PORT = 65432            # The port to send data to on the server
mySensorReadings = 'go'  # The application layer protoll

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server. We use a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(mySocket,
                           ca_certs="serverCertificate.crt",
                           cert_reqs=ssl.CERT_REQUIRED)


def readSensors():
    sensorReadings = input('Type sensor readings: ')
    return sensorReadings


with ssl_sock as s:
    ssl_sock.connect((HOST, PORT))
    text = 'go'
    while mySensorReadings != 'q':
        mySensorReadings = readSensors()
        ssl_sock.sendall(mySensorReadings.encode('utf-8'))
    s.close()
