# Connect to google from client side
from datetime import datetime as dt
import socket
import sys

d = str(dt.now()).split('.')[0]
print(f"Lab 8 SHUBHANG GUPTA {d}")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created!!!")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))


# default port for socket server side
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
    print("ip address of google:", host_ip)
except socket.gaierror:
    # this means could not resolve the host
    print("There was an error resolving the host")
    sys.exit()


# connecting to the server
s.connect((host_ip, port))
print("The socket has successfully connected to google!!!")
s.close()

