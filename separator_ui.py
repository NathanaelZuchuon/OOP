# This is the thousands separator:
# '10000' -> '10 000'

def sep(value):
	return '{:,}'.format(value).replace(',', '  ')