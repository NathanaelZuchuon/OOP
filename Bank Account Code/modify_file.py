import file_mode

from data import msg
from eval_stat import convert_to_dict

def msg_transfer(index, new_data):

	list_msg = msg()
	new_msg = list_msg[index]
	new_msg.append({new_data[0]: new_data[1]})

	return new_msg

def create_file(file):

	global costs

	try:
		costs = file_mode.read_mode(file)

	except FileNotFoundError:

		costs = file_mode.create_mode(file)

		with file_mode.write_mode(file) as f:
			f.write('dict(costs=0)')

def add_costs(file, _add):

	create_file(file)

	amount_costs = file_mode.file_content(costs)
	old_value = convert_to_dict(amount_costs[0]).get('costs')
	new_value = old_value + _add

	with file_mode.write_mode(file) as f:
		f.write(f'dict(costs={new_value})')

def return_costs(file):

	create_file(file)

	with file_mode.read_mode(file) as f:
		amount_costs = file_mode.file_content(f)

	value = convert_to_dict(amount_costs[0]).get('costs')
	print(f"\nLe total des frais s'élève à{currentie(sep(value))} .")


"""This function is used to update
the values of the attributes of a user.
"""

def modify_file(file, index, value, instance, new_data):

	with file_mode.read_mode(file) as data:
		users_data = file_mode.file_content(data)

	del users_data[index]

	if new_data is None:
		pass

	if value == 'modification':
		users_data.insert(index, f"dict(name='{instance.user}', password='{instance.code}', "
								+f"limit={instance.limit}, amount={instance.amount}, "
								+f"card='{instance.card}', msg={instance.msg}, time='{instance.time}')\n")

	if value == 'deletion':
		pass

	if value == 'transfer':

		new_msg = msg_transfer(index, new_data)
		users_data.insert(index, f"dict(name='{instance.user}', password='{instance.code}', "
								+f"limit={instance.limit}, amount={instance.amount}, "
								+f"card='{instance.card}', msg={new_msg}, time='{instance.time}')\n")

	with file_mode.write_mode(file) as data_deletion:
		pass

	with file_mode.append_mode(file) as data_update:

		for item in users_data:
			data_update.write(item)