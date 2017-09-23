import time
import json

def writeInLog(dictionary):
	timeNow = time.strftime("%c")
	timestamp = "Timestamp: " + timeNow + "\n"
	with open ('log.txt', 'a') as fp:
		fp.write(timestamp)
		for p in dictionary.items():
			fp.write("%s:%s\n" % p)
		fp.write("------------------------------------------------------------------------------------------------\n")