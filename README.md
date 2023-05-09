# CS361-Project
Self Explanatory

#CS361-Microservice
We will primarily use sockets as our pipeline.

How to Request Data: 
Simply run my microservice and connect to the server it creates at PORT 1080 of localhost.
Send a string of items delimited by spaces (this can be subject to change if inconvenient).
The first word of the string must be a keword that tells the serice what to do.
If you want to request data from a file:
  - Send the string "GET {filename}" to the server
  - Must be a file that exists
  - Example: stream.write("GET Downloads\file.txt".as_bytes())


If you want to save the current current list of stocks:

  - Send the string "POST {filename} {stock1} {stock2} {stock3} ..." to the server
  - File will be overwritten if it exists
  - Can only send up to 1024 bytes/characters of data (based on partner specifications, negotiable)
  - Example: stream.write("POST input.txt AAA EEE OOO WOW".as_bytes())

If you want to close the microservice:

  - Send the string "EXIT" to the server
  - This is so that the microservice can easily exit without user having to manually close terminal

How to Receive Data:
The microservice will send data back to you with the appropriate response.
The GET function will send the data of a file in the format "{stock1}\n {stock2}\n {stock3}\n"
All other functions will simply send bakc a confirmation message.
Use stream.read()

UML Diagram
![UML](https://github.com/BLRGAdityaC/CS361-Project/blob/main/UML%20Diagram.png)
