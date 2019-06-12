PHASE 1 
Files attached: 
1) Readme.doc: Group Members, Steps to execute the program
2) Designdocument.doc: Explanation of each data type, arguments used, definition of different API’s used.
3) Server.c: C program to implement server socket
4) Client.c: C program to implement client socket


TEAM MEMBERS:  AKHILA NAIR, POORNIMA MANJUNATH
Objective of the project: Allowing the Network software application to communicate using User Datagram Protocol. It is point to point communication and bidirectional means data can be transfered can be send and received from either side. 
Steps to execute the Program:
Step1: Open editor window and type “vim socket_server.c” and then save the written file using “:wq “.
Step 2: Compile the server code using “gcc socket_server.c -o Server.out“. (Here Server.out represents the name, you can give any name).
Step 3: For executing the server side type “./server.out 1234” ( Here 1234 is the port number)
After this step the server terminal waits for the client to send the message. It is important to run the server first and then run the client side. 
Step 4: Open a new terminal and type “vim socket_client.c” to open the client code and save the file using “:wq“. 
Step 5: Compile the client code and give a name to it using “gcc socket_client.c -o client.out “.
Step 6: Execute the program by mentioning the local host port number by using “./client.out localhost 1234“.
After this step client will ask for the message to be send to the server. The server should get the message and acknowledge the message back to client.
