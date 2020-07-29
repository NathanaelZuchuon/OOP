from help import email
from card_ui import _doc
from data import bank_chief
from separator_ui import sep
from currenties import currentie
from fixed_costs import remove_costs
from file_mode import file, cost_file
from modify_file import modify_file, return_costs, add_costs
from card import azur_max, gold_max, premium_max, visa_max, vip_max

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
		self.msg = msg # A dictionary list of the sender and the amount of the shipment: [{'X': 100}, {'Y': 200}].
		self.time = time # Used to store the last 'date-time' the user was connected to.
		self.index = index # The user's position in the storage file.

		self._consultation_number = 0 # No consultation has yet been performed.

		###############################
		self._withdraw_amount = []    # No withdraw has yet been done.
		self._all_costs = []          # No fees have yet been recorded.
		###############################

	def see_limit(self):
		return f"Le montant limite de votre compte est {currentie(sep(self.limit))} ."

	def remove_msg(self):
		self.msg = []

	def see_card(self):
		return _doc(self.card)

	def return_the_costs(self):

		chief = bank_chief()

		if self.user in chief:

			file_name = cost_file()
			return return_costs(file_name)

		else:
			return 'Vous ne disposer pas des droits pour accéder à cette option.'

	def balance(self):
		return f"Votre solde est de {currentie(sep(self.amount))} ."

	def _help(self):
		return 'Contacter la banque ' + email().lower()

	def addAmount(self, amount, sign, list_amount=[]):

		list_amount.append(amount)
		if sign == '+':
			self.amount+=amount
		else:
			self.amount-=amount

	def account_consultation(self):

		(self._consultation_number)+=1
		return self.balance()

	def account_consultation_historical(self):

		nbre = {0: 'Aucune consultation effectuée.\n\n', 1: '1 consultation effectuée.\n\n'}

		if self._consultation_number in nbre:
			return nbre.get(self._consultation_number)
		else:
			return f'{self._consultation_number} consultations effectuées.\n\n'

	def no_all_withdrawal(self):
		return "Vous ne pouvez pas effectué le retrait du solde effectif."

	def get_card(self):

		global max_withdraw

		limits = {'azur': azur_max, 'gold': gold_max, 'premium': premium_max,
				'visa': visa_max, 'vip': vip_max}
		max_withdraw = limits.get(self.card)

	def all_withdrawal(self):

		new_amount = self.amount - self.limit
		self.get_card()

		if new_amount > max_withdraw:
			return self.no_all_withdrawal()

		elif sum(self._withdraw_amount) >= max_withdraw:
			return self.no_all_withdrawal()

		elif new_amount < 0:
			return self.no_all_withdrawal()

		elif new_amount == 0: # 0 will not be considered.

			return (f"Votre solde vaut toujours {currentie(sep(self.amount))}\n"
				  +"et l'opération ne sera pas prise en compte.")

		else:

			self.amount = self.limit
			return self.action(self._withdraw_amount, new_amount)

	def action(self, list_amount, new_amount):

		list_amount.append(new_amount)
		return self.text()

	def text(self):
		return f"\nVotre solde s'élève désormais à {currentie(sep(self.amount))} ."

	def logout(self):

		self.remove_msg()

		file_name = file()
		guichet = Guichet(self.user, self.code, self.amount,
			self.limit, self.card, self.msg, self.time, None)
		modify_file(file_name, self.index, 'modification', guichet)

		file_name = cost_file()
		add_costs(file_name, sum(self._all_costs))

		return self.account_consultation_historical()