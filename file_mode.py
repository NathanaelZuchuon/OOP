"""This module allows me to open a file
in different mode depending on the function that I import.
"""

def create_mode(file):
	return open(file, 'x')

def read_mode(file):
	return open(file, "r")

def write_mode(file):
	return open(file, "w")

def append_mode(file):
	return open(file, "a")

def file_content(file):
	return file.readlines()

def reader():
	return 'E'

def path():

	from os import getcwd
	return '{}'.format(getcwd())

def file():
	return f'{path()}\\data.txt'

def cost_file():
	return f'{path()}\\costs.txt'

def create(file):

	file_name = file()

	try:
		read_mode(file_name)

	except FileNotFoundError:
		create_mode(file_name)

def create_file():

	create(file)
	create(cost_file)