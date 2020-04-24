import sys


def input_validation(value, msg):

	# This method forces the user to enter
	# positive integers because we are working with amounts.

	while type(value) is not int:

		try:

			value = int(input(msg))
			assert(value >= 0)
			return value

		except (ValueError, AssertionError):
			value = str(value)

def convert_to_string(value, msg, msg_error): # There must be an input.

	value = str(input(msg))

	while len(value) == 0:
		value = str(input(msg_error))

	return value

def axis():

	print("CREATION D'UN NOUVEAU COMPTE BANCAIRE".center(80))
	var = None

	user = convert_to_string(var, 'Entrer votre nom: ', 'Entrer votre nom: ')
	code = convert_to_string(var, 'Entrer votre code: ', 'Entrer votre code: ')
	limit = input_validation(var, 'Entrer le montant minimal à rester dans votre compte: ')
	amount = input_validation(var, 'Entrer le montant de création du compte: ')

	while limit > amount: # To respect the limit.
		amount = input_validation(var, 'Veuillez entrer un montant excédant le montant limite: ')

	print("\nBonjour %s, quelle opération voudriez-vous effectuer sur votre compte ?" % (user))


	"""

	This class is the user's account.
	It contains all the actions it can perform.
	These actions are defined as methods.

	"""

	class Guichet:

		# No amount has yet been entered
		deposit_amount = []
		withdraw_amount = []

		# No operation has yet been performed.
		consultation_number = deposit_number = withdraw_number = 0

		def __init__(self, user, code, amount, limit):

			self.user = user
			self.code = code
			self.amount = amount
			self.limit = limit

			self._var = None
			self._times = None
			self._single_amount = None

		def text_one(self, amount):

			if amount == 0: # 0 is not considered to be a real amount.
				print("\nVotre solde vaut toujours %s et l'opération ne sera pas prise en compte." % (self.amount))

			return amount == 0

		def text_two(self):

			print("\nVotre solde s'élève désormais à %s ." % (self.amount))

		def cancellation_check(self, value):

			if value.upper() == "X": # To cancel the operation in progress.
				return True

			else:
				return False

		def cancellation(self, value):

			if guichet.cancellation_check(value):
				guichet.display_formatting()

				return True

			else:
				return False

		def display_formatting(self):

			print('Opération annulée !', 'Voulez-vous effectuer une nouvelle opération ?', sep='\n\n')

		def information_about_cancellation(self):

			print("Pour annuler l'opération en cours, entrer 'X' ou 'x' ...")

		def convert_to_integer(self, value):

			return int(value)

		def return_type(self, value):

			return type(value)

		"""

		This method embellishes the historical
		by concatenating the amounts, eg:
		amounts: 10, 20, 10, 30, 20, 40.
		output: 2 of 10, 2 of 20, 1 of 30, and 1 of 40.

		"""

		def historical_formatting(self, list_amount):

			# To remove multiple same amounts.
			self._single_amount = list(set(list_amount))
			self._times = []

			add = self._times.append
			for i in range(len(self._single_amount)):

				# The number of times an amount has been entered.
				y = list_amount.count(self._single_amount[i])
				add(y)

			return [self._times, self._single_amount]

		def account_consultation(self):

			(guichet.consultation_number)+=1 # will return the number of account consultation
			print("\nVotre solde est de %s ." % (self.amount))

		def account_consultation_historical(self):

			if guichet.consultation_number == 0:
				print("\nVous n'avez pas effectué de consultation.")

			elif guichet.consultation_number == 1:
				print("\nVous avez effectué une consultation.")

			else:
				print("\nVous avez effectué %s consultations." % (guichet.consultation_number))

		def deposit(self):

			guichet.information_about_cancellation()

			msg_error = "Entrer le montant de dépôt: " ; msg = '\n'+msg_error
			new_amount = deposit_validation(guichet._var, msg, msg_error)

			if guichet.return_type(new_amount) is int:

				if guichet.text_one(new_amount):
					pass

				else:

					self.amount+=new_amount
					(guichet.deposit_number)+=1 # will return the number of deposit
					guichet.deposit_amount.append(new_amount) # will return the deposit amount
					guichet.text_two()

		def deposit_historical(self):

			historical = guichet.historical_formatting(guichet.deposit_amount)

			if guichet.deposit_number == 0:
				print("Vous n'avez pas effectué de dépôt.")

			elif guichet.deposit_number == 1:
				print("Vous avez effectué un dépôt de %s ." % (guichet.deposit_amount[0]))

			else:
				print("Vous avez effectué %s dépôts: " % (guichet.deposit_number), end = "")

				for i in range(len(historical[0])):

					set = (historical[0][i], historical[1][i])

					if i == len(historical[0]) - 1 and len(historical[0]) != 1:
						print("et %s de %s ." % set)

					elif len(historical[0]) == 1:
						print("%s de %s ." % set)

					else:
						print("%s de %s, " % set, end = "")

		def withdrawal_verification(self, amount, limit):

			if amount >= limit: # To respect the limit.
				return True

			else:
				return False

		def withdrawal(self):

			guichet.information_about_cancellation()

			msg_two = 'Entrer le montant de retrait: ' ; msg_one = '\n'+msg_two
			msg_error = 'Solde inférieur à la limite, entrer un nouveau montant de retrait: '
			new_amount = withdrawal_validation(guichet._var, msg_one, msg_two, msg_error)

			if guichet.return_type(new_amount) is int:

				if guichet.text_one(new_amount):
					pass

				else:

					self.amount-=new_amount
					(guichet.withdraw_number)+=1 # will return the number of withdraw
					guichet.withdraw_amount.append(new_amount) # will return the withdraw amount
					guichet.text_two()

		def withdrawal_history(self):

			historical = guichet.historical_formatting(guichet.withdraw_amount)

			if guichet.withdraw_number == 0:
				print("Vous n'avez pas effectué de retrait.")

			elif guichet.withdraw_number == 1:
				print("Vous avez effectué un retrait de %s ." % (guichet.withdraw_amount[0]))

			else:
				print("Vous avez effectué %s retraits: " % (guichet.withdraw_number), end = "")

				for i in range(len(historical[0])):

					set = (historical[0][i], historical[1][i])

					if i == len(historical[0]) - 1 and len(historical[0]) != 1:
						print("et %s de %s ." % set)

					elif len(historical[0]) == 1:
						print("%s de %s ." % set)

					else:
						print("%s de %s, " % set, end = "")

		def logout(self):

			# This is the transaction historical.
			# This method returns:
			# the number of operations performed,
			# and the concatenated amounts of each operation.

			guichet.account_consultation_historical()
			guichet.deposit_historical()
			guichet.withdrawal_history()
			guichet.account_consultation()

			print("\nÀ bientôt :)")
			sys.exit()

		def switcher(self, i):

			switcher = {'1': guichet.account_consultation,
						'2': guichet.deposit,
						'3': guichet.withdrawal,
						'4': guichet.logout}

			operation = switcher.get(i, lambda: print('Entrée invalide !'))
			return operation()

	guichet = Guichet(user, code, amount, limit)


	def deposit_validation(value, msg, msg_error):

		while True:

			res = convert_to_string(value, msg, msg_error)

			if guichet.cancellation(res):
				break

			else:

				try:

					res = guichet.convert_to_integer(res)
					assert(res >= 0)

				except (ValueError, AssertionError):
					pass

				else:
					return res

				finally:
					msg = msg_error

	def withdrawal_validation(value, msg_one, msg_two, msg_error):

		while True:

			res = convert_to_string(value, msg_one, msg_two)

			if guichet.cancellation(res):
				break

			else:

				try:
					msg_one = msg_two
					res = guichet.convert_to_integer(res)
					assert(res >= 0)

				except (ValueError, AssertionError):
					pass

				else:

					rest = guichet.amount - res

					if guichet.withdrawal_verification(rest, guichet.limit):
						return res

					else:
						msg_one = msg_error

	while True:

		# Operations that can be performed by the user.
		print("\n1. Consultation de compte", "2. Dépôt d'argent", "3. Retrait d'argent", "4. Déconnexion", sep='\n')

		num = str(input("\nVeuillez entrer le nombre correspondant... "))
		guichet.switcher(num) # To access the selected operation.

def main_method():
	axis()

main_method()
