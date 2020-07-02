from data import _card
from currenties import currentie
from separator import sep

def input_validation(msg, card, i, value=None):

	_min = _card(card)

	if i is True:
		pass

	else:
		print(f'\nVous ne pouvez pas entrer moins de{currentie(sep(_min))} .\n')

	while type(value) is not int:

		try:

			value = int(input(msg))
			assert(value >= _min)
			return value

		except (ValueError, AssertionError):
			value = None