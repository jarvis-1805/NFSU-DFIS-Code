from datetime import datetime as dt
import socket

d = str(dt.now()).split('.')[0]
print(f"Lab 8 SHUBHANG GUPTA {d}")

# create socket an connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip plus port binding
port1 = 80
port2 = 443

host_ip = socket.gethostbyname('www.google.com')
print(host_ip)

s.connect((host_ip, port1))
print("The socket has successfully connected to google")

# byte number
# print(s.recv(655350).decode('utf-8'))
