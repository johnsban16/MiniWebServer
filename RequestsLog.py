# Escribe el request en el archivo de logs
import time # para obtener la fecha

# Se le envía el diccionario con todos los headers del request y los guarda en el log
def writeInLog(dictionary):
	timeNow = time.strftime("%c") #timestamp del tiempo actual
	timestamp = "Timestamp: " + timeNow + "\n"
	with open ('log.txt', 'a') as fp: #escribe en el archivo log.txt
		fp.write(timestamp)
		for p in dictionary.items():
			fp.write("%s:%s\n" % p)
		fp.write("------------------------------------------------------------------------------------------------\n")