from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import thread
from time import sleep, gmtime, strftime
import ssl       # Fetch the socket module
import select

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
        thread.start_new_thread(handler, (clientsockSSL, addr))

    sleep(1000)

