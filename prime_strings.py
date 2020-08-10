def get_subString(text):

	subString = text[0]

	for i in range(1, len(text)-1):

		if text[i] != text[0]:
			pass
		else:
			break

		subString+=text[i]

	return subString

def validation(text, subString):

	i = 2
	while i <= len(text):

		if subString * i == text:
			break
		else:
			pass

		i+=1

	if i > len(text):
		return 'true'
	else:
		return 'false'

def getInput():

	text = str(input('Input: '))
	answer = validation(text, get_subString(text))

	print(f'Output: {answer}')

def main():

	while True:
		getInput()

main()