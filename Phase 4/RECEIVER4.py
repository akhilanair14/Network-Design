import socket
import io
import os
import sys
import select
import struct
import array
from ADDITION import add
        
ServerName = "localhost"
PortNumber = 42200
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerSocket.bind((ServerName,PortNumber))
print("Server Started")
buffer = bytearray()
myfile = open("newemoji.jpeg","wb")

packet_size = 1042#includes data, checksum, seqno.
noOfpackets = 0

'''Function to calculate sum of received data from sender'''
def SumOfData(data):
    buffer = bytearray(data)
    length = len(buffer)
    i = 0
    j = 2
    pt = 0
    sumOfBites = 0
    sumOfBites = bin(sumOfBites)
    
    checksum = 0
    checksum = bin(checksum)
    while(pt<=510): # loop for an data part
        data1 = buffer[i:j]
        p1 = ''.join(format(x, 'b').zfill(8) for x in bytearray(data1))
        i = i+2
        j = j+2               
        data2 = buffer[i:j]
        p2 = ''.join(format(y, 'b').zfill(8) for y in bytearray(data2))
        q = add(p1, p2)
        i = i+2
        j = j+2
        sumOfBites = add(q, sumOfBites) #Sum of data only
        pt = pt+2
    return sumOfBites



'''Function to Make new packet for sender'''
def AckPacket(Ack,ExSeq_No):
    size = 6
    Pkt = bytearray(size)
    Pkt[0:2] = struct.pack('H',Ack)
    Pkt[2:4] = struct.pack('H',ExSeq_No)
    if(len(Pkt[0:4])%2 == 1):
        Pkt[0:4] += "\0"
    ck = sum(array.array("H",Pkt[0:4]))
    ck = (ck >> 16) + (ck & 0xffff)
    ck += ck >> 16
    ck = ~ck
    ck=(((ck>>8)&0xff)|ck<<8) & 0xffff
    Pkt[4:6] = struct.pack('H',ck)
    return Pkt


 
ExSeqNo   =  1  #Expected Sequence Number initial value
ACK       =  1  #ACK intial value
packetdata=  0  

'''Function to Extract whole packet from sender and again sending it
back as new packet with checksum and acknowledgement'''
def ExtractPacket():
    
    global numPacks
    global ACK
    global ExSeqNo
    global packetdata

  
    packetdata,clientAddress = ServerSocket.recvfrom(packet_size)
    print("")
    data = packetdata[0:1024]
    Check = packetdata[1024:1040]
    ExpectedSeqNo = packetdata[1040:1042]
    print("CHECKSUM   = " + Check)
    print("ExpectedSeqNo" + ExpectedSeqNo)
    datasumval = SumOfData(data)
    q = add(Check, datasumval)
    q = str(q)
    print("Sum of CHK and LOCAL and this hould be all 1  = " + q)
    ExSeqNo = str(ExSeqNo)
    
     
    if((ExpectedSeqNo==ExSeqNo) & (q=='1111111111111111')):
        print("PACKET RECIEVED")
        myfile.write(data)
        ACK = int(ACK)
        ExSeqNo = int(ExSeqNo)
        print(ACK)
        print(ExSeqNo)
        backpacket=AckPacket(ACK,ExSeqNo)
        ACK = ACK+1
        ExSeqNo = ExSeqNo + 1
        ServerSocket.sendto(backpacket, clientAddress)
        print("ACK packet send ")
    
    else:
        print("Packet Not recieved")
        ACK = int(ACK)
        ExSeqNo = int(ExSeqNo)
        ACK = ACK-1
        ExSeqNo = ExSeqNo-1
        

            
            

while (1):
    ExtractPacket()
    if(packetdata==0):
            break
    
    
  

myfile.close()
print("File Downloaded")

