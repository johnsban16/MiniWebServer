# Parser de HTTP. Crea un diccionario con el método, la versión de HTTP, la URI
# y los headers del resto del request
def parse(strRequest):
	requestParts = strRequest.split('\r\n')
	requestFirstLine = requestParts[0]

	# Separa la primera línea del request para obtener METHOD, HTTPVERSION y URI 
	def parseRequetsLine(requestLine):
		requestLineParts = requestLine.split(" ")
		requestDic = 	{"METHOD": requestLineParts[0],
						 "HTTPVERSION": requestLineParts[2]}
		if requestLineParts[1].find("?") == -1:
			requestDic.update({"URI":requestLineParts[1]})
		else:
			uri = requestLineParts[1].split("?")
			requestDic.update({ "URI":uri[0],
						   "DATA":uri[1]})
		return requestDic

	#Separa el resto del request en encabezados y su valor.
	def parseHeaders(requestDic, requestParts):
		for i in range (1, len(requestParts)-2):
			headerParts = requestParts[i].split(": ")
			requestDic.update({headerParts[0]: headerParts[1]})
		return requestDic

	#Agrega el BODY al diccionario (solo si el request es POST)
	def parseBody(requestDic,requestParts):
		requestBody = requestParts[len(requestParts)-1]
		requestDic.update({"BODY":requestBody})
		return requestDic


	requestDictionary = parseRequetsLine(requestFirstLine)
	requestDictionary = parseHeaders(requestDictionary, requestParts)
	if requestDictionary["METHOD"] == "POST":
		requestDictionary = parseBody(requestDictionary, requestParts)
	return requestDictionary



#parser = HTTPPaser()
#dic = parser.parse(str)
#print(dic)