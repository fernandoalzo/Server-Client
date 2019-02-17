import socket 

#instanciamos el objeto de la clase socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#indicamos en que puerto debe escuchar y de que servidor esperar conexiones 
#lo dejamos en blanco para recibir conexiones externas 
soc.bind(("",4444))

#especificamos numero de conexiones que deseamosescuchar
soc.listen(1)

#instnaciamos la variable sc(socket liente) para recibir los datos, al recibir los datos este devlverz una tupla con los datos de conexion (IP, PORT)
sc, addr = soc.accept()

while True:
	#recibimos el mensaje, con el metodo recv() y como parametro la cantidad de bytes a recibir
	recibido = sc.recv(1024)

	#si el mensaje entrnate contiene la palabra close, se cierra la conexion
	if(recibido == "close"):
		break
	
	#mostrarel mesaje y la ip de quien lo envia
	print(str(addr[0]) + "Dice: ", recibido)
	
	#devolvemos el mensaje 
	sc.send(recibido)

print("Adios")

#cerramos la instancia del socket y el servidor
sc.close()
socket.close()



