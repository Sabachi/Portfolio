#Exploring the HyperText Transport Protocol
# Request response cycle

import socket

# Returns an object which creates a connection across the internet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish a connection to a port on a domain
mysock.connect(('data.pr4e.org', 80))

# The rule of internet protocol is that first you send something, with the send
# method
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) # Receives upto 512 characters
    if len(data) < 1: # if no data then end the file, this is the stop condition
        break
    print(data.decode(),end='') # decode the data from utf-8 to unicode

mysock.close()
