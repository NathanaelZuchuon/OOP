import music

from center_text import center_text
from file_mode import reader
from time import sleep
from os import startfile
from sys import exit

__author__ = 'Nathanaël Zuchuon'
__version__ = '1.3.5'

documentation = (
f'Ce programme a été écrit par {__author__}.\n',
f'Il est à sa version {__version__}\n',
'De manière briève, il permet une gestion efficace\n',
'de vos biens financiers virtuels.\n',
'***     Think-Code-Launch     ***'
)

for i in documentation:
	print(center_text(i))
	sleep(4)

exit(startfile('{}:\\Object-Oriented Programming\\Bank Account Code\\main_file.py'.format(reader())))