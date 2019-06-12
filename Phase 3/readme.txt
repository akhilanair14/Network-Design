PHASE 3
Files attached: 
1) Readme.doc: Group Members, Steps to execute the program
2) Designdocument.doc: Explanation of each data type, arguments used, definition of different API’s used.
3) Server.c: C program to implement server socket
4) Client.c: C program to implement client socket



TEAM MEMBERS:  Akhila Nair, Yuanhao Yang


Objective of phase 3:
Sender:
To achieve RDT 2.2 we break the image into packets and add checksum and sequence number into the packet.
When the data is sent and it is not corrupted and also the ack is not corrupted,data is not retransmitted again.
If the data is corrupted at the sender side,receiver will send a ack to sender saying that data is corrupted and the packet will be send again.
When sender receive a corrupted ACK packet from receiver, sender will resend the packet. 
Sender will continue to send new packet till it receives expecting Ack.

Receiver:
As sender, the receiver will also add checksum and sequence number.
Receiver will compare the checksum with the sender, which will help to understand if the data is corrupted or not.
When the data received is not corrupted and it receives the same sequence number as expected, receiver will send the ack with proper sequence number.
When data is not corrupted but sequence number is, i.e Ack was corrupted, though the sender will send the packet again, receiver will discard it.
When data is corrupted,receiver will send the ack with correct sequence number.


Steps to execute :
Step 1 : Open python 3.6.2
Step 2 : Open a new file and write the code for sender side.
Step 3 : Open another file and write the code for receiver side.
Step 4 : Run the sender first to bind to the port.
Step 5 : After that run the receiver side.


