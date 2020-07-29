from data import name
from file_mode import append_mode, file
from card import azur_limit, gold_limit, premium_limit, visa_limit, vip_limit

def getLimit(card):

	limits = {'AZUR': azur_limit, 'GOLD': gold_limit, 'PREMIUM': premium_limit,
			'VISA': visa_limit, 'VIP': vip_limit}
	limit = limits.get(card)

	return limit

def addAccount(file_name, *args):

	user, code, limit, amount, card = args[0], args[1], args[2], args[3], args[4]

	with append_mode(file_name) as f:
		f.write(f"dict(name='{user}', password='{code}', limit={limit}, "
			f"amount={amount.replace('  ', '')}, card='{card.lower()}', msg=[], time='')\n")