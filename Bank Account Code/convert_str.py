from _char import NOT_ALLOWED_CHARACTER

def space(word): # To remove unconscious spaces

	"""The user can enter 'Michel ' without being aware of the last character
	which he entered and at the next reconnection he will be surprised
	that 'Michel' does not work: hence this function.
	"""

	return True if word.startswith(' ') or word.endswith(' ') or len(word) == 0 else False

def convert_to_string(msg, invalid_char=NOT_ALLOWED_CHARACTER):

	while True:

		value = str(input(msg))

		if any([i in value for i in invalid_char]) or space(value):
			print(f"Les caractères suivants sont invalides: {' '.join(invalid_char)}\n")

		else:
			return value