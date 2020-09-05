from data import name
from file_mode import file
from collect_data import collect_data
from currenties import currentie
from modify_file import modify_file
from input_val import input_validation
from code_val import code_validation
from convert_str import convert_to_string
from separator import sep 
from __init__ import Guichet
from card import TYPE_CARD, _doc

"""This function allows the user to modify
some of his attributes (his name, ...etc).
"""

def modify_data():

	print('\nMODIFICATION DES DONNÉES')

	try:

		user, code, limit, amount, card, msg, time, index = collect_data()

	except TypeError:
		pass

	else:

		print() # for the layout...
		msg_user = "Entrer votre nouveau nom d'utilisateur: "
		msg_code = "Entrer votre nouveau mot de passe: "
		msg_limit = "Entrer votre nouvelle limite: "
		msg_card = "Entrer le numéro de votre nouveau type de carte: "

		file_name = file()
		list_users = name()

		del list_users[index] # He can enter the same name.

		new_user = convert_to_string(msg_user)

		while new_user in list_users: # Checking the existence of the account.
			print('Compte existant\n')
			new_user = convert_to_string(msg_user)

		code = code_validation(msg_code)

		print('\nDIFFÉRENTS TYPES DE CARTE')
		_doc('azur')
		_doc('gold')
		_doc('premium')

		card = convert_to_string('\n'+msg_card)
		while card not in TYPE_CARD:
			card = convert_to_string(msg_card)
		card = TYPE_CARD.get(card)

		limit = input_validation(msg_limit, card, False)
		msg_limit = f"Limite supérieur au solde ({currentie(sep(amount))}), recommencer: "

		while amount < limit:
			limit = input_validation(msg_limit, card, False)

		guichet = Guichet(new_user, code, amount, limit, card, msg, time, None)
		modify_file(file_name, index, 'modification', guichet, None) # Update the values.

		print('\nDonnées modifiées avec succès:',
				f"   * Nouveau nom d'utilisateur: {new_user}",
				f"   * Nouveau mot de passe: {code}",
				f"   * Nouvelle limite: {currentie(sep(limit))}", 
				f"   * Nouveau type de carte: {card}", sep='\n')