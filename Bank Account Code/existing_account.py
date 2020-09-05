from collect_data import collect_data
from known_data import known_data

"""This function allows a user to connect to his account.
"""

def existing_account():

	print('\nCONNEXION A UN COMPTE EXISTANT')

	try:
		user, code, limit, amount, card, msg, time, index = collect_data()

	except TypeError:
		pass

	else:
		known_data(user, code, amount, limit, card, msg, time, index)