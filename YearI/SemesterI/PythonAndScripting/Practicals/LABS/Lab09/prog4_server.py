# server side code

import socket

s = socket.socket()
print("Socket successfully created!!!")

# port on client
port = 12345

#can request from another pc
s.bind(('', port))
print("Socket binded to %s" %(port))

s.listen(5)
print("Socket is listening...")

while True:
    c, addr = s.accept()
    print('Got connection from:', addr)
    c.send('Thank you for connecting!!!'.encode())
    c.close()
    break

