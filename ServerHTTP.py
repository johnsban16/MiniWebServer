#Imports--------------------------
import socket # para escuchar a los clientes
import signal # para interrumpir al servidor
import time   # para obtener la fecha
import sys    # para exits y ese tipo de funciones
from HTTPMethodHandler import handle #importa el metodo que devuele una respuesta
from HTTPParser import parse #"descompone" el request en headers y sus valores
from RequestsLog import writeInLog #escribe en el log de request que se han hecho al servidor
#---------------------------------

PORT = 8000 # Puerto por el cual escucha el servidor.
			# Se puede modificar por si se desea escuchar en otro puerto.

class ServerHTTP:

	#Contructor de  la clase
	def __init__(self):
		self.host = ''
		self.port = PORT
		self.my_dir = (self.host, self.port)

	#Levanta el servidor (Aqui es donde se inicializa el socket que recibe los request)
	def serve(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			print("Trying to initialize in PORT:", self.port, "...")
			self.socket.bind(self.my_dir)

		except Exception as e:
			print("Can't establish connection on PORT:", self.port)
			self.stop()
			sys.exit(1)

		print("successful connection on PORT:", self.port, "!")
		self.wait_connection()

	#Apaga el servidor
	def stop(self):
		try:
			print("Turning off server...")

		except Exception as e:
	         print("Can't close connection with socket",e)

	#Se encicla esperando conexiones con el servidor
	def wait_connection(self):
		while True:
			self.socket.listen(3)
			conn, addr = self.socket.accept()

			print("Got connection from:", addr)
			data = conn.recv(1024) #se reciben los datos del request es byte
			request = bytes.decode(data) #se convierten a string
			print(request)

			dictionary = parse(request) #llamado al metodo que separa los headers
			httpResponse = handle(dictionary) #llamado al metodo que determina la respuesta para el request
			sendRequest = conn.send(httpResponse)
			if sendRequest == 0:
				raise RuntimeError("Unable to connect with socket...")
			writeInLog(dictionary) #escribe en el log de request
			conn.close() #cierra la conexion con el socket
			
# Se supone que esto es un CTRL + C que interrumpe el proceso del servidor
# No funciona muy bien. Hay que precionar CTRL + C y luego enviar un request para que se apague el servidor
def graceful_shutdown(signum, frame):
	signal.signal(signal.SIGINT, original_sigint)
	server.stop() #apaga el servidor
	sys.exit(1)

original_sigint = signal.getsignal(signal.SIGINT) #Triggerea la señal que activa el CTRL + C
signal.signal(signal.SIGINT, graceful_shutdown)
print ("Turning on server...") 
server = ServerHTTP()  # crea un objeto ServerHTTP
server.serve() 	#levanta el objeto ServerHTTP

#http://localhost:8000/ejemplo.html?q=parametro1&q2=parametro2
#curl -X "DELETE" http://localhost:8000/ejemplo.html


