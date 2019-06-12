from socket import *
import time

buf = 1024
hostname = 'localhost'
port = 15003
server_addr = (hostname,port)
s = socket(AF_INET,SOCK_DGRAM)

fileRead=open('123.jpg','rb')
message = fileRead.read(1024)

while message != b"":
    packet = message
    s.sendto(packet, server_addr)
    message = fileRead.read(1024)

s.sendto(b"", server_addr)
time.sleep(0.5)
fileRead.close()
print('finish')
s.close()
