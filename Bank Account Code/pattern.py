from datetime import datetime
from pandas import DataFrame
from sys import exit
from time import sleep

# All characters that should not appear in a username.
NOT_ALLOWED_CHARACTER = ["/", ":", "*", "?", '-', '~', ',', ';', '<', '>', '|', '"']

__author__ = 'Nathanaël Zuchuon'
__version__ = '1.2.0'

def code_validation(msg): # The user must enter a PIN code.

	nums = '0123456789' # The code is only numbers.
	while True:

		code = str(input(msg))

		if all([i in nums for i in code]) and len(code) == 4: # Only 4 numbers is necessary.
			return code

def bank_name():

	bname = '* By Zuch & Co. Bank *' # 'bname' refers to 'bank_name'.
	style = '**********************'
	print('', center_text(style), center_text(bname), center_text(style), sep='\n')

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

def center_text(text):
	return text.center(100)

"""This function lets me know which user it is.
An Exception will occur if it returns nothing
when it's called by the others:
TypeError: cannot unpack non-iterable NoneType object
"""

def collect_data():

	file_name = file()
	with read_mode(file_name) as data:
		users_data = file_content(data) # Returns a list of all the customers.

	################################### Their attributes ##########################################
	list_users = [convert_to_dict(users_data[i]).get('name') for i in range(len(users_data))]     #
	list_codes = [convert_to_dict(users_data[i]).get('password') for i in range(len(users_data))] #
	list_limit = [convert_to_dict(users_data[i]).get('limit') for i in range(len(users_data))]    #
	list_amount = [convert_to_dict(users_data[i]).get('amount') for i in range(len(users_data))]  #
	list_time = [convert_to_dict(users_data[i]).get('time') for i in range(len(users_data))]      #
	###############################################################################################

	attempt_user = attempt_code = 2

	information_about_cancellation()
	name = number_of_attempt(1, "nom d'utilisateur")

	if cancellation(name):
		return

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

	return name, password, list_limit[index], list_amount[index], list_time[index], index

def space(word): # To remove unconscious spaces

	"""The user can enter 'Michel ' without being aware of the last character
	which he entered and at the next reconnection he will be surprised
	that 'Michel' does not work: hence this function.
	"""

	return True if word.startswith(' ') or word.endswith(' ') else False

def convert_to_string(msg, invalid_char=NOT_ALLOWED_CHARACTER):

	while True:

		value = str(input(msg))

		if any([i in value for i in invalid_char]) or space(value):
			print(f"Les caractères suivants sont invalides: {' '.join(invalid_char)}\n")

		else:
			return value

"""This function allows the creation of a new bank account.
"""

def data_request():

	print("\nCREATION D'UN NOUVEAU COMPTE BANCAIRE")

	file_name = file()
	msg_user = 'Entrer votre nom: '
	msg_code = 'Entrer votre code à 4 chiffres: '

	with read_mode(file_name) as data:
		users_data = file_content(data)

	# This is the list of all users
	list_users = [convert_to_dict(users_data[i]).get('name') for i in range(len(users_data))]

	information_about_cancellation()
	user = convert_to_string(msg_user)

	if cancellation(user):
		return

	while user in list_users: # This avoids the creation of several accounts with the same name.

		print('Compte existant !!')

		information_about_cancellation()
		user = convert_to_string(msg_user)

		if cancellation(user):
			return

	code = code_validation(msg_code)
	limit = input_validation('Entrer le montant minimal à rester dans votre compte: ')
	amount = input_validation('Entrer le montant de création du compte: ')

	while limit > amount: # To respect the limit.
		amount = input_validation('Veuillez entrer un montant excédant le montant minimal du compte: ')

	amount-=limit
	with append_mode(file_name) as data:
		# Finally, we store in the file 'data.txt' the attributes of the account with their values.
		data.write(f"dict(name='{user}', password='{code}', limit={limit}, amount={amount}, time='{None}')\n")
#																									 ^
#															   The user has not yet been connected __|

	print('\nCompte créé avec succès:',
			f"   * Nom d'utilisateur: {user}",
			f"   * Mot de passe: {code}",
			f"   * Montant minimal à rester dans le compte: {sep(limit)}",
			f"   * Solde effectif du compte: {sep(amount)}", sep='\n')

"""This function allows the deletion of an account.
"""

def del_account():

	print("\nSUPPRESSION D'UN COMPTE EXISTANT")

	try:
		user, code, limit, amount, time, index = collect_data()

	except TypeError:
		pass

	else:

		file_name = file()
		modify_file(file_name, index, False, None)
		print('\nCompte supprimé avec succès !!')

def _help():
	print('Contacter la banque pour signaler le problème.',
		  'Adresse E-mail: nzuchuon@gmail.com', sep='\n')

