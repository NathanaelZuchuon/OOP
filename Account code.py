import sys


def non_nullity(arg): # The limit must be greater than or equal to zero.

	while (arg<0):

		try:
			arg = int(input("Entrer un bon montant: "))
		except ValueError:
			arg = 0
			print('"On prendra comme montant limite 0"')
			break

	return arg


class History:

	"""
	This class embellishes the history
	by concatenating the amounts, eg:
	amounts: 10, 20, 10, 30, 20 40.
	output: 2 of 10, 2 of 20, 1 of 30, 1 of 40.

	"""

	def __init__(self, list_amount):
		self.list_amount = list_amount
		self._times = None
		self._unique_amount = None

	def history_formatting(self):

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

	def text_one(self, value):

		if value == 0: # 0 is not considered to be a true value.
			print("Votre solde vaut toujours %s et l'opération ne sera pas prise en compte." % (self.amount))

		return value == 0

	def text_two(self):

		print("Votre solde s'élève désormais à %s ." % (self.amount))

	def cancellation_check(self, value):

		if value.upper() == "RETOUR": # To cancel the operation in progress.
			return True
		else:
			return False

	def display_formatting(self):

		print("Opération annulée !\n\nVoulez-vous effectuer une nouvelle opération ?")

	def information_about_cancellation(self):

		print("Pour annuler l'opération en cours, entrer 'RETOUR' ...")

	def str_to_int(self, value):

		return int(value)

	def account_consultation(self):

		(guichet.consultation_number)+=1 # will return the number of account consultation
		print("Votre solde est de %s ." % (self.amount))

	def account_consultation_history(self):

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

	def deposit_history(self):

		history = History(guichet.deposit_amount)
		history.history_formatting()

		if guichet.deposit_number == 0:
			print("Vous n'avez pas effectué de dépôt.")
		elif guichet.deposit_number == 1:
			print("Vous avez effectué un dépôt de %s ." % (guichet.deposit_amount[0]))
		else:
			print("Vous avez effectué %s dépôts: " % (guichet.deposit_number), end = "")

			for i in range(len(history._times)):

				if i == len(history._times) - 1:
					print("et %s de %s ." % (history._times[i], history._unique_amount[i]))
				elif len(history._times) == 1:
					print("%s de %s." % (history._times[i], history._unique_amount[i]))
				else:
					print("%s de %s, " % (history._times[i], history._unique_amount[i]), end = "")

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

			new_amount = guichet.str_to_int(new_amount)
			
			while guichet.withdrawal_verification_one((self.amount - new_amount), self.limit):

				new_amount = str(input("Votre solde s'élèvera à %s, inférieur à la limite: recommencer le retrait... " % (self.amount - new_amount)))

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

	def withdraw_history(self):

		history = History(guichet.withdraw_amount)
		history.history_formatting()

		if guichet.withdraw_number == 0:
			print("Vous n'avez pas effectué de retrait.")
		elif guichet.withdraw_number == 1:
			print("Vous avez effectué un retrait de %s ." % (guichet.withdraw_amount[0]))
		else:
			print("Vous avez effectué %s retraits: " % (guichet.withdraw_number), end = "")

			for i in range(len(history._times)):

				if i == len(history._times) - 1 and len(history._times) != 1:
					print("et %s de %s ." % (history._times[i], history._unique_amount[i]))
				elif len(history._times) == 1:
					print("%s de %s." % (history._times[i], history._unique_amount[i]))
				elif (i != len(history._times) - 1) or len(history._times) == 1:
					print("%s de %s, " % (history._times[i], history._unique_amount[i]), end = "")

	def logout(self):

		# This is the transaction history.
		# This method returns:
		# the number of operations performed,
		# and the concatenated amounts of each operation.

		guichet.account_consultation_history()
		guichet.deposit_history()
		guichet.withdraw_history()
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

try:
	limit = int(input("Entrer le montant minimal à rester dans votre compte: "))
except ValueError:
	limit = 0
	print('"On prendra comme montant limite 0"')

arg = non_nullity(limit)

amount = int(input("Entrer le montant de création du compte: "))

while (arg>amount):  # to respect the limit amount
	amount = int(input("Veuillez entrer un montant excédant le montant limite: "))

guichet = Guichet(user, code, amount, arg)
print("\nBonjour %s, quelle opération voudriez-vous effectuer sur votre compte ?" % (user))
guichet.main()
