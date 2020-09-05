from bank_name import bank_name
from main_menu import main_menu
from get_input import get
from switcher import switcher
from file_mode import create_file

def main_method():

	create_file()
	bank_name()

	while True:
		main_menu()
		num = get()
		switcher(num)

main_method()