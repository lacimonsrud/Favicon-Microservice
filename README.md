# Favicon-Microservice
Microservice for grabbing url favicon

For some reason the README exists in the main branch, while the code lives in the master branch (not sure what I did wrong here)

General Info! ---------------------------------------------------------------------------------------------------------

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

Mitgation plan! ---------------------------------------------------------------------------------------------------------

1. For which teammate did you implement “Microservice A”?

  Joshua Samuel

2. What is the current status of the microservice? Hopefully, it’s done!

  It looks very simple, but it is done!

3. If the microservice isn’t done, which parts aren’t done and when will they be done?

  No worries here, it should be complete unless anything comes up! If there are any changes that Joshua would like me to make, I am
  open to reworking the server if needed :)

4. How is your teammate going to access your microservice? Should they get your code from GitHub? Should they run your code locally? Is your microservice hosted somewhere? Etc.

  He can access it from GitHub! He should run it locally.

5. If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?

  He should contact me! I am available weekends, and most weekdays after 2pm.

6. If your teammate cannot access/call your microservice, by when do they need to tell you?

  He should let me know ASAP, I dont have a deadline by when I should be informed but the sooner the better!

7. Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?

  I'm a little worried that the microservice is too simple, but as I said before I am very open to working with Joshua to make it work the way he wants it to!
  Other than that, I don't have any other concerns or assumptions I'm making!

Extra Info! ---------------------------------------------------------------------------------------------------------

If you want to save the icon to a file you can:

import urllib.requeest
urllib.request.urlretrieve(icon.url, "filename.png")

filename.png can be the name of the file you want to save the icon to

This is included in favicon_server.py at the end!
