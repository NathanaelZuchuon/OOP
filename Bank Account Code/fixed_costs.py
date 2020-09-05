def remove_costs(amount, perc, valid_num={25: range(19,39), 50: range(39,69), 75: range(69, 89), 100: range(89, 99)}):

	cost = int((amount*perc)/100)
	_cost = list(str(cost))
	len_cost = len(_cost)

	if len_cost == 1:
		return cost

	if len_cost > 2:
		max_index = -(len_cost)
		num = _cost[-1: max_index: -1]
		num.reverse()

	else:
		num = _cost

	i = ''.join(num)

	if len(i) == 0:
		pass

	else:

		two_last_num = int(i)

		for k, v in valid_num.items():
			if two_last_num in v:
				_max = k
				break
			else:
				_max = 0

		if two_last_num > _max:

			_add = two_last_num - _max

			if _add <= 0:
				pass
			else:
				cost-=_add

		else:

			_add = _max - two_last_num

			if _add <= 0:
				pass
			else:
				cost+=_add

	return cost