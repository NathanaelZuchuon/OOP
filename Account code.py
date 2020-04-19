import sys


def except_ValueError(value): # There must be an entrance.
		
	if len(value) == 0 or ('-' in value) or ('+' in value): # To reject negative numbers
		return True
	else:
		return False

def except_TypeError(value):

	# The entrance must not be: a mixture of number and letter
	# and different from 'X' or 'x'.

	try:
		int(value)
	except ValueError:
		return True
	else:
		return False


class Historical:

	"""
	This class embellishes the historical
	by concatenating the amounts, eg:
	amounts: 10, 20, 10, 30, 20, 40.
	output: 2 of 10, 2 of 20, 1 of 30, and 1 of 40.

	"""

	def __init__(self, list_amount):
		self.list_amount = list_amount
		self._times = None
		self._unique_amount = None

	def historical_formatting(self):

		self._unique_amount = list(set(self.list_amount)) # To remove multiple same amounts.

		self._times = []
		add = self._times.append
		for i in range(len(self._unique_amount)):
			y = self.list_amount.count(self._unique_amount[i]) # The number of times an amount has been entered.
			add(y)


class Guichet:

	"""
	This class is the user's account.
	It contains all the actions it can perform.
	These actions are defined as methods.

	"""

	deposit_amount = []
	withdraw_amount = []
	consultation_number = deposit_number = withdraw_number = 0 # Because no operation has yet been performed.

	def __init__(self, user, code, amount, limit):

		self.user = user
		self.code = code
		self.amount = amount
		self.limit = limit

	def func(self):

		guichet.display_formatting()
		guichet.main()

	def text_one(self, amount):

		if amount == 0: # 0 is not considered to be a real amount.
			print("Votre solde vaut toujours %s et l'opération ne sera pas prise en compte." % (self.amount))

		return amount == 0

	def text_two(self):

		print("Votre solde s'élève désormais à %s ." % (self.amount))

	def cancellation_check(self, value):

		if value.upper() == "X": # To cancel the operation in progress.
			return True
		else:
			return False

	def display_formatting(self):

		print("Opération annulée !\n\nVoulez-vous effectuer une nouvelle opération ?")

	def information_about_cancellation(self):

		print("Pour annuler l'opération en cours, entrer 'X' ou 'x' ...")

	def str_to_int(self, value):

		return int(value)

	def account_consultation(self):

		(guichet.consultation_number)+=1 # will return the number of account consultation
		print("Votre solde est de %s ." % (self.amount))

	def account_consultation_historical(self):

		if guichet.consultation_number == 0:
			print("\nVous n'avez pas effectué de consultation.")
		elif guichet.consultation_number == 1:
			print("\nVous avez effectué une consultation.")
		else:
			print("\nVous avez effectué %s consultations." % (guichet.consultation_number))

	def deposit(self):

		guichet.information_about_cancellation()
		new_amount = str(input("\nEntrer le montant de dépôt: "))

		if guichet.cancellation_check(new_amount):
			guichet.func()

		else:

			while except_ValueError(new_amount) or except_TypeError(new_amount): 

				new_amount = str(input("Entrer le montant de dépôt: "))
			
				if guichet.cancellation_check(new_amount):
					guichet.func()
					break

		if except_TypeError(new_amount) == False:

			# At this level the input is a number-string, eg: '100' .
			# Hence the call of the 'str_to_int' method
			new_amount = guichet.str_to_int(new_amount)

			if guichet.text_one(new_amount):
				pass

			else:

				self.amount+=new_amount
				(guichet.deposit_number)+=1 # will return the number of deposit
				guichet.deposit_amount.append(new_amount) # will return the deposit amount
				guichet.text_two()
		else:
			pass

	def deposit_historical(self):

		historical = Historical(guichet.deposit_amount)
		historical.historical_formatting()

		if guichet.deposit_number == 0:
			print("Vous n'avez pas effectué de dépôt.")
		elif guichet.deposit_number == 1:
			print("Vous avez effectué un dépôt de %s ." % (guichet.deposit_amount[0]))
		else:
			print("Vous avez effectué %s dépôts: " % (guichet.deposit_number), end = "")

			for i in range(len(historical._times)):

				if i == len(historical._times) - 1:
					print("et %s de %s ." % (historical._times[i], historical._unique_amount[i]))
				elif len(historical._times) == 1:
					print("%s de %s." % (historical._times[i], historical._unique_amount[i]))
				else:
					print("%s de %s, " % (historical._times[i], historical._unique_amount[i]), end = "")

	def withdrawal_verification_one(self, amount, limit):

		if (amount<limit):
			return True
		else:
			return False

	def withdrawal_verification_two(self, amount, limit):

		if (amount>=limit):
			return True
		else:
			return False

	def withdraw(self):

		guichet.information_about_cancellation()
		new_amount = str(input("\nEntrer le montant de retrait: "))

		if guichet.cancellation_check(new_amount):
			guichet.func()

		else:

			while except_ValueError(new_amount) or except_TypeError(new_amount):

				new_amount = str(input("Entrer le montant de retrait: "))

				if guichet.cancellation_check(new_amount):
					guichet.func()
					break

		if except_TypeError(new_amount) == False:

			new_amount = guichet.str_to_int(new_amount)
			
			while guichet.withdrawal_verification_one((self.amount - new_amount), self.limit):

				i = guichet.str_to_int(new_amount)
				new_amount = str(input("Votre solde s'élèvera à %s, inférieur à la limite: recommencer le retrait... " % (self.amount - i)))

				if guichet.cancellation_check(new_amount):
					guichet.func()
					break

				else:

					while except_ValueError(new_amount) or except_TypeError(new_amount):
						
						new_amount = str(input("Votre solde s'élèvera à %s, inférieur à la limite: recommencer le retrait... " % (self.amount - i)))

						if guichet.cancellation_check(new_amount):
							guichet.func()
							break

				new_amount = guichet.str_to_int(new_amount)

			if guichet.withdrawal_verification_two((self.amount - new_amount), self.limit):

				if guichet.text_one(new_amount):
					pass
					
				else:

					self.amount-=new_amount
					(guichet.withdraw_number)+=1 # will return the number of withdraw
					guichet.withdraw_amount.append(new_amount) # will return the withdraw amount
					guichet.text_two()

		else:
			pass

	def withdraw_historical(self):

		historical = Historical(guichet.withdraw_amount)
		historical.historical_formatting()

		if guichet.withdraw_number == 0:
			print("Vous n'avez pas effectué de retrait.")
		elif guichet.withdraw_number == 1:
			print("Vous avez effectué un retrait de %s ." % (guichet.withdraw_amount[0]))
		else:
			print("Vous avez effectué %s retraits: " % (guichet.withdraw_number), end = "")

			for i in range(len(historical._times)):

				if i == len(historical._times) - 1 and len(historical._times) != 1:
					print("et %s de %s ." % (historical._times[i], historical._unique_amount[i]))
				elif len(historical._times) == 1:
					print("%s de %s." % (historical._times[i], historical._unique_amount[i]))
				elif (i != len(historical._times) - 1) or len(historical._times) == 1:
					print("%s de %s, " % (historical._times[i], historical._unique_amount[i]), end = "")

	def logout(self):

		# This is the transaction historical.
		# This method returns:
		# the number of operations performed,
		# and the concatenated amounts of each operation.

		guichet.account_consultation_historical()
		guichet.deposit_historical()
		guichet.withdraw_historical()
		guichet.account_consultation()

		print("\nÀ bientôt :)")
		sys.exit()

	def switcher(self, i):
		
		switcher = {'1': guichet.account_consultation,
					'2': guichet.deposit,
					'3': guichet.withdraw,
					'4': guichet.logout}

		operation = switcher.get(i, lambda: print('Entrée invalide !'))
		return operation()

	def main(self):

		while True:
			print("\n1. Consultation de compte\n2. Dépôt d'argent\n3. Retrait d'argent\n4. Déconnexion\n") # operations that can be performed by the user
			num = str(input("Veuillez entrer le nombre correspondant... "))
			guichet.switcher(num) # To access the selected operation.


print("CREATION D'UN NOUVEAU COMPTE BANCAIRE".center(80))

user = str(input("Entrer votre nom: "))
code = str(input("Entrer votre code: "))
limit = str(input("Entrer le montant minimal à rester dans votre compte: "))

while except_ValueError(limit) or except_TypeError(limit):
	limit = str(input("Entrer le montant minimal à rester dans votre compte: "))

amount = str(input("Entrer le montant de création du compte: "))

while except_ValueError(amount) or except_TypeError(amount):
	amount = str(input("Entrer le montant de création du compte: "))

limit, amount = int(limit), int(amount)

while (limit>amount): # to respect the limit amount
	amount = str(input("Veuillez entrer un montant excédant le montant limite: "))

	while except_ValueError(amount) or except_TypeError(amount):
		amount = str(input("Veuillez entrer un montant excédant le montant limite: "))

	amount = int(amount)

guichet = Guichet(user, code, amount, limit)
print("\nBonjour %s, quelle opération voudriez-vous effectuer sur votre compte ?" % (user))
guichet.main()
