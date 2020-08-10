def divisor(num):

	num = str(num)
	last_digit = len(num) - 1

	return int(num[0] + num[last_digit])

def validator(num):
	num = str(num)
	return True if len(num) >= 3 else False

def gapful_num(num, divisor):
	return 'true' if num % divisor == 0 else 'false'

def main():

	while True:

		try:
			num = int(input('Input: '))
		except ValueError:
			print('Entrer a number, please !!')
		else:

			if validator(num):
				print(f'Output: {gapful_num(num, divisor(num))}')
			else:
				print('At least three numbers')

main()