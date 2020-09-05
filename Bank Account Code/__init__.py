from file_mode import file, cost_file
from fixed_costs import remove_costs
from modify_file import modify_file, add_costs, return_costs
from currenties import currentie
from data import bank_chief
from cancel import cancellation
from cancel import information_about_cancellation
from separator import sep
from card import azur_limit, gold_limit, premium_limit
from card import azur_perc, gold_perc, premium_perc
from card import azur_max, gold_max, premium_max
from card import _doc

"""This class is the user's account.
It contains all the actions it can perform.
These actions are defined as methods.
"""

class Guichet:

	def __init__(self, user, code, amount, limit, card, msg, time, index):

		self.user = user
		self.code = code
		self.amount = amount
		self.limit = limit
		self.card = card # The type of card used by the user.
		self.msg = msg # A list of dictionnaries of user's names who do transfer and the amounts: [{'X': 100}, {'Y': 200}].
		self.time = time # Used to store the last 'date-time' the user was connected to.
		self.index = index # The user's position in the storage file.

		############################
		self._deposit_amount = []  #
		self._withdraw_amount = [] # No amount and no cost has yet been entered or registered.
		self._all_costs = []       #
		############################

		###############################
		self._consultation_number = 0 #
		self._deposit_number = 0      # No operation has yet been performed.
		self._withdraw_number = 0     #
		###############################

	def text_one(self, amount):

		stat = (amount == 0) # 0 is not considered to be a real amount.

		if stat:
			print(f"\nVotre solde vaut toujours {currentie(sep(self.amount))} "
				  +"et l'opération ne sera pas prise en compte.")

		return stat

	def text_two(self):
		print(f"\nVotre solde s'élève désormais à {currentie(sep(self.amount))} .")

	def see_limit(self):
		print(f"\nLe montant limite de votre compte est {currentie(sep(self.limit))} .")

	def remove_msg(self):
		self.msg = []

	def see_card(self):
		_doc(self.card)

	def return_the_costs(self):

		chief = bank_chief()

		if self.user in chief:

			file_name = cost_file()
			return_costs(file_name)

		else:
			print('\nVous ne disposer pas des droits pour accéder à cette option.')

	def balance(self):
		print(f"\nVotre solde est de {currentie(sep(self.amount))} .")

	def no_withdraw(self):
		print("\nVous ne pouvez pas effectué un retrait d'un tel montant.")

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

		if list_amount == []:
			print(f'\nAucun {operation} effectué.')

		else:

			operation = operation.title() + 's'
			print(f'\n\t{operation}')
			for i in range(len(historical[0])):
				print(f'Montant:{currentie(sep(historical[1][i]))}\t\tRécurrence: {historical[0][i]}')

	def action(self, var, list_amount, new_amount):

		var+=1
		list_amount.append(new_amount)
		self.text_two()

	def list_costs(self):

		global cost

		costs = {'azur': azur_perc, 'gold': gold_perc, 'premium': premium_perc}
		cost = costs.get(self.card)

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

		nbre = {0: '\nAucune consultation effectuée.', 1: '\n1 consultation effectuée.'}

		if self._consultation_number in nbre:
			print(nbre.get(self._consultation_number))
		else:
			print(f'\n{self._consultation_number} consultations effectuées.')

	def deposit(self):

		msg = "Entrer le montant de dépôt: "
		self.operation(self.deposit_validation, msg, self._deposit_number, self._deposit_amount, '+')

	def deposit_historical(self):
		self.history(self._deposit_amount, 'dépôt')

	def withdrawal_verification(self, amount, limit):
		return True if amount >= limit else False # To respect the limit.

	def withdrawal(self):

		msg = 'Entrer le montant de retrait: '
		self.operation(self.withdrawal_validation, msg, self._withdraw_number, self._withdraw_amount, '-')

	def withdrawal_history(self):
		self.history(self._withdraw_amount, 'retrait')

	def no_all_withdrawal(self):
		print("\nVous ne pouvez pas effectué le retrait du solde effectif.")

	def all_withdrawal(self):

		new_amount = self.amount - self.limit
		self.get_card()

		if new_amount > max_withdraw:
			self.no_all_withdrawal()

		elif sum(self._withdraw_amount) >= max_withdraw:
			self.no_all_withdrawal()

		elif self.text_one(new_amount):
			pass

		else:

			self.amount = self.limit
			self.action(self._withdraw_number, self._withdraw_amount, new_amount)

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
		self.remove_msg()

		file_name = file()
		guichet = Guichet(self.user, self.code, self.amount, self.limit, self.card, self.msg, self.time, None)
		modify_file(file_name, self.index, 'modification', guichet, None)

		file_name = cost_file()
		add_costs(file_name, sum(self._all_costs))

		print(f"À bientôt {self.user} .")

	def switcher(self, i):

		switcher = {'1': self.account_consultation,
					'2': self.deposit,
					'3': self.withdrawal,
					'4': self.all_withdrawal,
					'5': self.see_limit,
					'6': self.see_card,
					'7': self.return_the_costs,
					'8': self.logout}

		operation = switcher.get(i, lambda: print('Entrée invalide !'))
		return operation()

	def min_amount(self):

		global _min

		limits = {'azur': azur_limit, 'gold': gold_limit, 'premium': premium_limit}
		_min = limits.get(self.card)

	def deposit_validation(self, msg):

		msg_error = msg
		self.min_amount()

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

					if value >= _min:
						return value
					else:
						msg = f'Vous ne pouvez pas déposer moins de{currentie(sep(_min))} : '

	def get_card(self):

		global max_withdraw

		limits = {'azur': azur_max, 'gold': gold_max, 'premium': premium_max}
		max_withdraw = limits.get(self.card)

	def withdrawal_validation(self, msg):

		msg_error = msg
		self.get_card()
		self.min_amount()
		self.list_costs()

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

						new_list = self._withdraw_amount.copy()
						new_list.append(value)

						if value >= _min:

							if sum(self._withdraw_amount) >= max_withdraw:
								print('\nVous ne pouvez plus effectuer de retrait.')
								return

							elif (value > max_withdraw) or (sum(new_list) > max_withdraw):
								self.no_withdraw()
								return

							_cost = remove_costs(value, cost)
							self._all_costs.append(_cost)
							self.amount-=_cost

							file_name, chief = cost_file(), bank_chief()

							if self.user in chief:
								add_costs(file_name, sum(self._all_costs))

							return value

						else:
							msg = f'Vous ne pouvez pas retirer moins de{currentie(sep(_min))} : '

					else:
						msg = (f"Votre solde s'élèvera à {currentie(sep(rest))} inférieur à la limite, "
							   +"entrer un nouveau montant de retrait: ")