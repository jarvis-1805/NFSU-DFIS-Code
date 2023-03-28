# client side code

import socket

s = socket.socket()
rhost = '127.0.0.1'
rport = 12345
s.connect((rhost, rport))
print(s.recv(1024).decode())

# close the connection
s.close()

