from file_mode import file
from file_mode import read_mode
from file_mode import file_content
from eval_stat import convert_to_dict
from card import azur_min, gold_min, premium_min, visa_min, vip_min

def _card(card):

	limits = {'azur': azur_min, 'gold': gold_min, 'premium': premium_min,
			'visa': visa_min, 'vip': vip_min}
	_min = limits.get(card)

	return _min

def return_users():

	global max_index, users_data

	file_name = file()
	with read_mode(file_name) as f:  # Returns the list of all the bank's clients
		users_data = file_content(f) # and the values of their attributes.

	max_index = [x for x in range(len(users_data))]

def return_data(key):

	global _list

	return_users()
	_list = [convert_to_dict(users_data[i]).get(key) for i in max_index]

def name():
	return_data('name')
	return _list

def password():
	return_data('password')
	return _list

def limit():
	return_data('limit')
	return _list

def amount():
	return_data('amount')
	return _list

def card():
	return_data('card')
	return _list

def msg():
	return_data('msg')
	return _list

def time():
	return_data('time')
	return _list

def bank_chief():
	return ('Michel', 'Mc', 'Sterling', )