from separator_ui import sep
from currenties import currentie

from card import azur_min, gold_min, premium_min, visa_min, vip_min
from card import azur_max, gold_max, premium_max, visa_max, vip_max
from card import azur_perc, gold_perc, premium_perc, visa_perc, vip_perc
from card import azur_limit, gold_limit, premium_limit, visa_limit, vip_limit

def _doc(card):

	cards = {
		'azur': [azur_limit, azur_perc, azur_max, azur_min],
		'gold': [gold_limit, gold_perc, gold_max, gold_min],
		'premium': [premium_limit, premium_perc, premium_max, premium_min],
		'visa': [visa_limit, visa_perc, visa_max, visa_min],
		'vip': [vip_limit, vip_perc, vip_max, vip_min],
		}

	doc = (
	f"Vous ne pouvez pas retirer plus de {currentie(sep(cards.get(card)[2]))} par connexion.\n"
	f"Vous ne pouvez pas entrer un montant inférieur à {currentie(sep(cards.get(card)[3]))}.\n"
	f"La banque vous prélève {cards.get(card)[1]}% par transaction.\n"
	f"Votre limite s'élève à {currentie(sep(cards.get(card)[0]))}."
	)

	return doc