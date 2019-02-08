#!/usr/bin/env python3

import socket

HOST = '192.168.43.184'      # The server's hostname or IP address
PORT = 65433            # The port to send data to on the server
mySensorReadings = 'go'  # The application layer protoll


def readSensors():
    sensorReadings = input('Type sensor readings: ')
    return sensorReadings


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while mySensorReadings != 'q':
    mySensorReadings = readSensors()
    s.sendall(mySensorReadings.encode('utf-8'))
