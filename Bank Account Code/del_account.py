from collect_data import collect_data
from modify_file import modify_file, add_costs
from file_mode import file, cost_file

"""This function allows the deletion of an account.
"""

def del_account():

	print("\nSUPPRESSION D'UN COMPTE EXISTANT")

	try:
		user, code, limit, amount, card, msg, time, index = collect_data()

	except TypeError:
		pass

	else:

		file_name, _file_name = file(), cost_file
		modify_file(file_name, index, 'deletion', None, None)
		add_costs(_file_name, amount)
		print('\nCompte supprimé avec succès !!')