PHASE 1 
Files attached: 
1) Readme.doc: Group Members, Steps to execute the program
2) Designdocument.doc: Explanation of each data type, arguments used, definition of different API’s used.
3) Server.c: C program to implement server socket
4) Client.c: C program to implement client socket
5) Transfer File


TEAM MEMBERS:  Akhila Nair, Yuanhao Yang


Objective of phase 2:
The main objective is transfer the file using UDP protocol which is unreliable but to use reliable data transfer (RDT 1.0) on top of it. Here the file is broken into chunks or pieces and then sent to the client.
Also the file has to be read in binary format.We are assuming that the UDP layer is perfectly reliable.In this phase, server code works as a sender and client code works as a reciever. 
Therefore the image will be splited into small packets at server side while at client side, it will reassembled. 
The only exception here is that it will work in a one way direction, i.e. from server to client.


Steps to execute :
Step 1 : Open python 3.6.2
Step 2 : Open a new file and write the code for server.
Step 3 : Open another file and write the code for client.
Step 4 : Run the server first to bind to the port.
Step 5 : After that run the client side.


Further explanation with screenshots is described in the design document.


 