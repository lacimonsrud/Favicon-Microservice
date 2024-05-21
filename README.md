# Favicon-Microservice
Microservice for grabbing url favicon

A. How to programmatically request data:

Launch the microservice server, using python favicon_server.py
Connect to the socket using zeroMQ at port 5555
Send a request of the url including the http://www. part

EXAMPLE: socket.send_string("http://www.reddit.com") OR socket.send_string(url) where url = "http://www.reddit.com"
 
B. How to programmatically recieve data:

Set up your program to recieve a response from the socket using socket.recv()
Save the response into a variable and voila! You now have the url to the favicon :)

C. UML Diagram:

![image](https://github.com/lacimonsrud/Favicon-Microservice/assets/114252570/bd4a8c51-e289-4b19-a029-ee9a92182dff)

