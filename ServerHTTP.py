#Imports--------------------------
import socket
import signal
import time
import sys
#import HTTPMethodHandler
#import HTTPResponse
from HTTPParser import parse
#---------------------------------

PORT = 8000 # Puerto por el cual escucha el servidor.
			# Se puede modificar por si se desea escuchar en otro puerto.

class ServerHTTP:

	#Contructor de  la clase
	def __init__(self):
		self.host = ''
		self.port = PORT
		self.my_dir = (self.host, self.port)
		#self.www_dir = 'www'

	#Levanta el servidor
	def serve(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			print("Tratando de inicializar en el puerto:", self.port, "...")
			self.socket.bind(self.my_dir)

		except Exception as e:
			print("No se pudo establecer conexión con el puerto:", self.port)
			self.stop()
			sys.exit(1)

		print("Conexión exitosa con el puerto:", self.port, "!")
		self.esperar_conexion()

	#Baja el servidor
	def stop(self):
		try:
			print("Apagando el servidor...")

		except Exception as e:
	         print("No se puede cerrar conexión con el socket",e)

	def esperar_conexion(self):
		while True:
			self.socket.listen(3)
			conn, addr = self.socket.accept()

			print("Got connection from:", addr)
			data = conn.recv(1024) #receive data from client
			request = bytes.decode(data) #decode it to string
			
			dictionary = parse(request)
			#print(dictionary)
			if "Content-Length" in dictionary:
				bodyLength = dictionary["Content-Length"]
				#TO-DO: get body for POST methods
			


def graceful_shutdown(sig, dummy):
	server.stop() #shut down the server
	sys.exit(1)

signal.signal(signal.SIGINT, graceful_shutdown)
print ("Inicializando servidor...")
server = ServerHTTP()  		# construct server object
server.serve() 	# aquire the socket



