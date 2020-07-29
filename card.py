from separator_ui import sep
from currenties import currentie

def _print():
	print('\nDIFFÉRENTS TYPES DE CARTE', 
		'=========================', sep='\n')

azur_min = 100
gold_min = 500
premium_min = 1000
visa_min = 1500
vip_min = 2000

azur_perc = 1
gold_perc = 3
premium_perc = 5
visa_perc = 7
vip_perc = 9

azur_limit = 500
gold_limit = 1000
premium_limit = 1500
visa_limit = 2000
vip_limit = 4000

azur_max = 5000
gold_max = 10000
premium_max = 15000
visa_max = 20000
vip_max = 40000

def _doc(card):

	cards = {'azur': ['1', azur_limit, azur_perc, azur_max, azur_min],
			'gold': ['2', gold_limit, gold_perc, gold_max, gold_min],
			'premium': ['3', premium_limit, premium_perc, premium_max, premium_min],
			'visa': ['4', visa_limit, visa_perc, visa_max, visa_min],
			'vip': ['5', vip_limit, vip_perc, vip_max, vip_min]}

	doc = (
	f'\n{cards.get(card)[0]}. {card.upper()}',
	'==============================================================',
	f'Vous ne pouvez pas retirer plus de {currentie(sep(cards.get(card)[3]))} par connexion.',
	f'Vous ne pouvez pas entrer un montant inférieur à {currentie(sep(cards.get(card)[4]))}.',
	f'La banque vous prélève {cards.get(card)[2]}% par transaction.',
	f'Votre limite s\'élève à {currentie(sep(cards.get(card)[1]))}.',
	)

	for i in doc:
		print(i)