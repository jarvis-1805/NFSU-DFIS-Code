from datetime import datetime as dt
import socket

d = str(dt.now()).split('.')[0]
print(f"Lab 8 SHUBHANG GUPTA {d}")

# get your pc host name
host = socket.gethostname()
print('HOST:', host)

# get your ip
ip = socket.gethostbyname(host)
print(f'{host} ip: {ip}')

# get ip of google.com
ip_google = socket.gethostbyname('www.google.com')
print('GOOGLE.COM ip:', ip_google)

