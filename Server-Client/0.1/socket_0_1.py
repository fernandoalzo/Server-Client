import socket

s = socket.socket()

host = "192.168.0.8"        #socket.gethostname() #get local hostname
port = 1500
s.bind((host, port)) #bind to the port

s.listen(100)

while True:
	c, addr = s.accept() #establish connection with client
	print("got the connection from ", addr)
	c.send("thank you for connecting".encode())
	c.close()

