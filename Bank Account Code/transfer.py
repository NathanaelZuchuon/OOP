import data

from fixed_costs import remove_costs
from file_mode import file, cost_file
from currenties import currentie
from collect_data import collect_data
from eval_stat import convert_to_dict
from cancel import information_about_cancellation
from card import azur_perc, gold_perc, premium_perc
from help import _help
from number_of_attempt import number_of_attempt
from __init__ import Guichet
from input_val import input_validation
from modify_file import modify_file, add_costs
from separator import sep

"""This function allows the transfer
of money from one user to another.
"""

def transfer():

	print("\nTRANSFERT D'ARGENT")

	try:
		user, code, limit, amount, card, msg, time, index = collect_data()

	except TypeError:
		pass

	else:

		attempt_user, file_name = 1, file()

		####### Their attributes #####
		list_users = data.name()     #
		list_codes = data.password() #
		list_limit = data.limit()    #
		list_amount = data.amount()  #
		list_time = data.time()      #
		list_card = data.card()      #
		list_msg = data.msg()        #
		##############################

		################ Recipient verification ############################
		while attempt_user < 4:                                            #
			recipient = number_of_attempt(attempt_user, "receveur")        #
                                                                           #
			if recipient == user:                                          #
                                                                           #
				if attempt_user == 3:                                      #
					print('Auto-transfert impossible !!\n')                #
					return                                                 #
                                                                           #
				else:                                                      #
					print('Auto-transfert impossible !!')                  #
                                                                           #
			elif recipient not in list_users:                              #
				print('Compte inexistant !!')                              #
                                                                           #
			elif (recipient in list_users) and (recipient != user):        #
				break                                                      #
                                                                           #
			if (attempt_user == 3) and (recipient == user):                #
				print('Auto-transfert impossible !!\n')                    #
				return                                                     #
                                                                           #
			if (recipient not in list_users) and (attempt_user == 3):      #
				print('\nCompte inexistant !!')                            #
				_help()                                                    #
				return                                                     #
                                                                           #
			attempt_user+=1                                                #
		####################################################################

		trans_amount = input_validation('Entrer le montant de transfert: ', card, False)
		while (amount-trans_amount) < limit:
			trans_amount = input_validation( f'Solde restant ({currentie(sep(amount-trans_amount))}) '
											+f'inférieur à la limite ({currentie(sep(limit))}), recommencer: ', 
											card, True)

		costs = {'azur': azur_perc, 'gold': gold_perc, 'premium': premium_perc}
		cost = costs.get(card)
		_cost = remove_costs(trans_amount, cost)

		recipient_index = list_users.index(recipient)
		amount-=(_cost+trans_amount)
		list_amount[recipient_index]+=trans_amount

		guichet = Guichet(user, code, amount, limit, card, msg, time, index)
		recipient_guichet = Guichet(recipient, list_codes[recipient_index], 
			list_amount[recipient_index], list_limit[recipient_index], 
			list_card[recipient_index], list_msg[index], list_time[recipient_index], recipient_index)

		modify_file(file_name, index, 'modification', guichet, None)
		modify_file(file_name, recipient_index, 'transfer', recipient_guichet, (user, trans_amount))

		file_name = cost_file()
		add_costs(file_name, _cost)

		print('',
			f'     DE:\t  {user}',
			f'      À:\t  {recipient}',
			f'MONTANT:\t {currentie(sep(trans_amount))}', sep='\n')

		print(f'\n* Solde restant: {currentie(sep(amount))}', end='\n\n')