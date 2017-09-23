#Manejador de metodos de HTTP.
from HTTPResponse import responseOK, responseOkDefault, responseNotFound, responseNotAcceptable, responseNotImplemented
import os
from pathlib import Path
import mimetypes

def getMimeType(filePath):
	guessed_type = mimetypes.guess_type(filePath)
	mimeType = guessed_type[0]
	if mimeType == None:
		mimeType = "text/html"
	return mimeType

def handle(requestDictionary):
	method = requestDictionary["METHOD"]
	if method == "GET" or method == "HEAD" or method == "POST":
		filePath = os.getcwd() + requestDictionary["URI"]
		path = Path(filePath)
		if path.exists():
			fileType = getMimeType(filePath)
			acceptHeader = requestDictionary["Accept"]
			if fileType in acceptHeader or  "*/*" in acceptHeader:
				if requestDictionary["URI"] != "/":
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