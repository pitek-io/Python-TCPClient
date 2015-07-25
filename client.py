__author__ = 'ricky phillip vaughn jr'

from socket import *
import sys

def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()

if __name__ == '__main__':
    if(len(sys.argv) < 3) :
        print 'Usage : python client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    buf = 1024
    name = "user"

    addr = (host, port)

    clientsocket = socket(AF_INET, SOCK_STREAM)

    clientsocket.connect(addr)

    while 1:
        data = raw_input(">> ")
        if not data:
            break
        else:
            clientsocket.send(data)
            data = clientsocket.recv(buf)
            if not data:
                break
            else:
                print data
    clientsocket.close()
