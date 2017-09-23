#Imports--------------------------
import socket
import signal
import time
import sys
from HTTPMethodHandler import handle
#import HTTPResponse
from HTTPParser import parse
from logCSV import writeInLog
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
		self.wait_connection()

	#Baja el servidor
	def stop(self):
		try:
			print("Apagando el servidor...")

		except Exception as e:
	         print("No se puede cerrar conexión con el socket",e)

	def wait_connection(self):
		while True:
			self.socket.listen(3)
			conn, addr = self.socket.accept()

			print("Recibí conexión desde:", addr)
			data = conn.recv(1024) #receive data from client
			request = bytes.decode(data) #decode it to string
			print(request)
			
			dictionary = parse(request)
			handle(dictionary)
			httpResponse = handle(dictionary)
			#TO-DO: guardar en bitacora
			sendRequest = conn.send(httpResponse)
			print (httpResponse)
			if sendRequest == 0:
				raise RuntimeError("socket connection broken")
			writeInLog(dictionary)
			conn.close()


			

def graceful_shutdown(signum, frame):
	signal.signal(signal.SIGINT, original_sigint)
	server.stop() #shut down the server
	sys.exit(1)

original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, graceful_shutdown)
print ("Inicializando servidor...")
server = ServerHTTP()  		# construct server object
server.serve() 	# aquire the socket

#http://localhost:8000/ejemplo.html?q=parametro1&q2=parametro2
#curl -X "DELETE" http://localhost:8000/ejemplo.html


