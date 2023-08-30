import whois
import nmap
import ssl
import socket

def _whois():
  _website = input("Enter the name of the website: ")
  w = whois.whois(_website)
  w.expiration_date
  w.text
  print("\n\nWhois Query Result:")
  print('IP: ', socket.gethostbyname(_website))
  print(w)

def _nmap():
  ip = input("Enter the IP: ")
  nm = nmap.PortScanner()
  nm.scan(ip)
  for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
      print('----------')
      print('Protocol : %s' % proto)
      lport = nm[host][proto].keys()
      for port in lport:
        print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

def _cert():
  ip = input("Enter the ip/website: ")
  print("---------------------------------------------------------")
  print(ssl.get_server_certificate((ip, 443)))

def main():
  while True:
    print("\n========= MENU =========")
    print("1. WHOIS Query")
    print("2. NMAP Query")
    print("3. Generate Certificate")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 0:
      break

    if choice == 1:
      _whois()
    elif choice == 2:
      _nmap()
    elif choice == 3:
      _cert()
    else:
      print("Wrong Choice! Try Again!!!")

if __name__ == "__main__":
  main()