def min_length(text, length=5):
	return True if len(text) >= length else False

def max_length(text, length=10):
	return True if len(text) <= length else False

def contains_number(text):
	numbers = '123456789'
	return True if any([i in numbers for i in text]) else False

def contains_uppercase_string(text):
	uppers = 'ABCDEFGHJIKLMNOPQRSTUVWXYZ'
	return True if any([i in uppers for i in text]) else False

def contains_special_char(text, char=['&', '+', '@', '$', '#', '%', '\'',
									'-', '/', '~', '\\', '!', '_', '*',
									]
									):
	return True if any([i in char for i in text]) else False

def contains_space(text):
	return True if ' ' not in text else False

def return_answer(*args):
	return 'true' if all([i is True for i in args]) else 'false'

def getInput():

	text = str(input('Input: '))
	answer = return_answer(
		min_length(text),
		max_length(text),
		contains_number(text),
		contains_special_char(text),
		contains_space(text),
		contains_uppercase_string(text),
		)
	print(f'Output: {answer}')

def main():

	while True:
		getInput()

main()