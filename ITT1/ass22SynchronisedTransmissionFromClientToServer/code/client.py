#!/usr/bin/env python3

import socket
from time import sleep
from random import randint

HOST = '192.168.43.242'      # The server's hostname or IP address
PORT = 65433            # The port to send data to on the server
mySensorReadings = 'go'  # The application layer protoll


def temperatureSensor():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        t = f.readline()

    #out = randint(0, 100)
    return str(t) + "q"


def pad(i):
    if len(i) == 1:
        return "00" + str(i)
    elif len(i) == 2:
        return "0" + str(i)
    else:
        return str(i)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

input("Press enter to begin")
while True:
    try:
        mySensorReadings = temperatureSensor()
        print(mySensorReadings)
        s.sendall(mySensorReadings.encode('utf-8'))
        sleep(1)

    except KeyboardInterrupt:
        s.close()
        exit()
