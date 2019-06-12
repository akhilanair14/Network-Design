phase 4

TEAM MEMBERS:  Akhila Nair, Yuanhao Yang
Attachments: Readme, Receiver4.py, Sender4.py, Add.py, emoji.jpg, design document, newemoji.jpg,contribution 
Objective of phase 4:
Sender:
To achieve RDT 2.2 we break the image into packets and add checksum and sequence number into the packet.
In terms of RDT3.0,we add timer to resend data when process of transmission happens packet loss. 
When sender sends corrupted to server, sender will receive a ack and will be told that data is not correct. 
Then sender will resend data. If sender doesn't receive ack before timeout, sender will resend data to server whatever server whether receive duplicate.

Server:
To achieve RDT2.2, server add checksum and sequence number.
Server will compare the checksum with the sender, which will help to understand if the data is corrupted or not.
When the data received is not corrupted and it receives the same sequence number as expected, Server will send the ack with proper sequence number.
When data is not corrupted but sequence number is, i.e Ack was corrupted, though the sender will send the packet again, Server will discard it.
When data is corrupted,receiver will send the ack with correct sequence number.
In RDT3.0, server is considered to be same as RDT2.2.