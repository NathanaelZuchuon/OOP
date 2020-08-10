def sum(n):

	if len(n) == 0:
		print('No element !')

	else:

		sum = n[0]

		for i in range(1, len(n)):
			sum+=n[i]

		print(sum)

"""

>>> sum([1, 2, 3])
>>> 6

"""