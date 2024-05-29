#
#   Favicon server in Python using zeroMQ
#

import time
import zmq
import favicon

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for request from client
    url = socket.recv()

    # Optional print statement to show request
    print(f"Server Received request: {url}")

    # Use favicon library to grab icon from url
    # You need to supply a url including the https://


    
    # Try to find favicon from given url
    try:
        icons = favicon.get(url)

        # Favicon function grabs multiple icons
        # first one in array should be the one we want
        icon = icons[0]

        #  Do some 'work'
        time.sleep(1)

        # Optional Print statement to show response
        print(f"Server sending response: {icon.url}")

        # Send reply back to client
        socket.send_string(icon.url)

    # Let client know if favicon not found or server unresponsive
    except Exception as err:
        print(f"Unable to retrieve favicon: {err}")

        socket.send(b"FAVICON_NOT_FOUND")


###############################################################################

    # If you want to save the icon to a file you can:

    # import urllib.requeest
    # urllib.request.urlretrieve(icon.url, "filename.png")

    # filename.png can be the name of the file you want to save the icon to

###############################################################################
