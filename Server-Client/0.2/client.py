import socket

soc = socket.socket()

#nos conectamos al ssrvidor

soc.connect(("0.0.0.0", 9999))
#soc.connect(("192.168.0.8", 4444))

#creamos un bucle para mantener abierta la conexion
while True:
	
	mensaje = raw_input("mensaje a enviar: ")
	
	#enviamos en mensaje
	soc.send(mensaje)

	#creamos la regla close para cerra la conexion cuando se envie como mensaje al servidor
	if(mensaje == "close"):
		break

print("Adios...")

soc.close()
