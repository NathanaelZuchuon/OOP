import data

from help import _help
from number_of_attempt import number_of_attempt
from cancel import cancellation
from cancel import information_about_cancellation

"""This function lets me know which user it is.
An Exception will occur if it returns nothing
when it's called by the others:
TypeError: cannot unpack non-iterable NoneType object
"""

def collect_data():

	attempt_user = attempt_code = 2

	information_about_cancellation()
	name = number_of_attempt(1, "nom d'utilisateur")

	if cancellation(name):
		return

	####### Their attributes #####
	list_users = data.name()     #
	list_codes = data.password() #
	list_limit = data.limit()    #
	list_amount = data.amount()  #
	list_time = data.time()      #
	list_card = data.card()      #
	list_msg = data.msg()        #
	##############################

	while name not in list_users: # Checking the existence of the account.

		print('Compte inexistant !!')

		information_about_cancellation()
		name = number_of_attempt(attempt_user, "nom d'utilisateur")

		if cancellation(name):
			return

		if (attempt_user == 3) and (name not in list_users):
			print('\nCompte inexistant !!')
			_help()
			return

		attempt_user+=1

	index = list_users.index(name)

	password = number_of_attempt(1, "mot de passe")
	while password != list_codes[index]: # Password verification.

		print('Mot de passe incorrect !!')
		password = number_of_attempt(attempt_code, "mot de passe")

		if (attempt_code == 3) and (password != list_codes[index]):
			print('\nMot de passe incorrect !!')
			_help()
			return

		attempt_code+=1

	return name, password, list_limit[index], list_amount[index], list_card[index], list_msg[index], list_time[index], index