def input_validation(msg, value=None):

	# This function forces the user
	# to enter positive integers.

	while type(value) is not int:

		try:

			value = int(input(msg))
			assert(value >= 0) # We are working with amounts.
			return value

		except (ValueError, AssertionError):
			value = None

def known_data(user, code, amount, limit, time, index):

	new_time = str(datetime.today()) # We will format the date for a better layout.

	if time == 'None':
		print(f"\nSalut {user}, quelle opération voudriez-vous effectuer sur votre compte ?")

	else:

		date = order(time[:10])
		print(	f"\nDernière connexion le {date} à {time[11:19]}",
				f"\n{salutation(int(new_time[11:13]))} {user}, "
				"quelle opération voudriez-vous effectuer sur votre compte ?")

	guichet = Guichet(user, code, amount, limit, new_time, index)
	while True:

		# Operations that can be performed by the user.
		print("\n1. Consultation de compte",
				"2. Dépôt d'argent",
				"3. Retrait d'argent",
				"4. Retrait du solde effectif",
				"5. Voir limite du compte",
				"6. Déconnexion", sep='\n')

		num = _input()
		guichet.switcher(num) # To access the selected operation.

		if num == '6': # The exit loop because '6' is the logout method.
			break

def convert_to_dict(statement):
	return eval(statement)

"""This function allows a user to connect to his account.
"""

def existing_account():

	print('\nCONNEXION A UN COMPTE EXISTANT')

	try:
		user, code, limit, amount, time, index = collect_data()

	except TypeError:
		pass

	else:
		known_data(user, code, amount, limit, time, index)

def read_mode(file):
	return open(file, "r")

def write_mode(file):
	return open(file, "w")

def append_mode(file):
	return open(file, "a")

def file_content(file):
	return file.readlines()

def file():
	return r'G:\\Object-Oriented Programming\\Bank Account Code\\data.txt'

def get():
	return str(input('\nVeuillez entrer le nombre correspondant... '))

def _input():
	return str(input('\n>>> '))

def logout():

	print('\nVotre fidélité, notre satisfaction :)')
	print('Déconnexion dans 5 secondes.')
	sleep(5)
	exit()

def main_menu():

	style = '***************************************'
	print('',
		  center_text(style),
		  center_text("*            MENU PRINCIPAL           *"),
		  center_text("*                                     *"),
		  center_text("* 1. CREATION D'UN NOUVEAU COMPTE     *"),
		  center_text("* 2. CONNEXION A UN COMPTE EXISTANT   *"),
		  center_text("* 3. MODIFICATION DES DONNÉES         *"),
		  center_text("* 4. TRANSFERT D'ARGENT               *"),
		  center_text("* 5. SUPPRESSION D'UN COMPTE EXISTANT *"),
		  center_text("* 6. DECONNEXION                      *"),
		  center_text("*                                     *"),
		  center_text(style), sep='\n')

"""This function allows the user to modify
some of his attributes (his name, ...etc).
"""

def modify_data():

	print('\nMODIFICATION DES DONNÉES')

	try:
		user, code, limit, amount, time, index = collect_data()

	except TypeError:
		pass

	else:

		print() # for the layout...
		msg_user = "Entrer votre nouveau nom d'utilisateur: "
		msg_code = "Entrer votre nouveau mot de passe: "
		msg_limit = "Entrer votre nouvelle limite: "
		file_name = file()

		with read_mode(file_name) as data:
			users_data = file_content(data)

		list_users = [convert_to_dict(users_data[i]).get('name') for i in range(len(users_data))]
		del list_users[index] # He can enter the same name.

		new_user = convert_to_string(msg_user)

		while new_user in list_users: # Checking the existence of the account.
			print('Compte existant\n')
			new_user = convert_to_string(msg_user)

		code = code_validation(msg_code)

		limit = input_validation(msg_limit)
		msg_limit = f"Limite supérieur au solde ({sep(amount)}), recommencer: "

		while amount < limit:
			limit = input_validation(msg_limit)

		guichet = Guichet(new_user, code, amount, limit, time, None)
		modify_file(file_name, index, True, guichet) # Update the values.

		print('\nDonnées modifiées avec succès:',
				f"   * Nouveau nom d'utilisateur: {new_user}",
				f"   * Nouveau mot de passe: {code}",
				f"   * Nouvelle limite: {sep(limit)}", sep='\n')

"""This function is used to update
the values of the attributes of a user.
"""

def modify_file(file, index, value, instance):

	with read_mode(file) as data:
		users_data = file_content(data)

	del users_data[index]

	if value is True:
		users_data.insert(index, f"dict(name='{instance.user}', password='{instance.code}', "
								+f"limit={instance.limit}, amount={instance.amount}, "
								+f"time='{instance.time}')\n")

	with write_mode(file) as data_deletion:
		pass

	with append_mode(file) as data_update:

		for item in users_data:
			data_update.write(item)

