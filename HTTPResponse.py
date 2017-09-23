# Responde con el código correspondiente dependiendo del
# request HTTP
import time
import os

def readFromFile(file):
	try:
		file_handler = open(file,'rb')
		message = file_handler.read() # read file content                       
		file_handler.close()
	except Exception as e:
		message = b"<html><body><h1>404 Not Found</h1></body></html>"
	return message

def createHeaders(file, typeFile):
	binaryFile = readFromFile(file)
	headers = ""
	timeNow 		= time.strftime("%c")
	headers 		+= "Date: " + timeNow + "\r\n"
	headers 		+= "Server: ServerPython/1.0\r\n"
	headers 		+= "Content-Length: " + str(len(binaryFile)) + "\r\n"
	headers			+= "Content-Type: " + typeFile + "\r\n"
	return headers

def responseOkDefault():
	indexPath 	 = os.getcwd() + "/index.html"
	message		 = readFromFile(indexPath)
	okStatus 	 = "HTTP/1.1 200 OK\r\n"
	headers 	 = createHeaders(indexPath, "text/html")
	okResponse 	 = okStatus + headers + "\r\n"
	httpResponse = okResponse.encode() + message
	return httpResponse

def responseOK(file, typeFile, method):
	if method != "HEAD":
		message = readFromFile(file)
	okStatus 	 = "HTTP/1.1 200 OK\r\n"
	headers 	 = createHeaders(file, typeFile)
	okResponse 	 = okStatus + headers + "\r\n"
	if method != "HEAD":
		httpResponse = okResponse.encode() + message
	else:
		httpResponse = okResponse.encode()
	return httpResponse

def responseNotFound():
	headers 		= ""
	timeNow 		= time.strftime("%c")
	notFoundBody 	= "<html><body><h1>404 Not Found</h1></body></html>"
	message 		= notFoundBody.encode()
	notFoundStatus	= "HTTP/1.1 404 Not Found\r\n"
	headers += "Date: " + timeNow + "\r\n"
	headers += "Server: ServerPython/1.0\r\n"
	headers += "Content-Length: " + str(len(message)) + "\r\n"
	headers += "Content-Type: text/html\r\n"
	notFoundResponse = notFoundStatus + headers + "\r\n"
	httpResponse = notFoundResponse.encode() + message
	return httpResponse

def responseNotAcceptable(file, typeFile):
	notAcceptableBody 		= "<html><body><h1>406 Not Acceptable</h1></body></html>"
	message 				= notAcceptableBody.encode()
	notAcceptableStatus 	= "HTTP/1.1 406 Not Acceptable\r\n"
	headers 				= createHeaders(file, typeFile)
	notAcceptableResponse 	= notAcceptableStatus + headers + "\r\n"
	httpResponse 			= notAcceptableResponse.encode() + message
	return httpResponse

def responseNotImplemented():
	headers 				= ""
	timeNow 				= time.strftime("%c")
	notImplementedBody 		= "<html><body><h1>501 Not Implemented</h1></body></html>"
	message					= notImplementedBody.encode()
	notImplementedStatus 	= "HTTP/1.1 501 Not Implemented\r\n"
	headers += "Date: " + timeNow + "\r\n"
	headers += "Server: ServerPython/1.0\r\n"
	headers += "Content-Length: " + str(len(message)) + "\r\n"
	headers += "Content-Type: text/html\r\n"
	notImplementedResponse  = notImplementedStatus + headers + "\r\n"
	httpResponse 			= notImplementedResponse.encode() + message
	return httpResponse

#

