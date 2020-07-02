from separator import sep

# Different type of card a user can choose.
TYPE_CARD = {'1': 'azur', '2': 'gold', '3': 'premium'}

azur_limit = 100
gold_limit = 500
premium_limit = 1000

azur_perc = 1
gold_perc = 3
premium_perc = 5

azur_max = 3000
gold_max = 10000
premium_max = 25000

def _doc(card):

	cards = {'azur': [azur_limit, azur_perc, azur_max],
			'gold': [gold_limit, gold_perc, gold_max],
			'premium': [premium_limit, premium_perc, premium_max]}

	doc = (
	f'\n{card.title()}',
	'=====================================================',
	f'Vous ne pouvez pas retirer plus de {sep(cards.get(card)[2])}.',
	f'Vous ne pouvez pas entrer un montant inférieur à {sep(cards.get(card)[0])}.',
	f'La banque vous prélève {cards.get(card)[1]}% sur chaque opération.')

	for i in doc:
		print(i)