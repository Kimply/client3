import socket

ip=input('Enter ip server :')
port=input('\nEnter port server :')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
   while(1):
      s.settimeout(3)
      s.connect((ip, int(port)))
      s.settimeout(3)
      while True:
          message=input("your message: ")
          s.send(message.encode('utf-8'))
  

isOpen(ip,port)      


        