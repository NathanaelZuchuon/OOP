from file_mode import append_mode, file
from data import name
from currenties import currentie
from convert_str import convert_to_string
from input_val import input_validation
from code_val import code_validation
from separator import sep
from cancel import cancellation
from cancel import information_about_cancellation
from card import TYPE_CARD, _doc

"""This function allows the creation of a new bank account.
"""

def data_request():

	print("\nCREATION D'UN NOUVEAU COMPTE BANCAIRE")

	msg_user = 'Entrer votre nom: '
	msg_code = 'Entrer votre code à 4 chiffres: '

	information_about_cancellation()
	user = convert_to_string(msg_user)

	if cancellation(user):
		return

	list_users = name()
	file_name = file()

	while user in list_users: # This avoids the creation of several accounts with the same name.

		print('Compte existant !!')

		information_about_cancellation()
		user = convert_to_string(msg_user)

		if cancellation(user):
			return

	code = code_validation(msg_code)

	print('\nDIFFÉRENTS TYPES DE CARTE')
	_doc('azur')
	_doc('gold')
	_doc('premium')

	card = convert_to_string('\nEntrer le numéro du type de carte: ')
	while card not in TYPE_CARD:
		card = convert_to_string('Entrer le numéro du type de carte: ')
	card = TYPE_CARD.get(card)

	limit = input_validation('Entrer le montant minimal à rester dans votre compte: ', card, True)
	amount = input_validation('Entrer le montant de création du compte: ', card, True)

	while limit > amount: # To respect the limit.
		amount = input_validation('Veuillez entrer un montant excédant le montant minimal du compte: ', card, True)

	with append_mode(file_name) as f:
		# We store in the 'data.txt' file the attributes of the account with their values.
		f.write(f"dict(name='{user}', password='{code}', limit={limit}, "
			f"amount={amount}, card='{card}', msg=[], time='')\n")
#B															^
#Z					  The user has not yet been connected __|

	print('\nCompte créé avec succès:',
			f"   * Nom d'utilisateur: {user}",
			f"   * Mot de passe: {code}",
			f"   * Montant minimal à rester dans le compte: {currentie(sep(limit))}",
			f"   * Solde effectif du compte: {currentie(sep(amount))}", 
			f"   * Type de carte: {card}", sep='\n')