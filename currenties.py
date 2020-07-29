def currentie(amount, country='CAM', lang='fr'):

	devises = {'CAM': {'fr': 'F CFA', 'en': 'XAF'},
			'US': {'fr': 'US', 'en': '$'},
			'EU': {'fr': '€', 'en': '€'},
			'EN': {'fr': '£', 'en': '£'}}
	devise = devises.get(country).get(lang)

	if lang == 'fr':
		return f'{amount} {devise}'
	else:
		return f'{devise} {amount}'