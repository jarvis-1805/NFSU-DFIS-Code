import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.1.45", 21))
response = s.recv(1024)
if ("FreeFloat Ftp Server (Version 1.00)" in response):
  print("[+] FreeFloat Ftp Server is vulnerable.")
#elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
