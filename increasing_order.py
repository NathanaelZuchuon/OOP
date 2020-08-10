def getOrder(numbers):

	for i in range(len(numbers)):
		_min = min(numbers)
		print(_min, end='\r ')
		numbers.remove(_min)

nums = []
for i in range(5):
	nums.append(int(input('Entrer un nombre: ')))

getOrder(nums)