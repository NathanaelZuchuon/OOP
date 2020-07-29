from order_ui import order
from separator_ui import sep
from datetime import datetime
from currenties import currentie

def new_date():
	return str(datetime.today()) # We will format the date for a better layout.

def transfer(msg):

	var = 'vous a transféré une somme de'

	date = new_date()
	j = order(date[:10])[1]

	for s in range(len(msg)):

		for k, v in msg[s].items():

			i = order(v[1][:10])[1]
			_format = f'{k} {var} {currentie(sep(v[0]))}'

			if i == j:

				return _format + f' aujourd\'hui à {v[1][11:19]}'

			elif i == (j-1):

				return _format + f' hier à {v[1][11:19]}'

			else:

				return _format + f' {order(v[1][:10])[0]} à {v[1][11:19]}'