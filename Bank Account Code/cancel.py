def information_about_cancellation():
	print("\nPour annuler l'opération en cours, entrer 'X' ou 'x' ...\n")

def display_formatting():
	print('\nOpération annulée !', 'Voulez-vous effectuer une nouvelle opération ?', sep='\n')

def cancellation_check(value):
	return True if value.upper() == "X" else False # To cancel the operation in process.

def cancellation(value):

	if cancellation_check(value):

		display_formatting()
		return True

	else:
		return False