from new_account import new_account
from existing_account import existing_account
from modify_data import modify_data
from transfer import transfer
from del_account import del_account
from logout import logout

def switcher(i):

	switcher = {'1': new_account,
				'2': existing_account,
				'3': modify_data,
				'4': transfer,
				'5': del_account,
				'6': logout}

	operation = switcher.get(i, lambda: print('Entrée invalide !'))
	return operation()