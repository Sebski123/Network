from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import thread
from time import sleep, gmtime, strftime
import ssl       # Fetch the socket module
import select
import threading

HOST = ''
PORT1 = 65432
PORT2 = 65433


def handler(clientsock, addr):
    while 1:
        data = select.select([clientsock], [], [], 1)
        if len(data[0]) > 0:
            data = clientsock.recv(1024)
            print(data)


if __name__ == '__main__':
    ADDR = [(HOST, PORT1), (HOST, PORT2)]
    tList = []
    for i in range(2):
        serversock = socket(AF_INET, SOCK_STREAM)
        serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serversock.bind(ADDR[i])
        serversock.listen(5)

        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)
        clientsockSSL = ssl.wrap_socket(clientsock,
                                        server_side=True,
                                        certfile="certificates/server.crt",
                                        keyfile="certificates/server.key")
        tList.append(threading.Thread(
            target=handler, args=(clientsockSSL, addr)))

    for t in tList:
        t.start()
        print t.name

    for t in tList:
        t.join()
