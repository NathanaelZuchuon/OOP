from __init__ import Guichet
from get_input import _input
from datetime import datetime
from order import order
from order import salutation
from modify_file import return_costs
from order import last_connexion
from currenties import currentie
from separator import sep

def new_date():
	return str(datetime.today()) # We will format the date for a better layout.

def which_operation(user):

	new_time = new_date()
	print(f"\n{salutation(int(new_time[11:13]))} {user}, "
			"quelle opération voudriez-vous effectuer sur votre compte ?")

def known_data(user, code, amount, limit, card, msg, time, index):

	if time == '':
		which_operation(user)

	else:

		last_connexion(time)
		which_operation(user)

	if msg == []:
		pass

	else:

		print() # for the layout...
		for i in range(len(msg)):
			for k, v in msg[i].items():
				print(f'{k} vous a transféré une somme de:\t\t{currentie(sep(v))}')

	new_time = new_date()
	guichet = Guichet(user, code, amount, limit, card, msg, new_time, index)

	while True:

		# Operations that can be performed by the user.
		print("\n1. Consultation de compte",
				"2. Dépôt d'argent",
				"3. Retrait d'argent",
				"4. Retrait du solde effectif",
				"5. Voir limite du compte",
				"6. Voir information sur la carte",
				"7. Voir total des frais",
				"8. Déconnexion", sep='\n')

		num = _input()
		guichet.switcher(num) # To access the selected operation.

		if num == '8': # The exit loop because '7' is the logout method.
			break