def convertToF(tempCel):
	tempFar = (tempCel * 9)/5 + 32
	return tempFar

def convertToC(tempFar):
	tempCel = (tempFar - 32) / (9/5)
	return tempCel

if __name__ == '__main__':
	for i in range(20):
		print(convertToF(i))
	for i in range(20):
		print(convertToC(i))
