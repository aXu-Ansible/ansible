#!/usr/bin/python
import socket
import sys
def tryPort(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    host = socket.gethostname()
    try:
        sock.bind((host, port))
        result = True
    except:
        print("Port is in use")
    sock.close()
    return result

# create a socket object

tryPort(18080)
serversocket = socket.socket(
socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 19999

# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)
while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()
   print("Got a connection from %s" % str(addr))
   msg='Thank you for connecting from server'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()
