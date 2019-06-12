import socket               #This header is better

host="localhost"
port = 15003
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',port))
print ("bind complete")
#addr = (host,port)
buf=1024

outputFile = "123.jpg"
fileWrite = open(outputFile, 'ab') #File should be created before receiving binary file
while 1:
    # Wait here until recieve message from socket
    message, clientAddress = s.recvfrom(1024)
    # Write local file
    fileWrite.write(message)
    fileWrite.seek(1024)
    # If EOF, close the file
    if message == b"":
        break
fileWrite.close()
s.close()
print ("Download have finished")

#Send the ack to the client

#reference http://blog.csdn.net/guddqs/article/details/53808605
