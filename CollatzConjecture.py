def getInput():

	while True:
		try:
			num = int(input('Input: '))
		except ValueError:
			print('A whole number, please!!')
		else:
			return num

def collatzConjecture():

	num = getInput()

	while (num != 1):

		if num % 2 == 0:
			num/=2
			num = int(num)
		else:
			num*=3
			num+=1
		print(num)

def main():

	while True:
		collatzConjecture()

main()