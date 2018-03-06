#!/usr/bin/python
import socket
import sys
#from sys import argv

 
#print (sys.argv[0])
print (sys.argv[1])
PORT = int(sys.argv[1])
#if ((sys.argv[1] > 50000) or (sys.argv[1] < 79)) :
if not (PORT in range(79,60000) ) :
  print ("wrong port")
  sys.exit(0)

HOST = ''   # Symbolic name, meaning all available interfaces

PORT = 18888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
#Start listening on socket
s.listen(100)
print ('Socket now listening')
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    msg='Thank you for connecting'+ "\r\n"
    s.send(msg.encode('ascii'))
     
s.close()
