def convertToF(tempCel):
	tempFar = tempCel * (9/5) + 32
	return tempFar

if __name__ == '__main__':
	for i in range(20):
		print(convertToF(i))