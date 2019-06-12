import socket
import os
from ADDITION import add
import math
import sys
import select
import struct
import array
from time import sleep


ServerName = "localhost"
PortNumber = 42200
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                       
addr = (ServerName, PortNumber)
buf = 1024 #size of actual data

f = open("emoji.jpg", "rb") 
buffer = bytearray(os.path.getsize("emoji.jpg"))
f.readinto(buffer)
length = len(buffer)
print(length)


''' This section is used to adjust the partially
filled data in packet because size of data is fixed i.e. 1024 bytes''' 
numPacks = (int)(length / buf) + 1
print(numPacks)
emptyBytes = (numPacks * buf - length)
print(emptyBytes)
if(emptyBytes != 0):
	filler = buffer.ljust(emptyBytes + length, '0')
	newLength = len(filler)
	print(newLength)
	buffer = filler
	length = newLength
	print(length)
	

i             = 0   #index for data in checksum calculation
j             = 2   #index for data in checksum calculation

noOfpackets   = 0   #number of packets counter

a             = 0   #Packet variable
b             = 1024#Packet variable

''' window variables '''
base          = 1   #Initial value of Base 
nextSeqNumber = 1   #Initial value of next sequence number
WindowSize    = 4   #Window Size
complete      = 0   #Flag to signal completion of send
packetdata=0

''' Function to calculate checksum of packet data'''
def MakePacketChecksum():

    global i
    global j
    pt = 0
    sumOfBites = 0
    sumOfBites = bin(sumOfBites)
    
    checksum = 0
    checksum = bin(checksum)
    while(pt<=510):#loop for checksum calculation
        data1 = buffer[i:j]
        p1 = ''.join(format(x, 'b').zfill(8) for x in bytearray(data1))
        i = i+2
        j = j+2
        
        data2 = buffer[i:j]
        p2 = ''.join(format(y, 'b').zfill(8) for y in bytearray(data2))
        q = add(p1, p2)
        i = i+2
        j = j+2
        pt = pt+2
        sumOfBites = add(q, sumOfBites)

    checksum =''.join([bin(~0)[3:] if x == '0' else bin(~1)[4:] for x in sumOfBites])
    return checksum

'''Function to calculate checksum of ACK and SEQNO from reciever for authenticity'''
def ChkOfAckSeq(bpbuf):
	if(len(bpbuf)%2 == 1):
	    bpbuf += "\0"
	ck = sum(array.array("H",bpbuf))
	ck = (ck >> 16) + (ck & 0xffff)
	ck += ck >> 16
	ck = ~ck
	return (((ck>>8)&0xff)|ck<<8) & 0xffff
  

''' Function to Send Packet to reciever'''
def MakePacket(nextSeq):
        global a
        global b
        global nextSeqNumber
        global packetdata
        
        checksum = MakePacketChecksum()
        print(checksum + "checksum at sender")
        data = buffer[a:b]
        data = str(data)
        nextSeqNumber = str(nextSeqNumber)
        print("Next Seq No: " + nextSeqNumber + "\n")
        packetdata = [data,checksum,nextSeqNumber]
        packetdata = ''.join(packetdata)
        a+=1024
        b+=1024
        checksum = 0
        return nextSeqNumber

def PacketCycle():
        while(1):
                global a,b
                global noOfpackets
                global i, j
                global nextSeqNumber,WindowSize,base,complete
                global packetdata
                
                while(1):
                        if(noOfpackets>=length):
                                        complete=1
                                        print("File transfer Successful ") 
                                        break
                        if(nextSeqNumber<base+WindowSize):
                                nextSeq = MakePacket(nextSeqNumber)
                                ClientSocket.sendto(packetdata, addr)
                                noOfpackets+=1024
                                if(base == nextSeqNumber):
                                        ClientSocket.settimeout(0.3)
                                nextSeqNumber = int(nextSeqNumber)        
                                nextSeqNumber+=1
                        else:
                                 break
                                        
                while(1):
                        try:
                                if(complete == 1):
                                        return
                                backpacket, serverAddress = ClientSocket.recvfrom(6)#Buffer size:2 bytes each for ACK, SEQNO, CHECKSUM 
                                bpbuf = list(bytearray(backpacket))
                                newckhsumcal = ChkOfAckSeq(bpbuf[0:4])#calculating new checksum from ACK and SEQNO to check authenticity
                                bpbuf[:] = ""
                                
                                getacknum = struct.unpack("H",str(backpacket[0:2])) #extracting ACK
                                seq = struct.unpack("H",str(backpacket[2:4]))       #extracting SEQNO  
                                newchksum = struct.unpack("H",str(backpacket[4:6])) #extracting CHECKSUM
                                
                                
                                if(newchksum[0] == newckhsumcal): #extracted values are tuple.So accessing by index
                                        base = newchksum[0] 
                                        base = getacknum[0] + 1
                                        getacknum = getacknum[0]+1
                                        if (base == nextSeqNumber):
                                                break
                                        

                        except socket.timeout: #When timeout occurs control comes here
                                goingBack = nextSeqNumber-base #Correcting variables in order to send back packets
                                base == nextSeqNumber
                                a-=(goingBack*1024) # Packet data indeces correction a, b
                                b-=(goingBack*1024)
                                i-=(goingBack*1024) #Checksum indeces correction i,j
                                j-=(goingBack*1024)
                                noOfpackets-=(goingBack*1024) # Correcting counter number
                                nextSeqNumber = int(nextSeqNumber)
                                nextSeqNumber-=goingBack
                                print("timeout")
                                break
                       
                        
                if(noOfpackets>=length):
                        print("File transfer Successful")
                        break

PacketCycle()                                
                        
print("")
print("All Done!!!")
        
f.close()    
ClientSocket.close()

