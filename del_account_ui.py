from file_mode import file, cost_file
from modify_file import modify_file, add_costs

"""This function allows the deletion of an account.
"""

def del_account(amount, index):

	file_name, _file_name = file(), cost_file()

	modify_file(file_name, index, 'deletion')
	add_costs(_file_name, amount)