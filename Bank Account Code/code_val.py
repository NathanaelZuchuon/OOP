def code_validation(msg): # The user must enter a PIN code.

	nums = '0123456789' # The code is only numbers.
	while True:

		code = str(input(msg))

		if all([i in nums for i in code]) and len(code) == 4: # Only 4 numbers is necessary.
			return code