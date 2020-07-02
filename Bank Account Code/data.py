from file_mode import read_mode
from file_mode import file_content
from file_mode import file
from eval_stat import convert_to_dict
from card import azur_limit, gold_limit, premium_limit

def _card(card):

	limits = {'azur': azur_limit, 'gold': gold_limit, 'premium': premium_limit}
	_min = limits.get(card)

	return _min

def return_users():

	global max_index, users_data

	file_name = file()
	with read_mode(file_name) as f:
		users_data = file_content(f) # Returns a list of all the customers.

	max_index = [x for x in range(len(users_data))]

def name():
	return_users()
	return [convert_to_dict(users_data[c]).get('name') for c in max_index]

def password():
	return_users()
	return [convert_to_dict(users_data[i]).get('password') for i in max_index]

def limit():
	return_users()
	return [convert_to_dict(users_data[j]).get('limit') for j in max_index]

def amount():
	return_users()
	return [convert_to_dict(users_data[k]).get('amount') for k in max_index]

def card():
	return_users()
	return [convert_to_dict(users_data[v]).get('card') for v in max_index]

def msg():
	return_users()
	return [convert_to_dict(users_data[z]).get('msg') for z in max_index]

def time():
	return_users()
	return [convert_to_dict(users_data[s]).get('time') for s in max_index]

def bank_chief():
	return ('Michel', )