def new_account():
	data_request()

def number_of_attempt(attempt, text):

	print(f'Tentative {attempt} sur 3')
	data = str(input(f"Entrer votre {text}: "))
	return data

def order(date):

	date = list(date)

	year = date[:4]
	month = date[4:8]
	day = date[8:]

	month.extend(year)
	day.extend(month)

	return ''.join(day)

def salutation(time):
	return 'Bonjour' if time in range(6, 16) else 'Bonsoir'

# This is the thousands separator:
# '10000' -> '10 000'

def sep(value):
	return '{:,}'.format(value).replace(',', ' ')

"""This function allows the transfer
of money from one user to another.
"""

def transfer():

	print("\nTRANSFERT D'ARGENT")

	try:
		user, code, limit, amount, time, index = collect_data()

	except TypeError:
		pass

	else:

		file_name = file()
		with read_mode(file_name) as data:
			users_data = file_content(data)

		list_users = [convert_to_dict(users_data[i]).get('name') for i in range(len(users_data))]
		list_codes = [convert_to_dict(users_data[i]).get('password') for i in range(len(users_data))]
		list_limit = [convert_to_dict(users_data[i]).get('limit') for i in range(len(users_data))]
		list_amount = [convert_to_dict(users_data[i]).get('amount') for i in range(len(users_data))]
		list_time = [convert_to_dict(users_data[i]).get('time') for i in range(len(users_data))]

		attempt_user = 1
		
		################ Recipient verification ##################
		while attempt_user < 4:                                  #
			name = number_of_attempt(attempt_user, "receveur")   #
                                                                 #
			if name == user:                                     #
                                                                 #
				if attempt_user == 3:                            #
					print('Auto-transfert impossible !!\n')      #
					return                                       #
                                                                 #
				else:                                            #
					print('Auto-transfert impossible !!')        #
                                                                 #
			elif name not in list_users:                         #
				print('Compte inexistant !!')                    #
                                                                 #
			elif (name in list_users) and (name != user):        #
				break                                            #
                                                                 #
			if (attempt_user == 3) and (name == user):           #
				print('Auto-transfert impossible !!\n')          #
				return                                           #
                                                                 #
			if (name not in list_users) and (attempt_user == 3): #
				print('\nCompte inexistant !!')                  #
				help()                                           #
				return                                           #
                                                                 #
			attempt_user+=1                                      #
		##########################################################

		print() # for the layout...

		trans_amount = input_validation('Entrer le montant de transfert: ')
		while (amount-trans_amount) < limit:
			trans_amount = input_validation( f'Solde restant ({sep(amount-trans_amount)}) '
											+f'inférieur à la limite ({sep(limit)}), recommencer: ')

		index_name = list_users.index(name)
		amount-=trans_amount
		list_amount[index_name]+=trans_amount

		guichet_user = Guichet(user, code, amount, limit, time, index)
		guichet_name = Guichet(name, list_codes[index_name], 
			list_amount[index_name], list_limit[index_name], 
			list_time[index_name], index_name)

		modify_file(file_name, index, True, guichet_user)
		modify_file(file_name, index_name, True, guichet_name)

		area = {"DE": [user],
				"À": [name],
				"MONTANT": [sep(trans_amount)]}

		brics = DataFrame(area)
		brics.index = ['*']

		print('', brics, sep='\n')
		print(f'\n* Solde restant: {sep(amount)}', end='\n\n')

"""This class is the user's account.
It contains all the actions it can perform.
These actions are defined as methods.
"""

