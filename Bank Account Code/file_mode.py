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

def file():
	return '{}:\\Object-Oriented Programming\\Bank Account Code\\data.txt'.format(reader())

def cost_file():
	return '{}:\\Object-Oriented Programming\\Bank Account Code\\costs.txt'.format(reader())

def create_file():

	file_name = file()

	try:
		read_mode(file_name)

	except FileNotFoundError:
		create_mode(file_name)