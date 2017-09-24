# Manejador de metodos de HTTP.
# Importa los metodos que generan respuestas para los requests
from HTTPResponse import responseOK, responseOkDefault, responseNotFound, responseNotAcceptable, responseNotImplemented
import os # para obtener el path de un archivo
from pathlib import Path # se utiliza para determinar si existe o no un archivo
import mimetypes # para determinar el mimetype del archivo en el request

# obtiene el mimetype de un archivo. 
# Si es None se le asigna "text/html" esto para cuando se hace GET sin especificar direccion (index) 
def getMimeType(filePath):
	guessed_type = mimetypes.guess_type(filePath)
	mimeType = guessed_type[0]
	if mimeType == None:
		mimeType = "text/html"
	return mimeType

# Metodo que se encagar de analizar el metodo, la direccion y el header Accept
# para determinar que respuesta debe dar el servidor 
def handle(requestDictionary):
	method = requestDictionary["METHOD"]
	if method == "GET" or method == "HEAD" or method == "POST": # para saber si hacer 501
		filePath = os.getcwd() + requestDictionary["URI"] # obtiene la direccion del archivo
		path = Path(filePath)
		if path.exists(): # para saber si hacer 404
			fileType = getMimeType(filePath)
			acceptHeader = requestDictionary["Accept"]
			if fileType in acceptHeader or  "*/*" in acceptHeader: # para saber si hacer 406
				if requestDictionary["URI"] != "/": # para saber si hacer 200 para index o para otro archivo
					response = responseOK(filePath, fileType, method)
				else: 
					response = responseOkDefault()
			else:
				response = responseNotAcceptable(filePath, fileType)	
		else:
			response = responseNotFound()
	else:
		response = responseNotImplemented()
	return response
			


	
#HTTPMH = HTTPMethodHandler()