class Guichet:

	def __init__(self, user, code, amount, limit, time, index):

		self.user = user
		self.code = code
		self.amount = amount
		self.limit = limit
		self.time = time # Used to store the last 'date-time' the user has been connected.
		self.index = index # The position of the user in the store file.

		self._deposit_amount = []
		self._withdraw_amount = [] # No amount has yet been entered.

		self._consultation_number = 0 #
		self._deposit_number = 0      # No operation has yet been performed.
		self._withdraw_number = 0     #

	def text_one(self, amount):

		stat = (amount == 0) # 0 is not considered to be a real amount.

		if stat:
			print(f"\nVotre solde vaut toujours {sep(self.amount)} "
				  +"et l'opération ne sera pas prise en compte.")

		return stat

	def text_two(self):
		print(f"\nVotre solde s'élève désormais à {sep(self.amount)} .")

	def see_limit(self):
		print(f"\nLe montant limite de votre compte est {sep(self.limit)} .")

	def balance(self):
		print(f"\nVotre solde est de {sep(self.amount)} .")

	def convert_to_integer(self, value):
		return int(value)

	def return_type(self, value):
		return type(value)

	def convert_to_string(self, msg):
		return str(input(msg))

	"""This method embellishes the historical
	by concatenating the amounts, eg:
	amounts: 10, 20, 10, 30, 20, 40.
	output: 2 of 10, 2 of 20, 1 of 30, and 1 of 40.
	"""

	def historical_formatting(self, list_amount):

		# To remove multiple same amounts.
		single_amount = list(set(list_amount))
		times = []

		add = times.append
		for i in range(len(single_amount)):

			# The number of times an amount has been entered.
			y = list_amount.count(single_amount[i])
			add(y)

		return [times, single_amount]

	def history(self, list_amount, operation):

		historical = self.historical_formatting(list_amount)
		max_index = len(historical[0])
		area = {}

		if max_index == 0:

			style = '~'
			new_style = f'Aucun {operation} effectué.'
			print(new_style, style * len(pattern), sep='\n')

		else:

			for i in range(max_index):
				area.update({sep(historical[1][i]): [historical[0][i]]})

			brics = DataFrame(area)
			brics.index = [f'Nombre de {operation}']
			print('', brics, sep='\n', end='\n\n')

	def action(self, var, list_amount, new_amount):

		var+=1
		list_amount.append(new_amount)
		self.text_two()	

	def operation(self, method, msg, var, list_amount, sign):

		information_about_cancellation()
		new_amount = method(msg)

		if self.return_type(new_amount) is int:

			if self.text_one(new_amount):
				pass

			else:

				exec(f'self.amount{sign}={new_amount}')
				self.action(var, list_amount, new_amount)

	def account_consultation(self):

		(self._consultation_number)+=1
		self.balance()

	def account_consultation_historical(self):

		global pattern

		style = '~'
		new_style = f'{self._consultation_number} consultation(s) effectuée(s).'
		print('', style * len(new_style), new_style, style * len(new_style), sep='\n')

		pattern = new_style

	def deposit(self):

		msg = "Entrer le montant de dépôt: "
		self.operation(self.deposit_validation, msg, self._deposit_number, self._deposit_amount, '+')

	def deposit_historical(self):
		self.history(self._deposit_amount, 'dépôts')

	def withdrawal_verification(self, amount, limit):
		return True if amount >= limit else False # To respect the limit.

	def withdrawal(self):

		msg = 'Entrer le montant de retrait: '
		self.operation(self.withdrawal_validation, msg, self._withdraw_number, self._withdraw_amount, '-')

	def all_withdrawal(self):

		new_amount = self.amount - self.limit

		if self.text_one(new_amount):
			pass

		else:

			self.amount = self.limit
			self.action(self._withdraw_number, self._withdraw_amount, new_amount)

	def withdrawal_history(self):
		self.history(self._withdraw_amount, 'retraits')

	def logout(self):

		"""This is the transaction historical.
		This method returns:
		the number of operations performed,
		and the concatenated amounts of each operation.
		"""

		self.account_consultation_historical()
		self.deposit_historical()
		self.withdrawal_history()
		self.balance()

		file_name = file()
		modify_file(file_name, self.index, 
			True, Guichet(self.user, self.code, self.amount, self.limit, self.time, None))
		print(f"À bientôt {self.user} .")

	def switcher(self, i):

		switcher = {'1': self.account_consultation,
					'2': self.deposit,
					'3': self.withdrawal,
					'4': self.all_withdrawal,
					'5': self.see_limit,
					'6': self.logout}

		operation = switcher.get(i, lambda: print('Entrée invalide !'))
		return operation()

	def deposit_validation(self, msg):

		while True:

			value = self.convert_to_string(msg)

			if cancellation(value):
				break

			else:

				try:

					value = self.convert_to_integer(value)
					assert(value >= 0)

				except (ValueError, AssertionError):
					pass

				else:
					return value

	def withdrawal_validation(self, msg, msg_error=''):

		msg_error = msg

		while True:

			value = self.convert_to_string(msg)

			if cancellation(value):
				break

			else:

				try:

					msg = msg_error
					value = self.convert_to_integer(value)
					assert(value >= 0)

				except (ValueError, AssertionError):
					pass

				else:

					rest = self.amount - value

					if self.withdrawal_verification(rest, self.limit):
						return value

					else:
						msg = (f"Votre solde s'élèvera à {sep(rest)} inférieur à la limite, "
							   +"entrer un nouveau montant de retrait: ")

def switcher(i):

	switcher = {'1': new_account,
				'2': existing_account,
				'3': modify_data,
				'4': transfer,
				'5': del_account,
				'6': logout}

	operation = switcher.get(i, lambda: print('Entrée invalide !'))
	return operation()

def main_method():
	bank_name()

	while True:
		main_menu()
		num = get()
		switcher(num)

main_method()