import known_data_ui
from calendar import weekday

def order(date):

	days = {0: 'lundi ', 1: 'mardi ', 2: 'mercredi ', 
			3: 'jeudi ', 4: 'vendredi ', 5: 'samedi ', 
			6: 'dimanche '}
	months = {1: ' janvier ', 2: ' février ', 3: ' mars ', 4: ' avril ', 
			5: ' mai ', 6: ' juin ', 7: ' juillet ', 8: ' août ', 9: ' septembre ', 
			10: ' octobre ', 11: ' novembre ', 12: ' décembre '}
	date = list(date)

	year = date[:4]
	month = date[4:8]
	day = date[8:]

	new_year = int(''.join(year))
	new_month = int(''.join(month[1:3]))
	new_day = int(''.join(day))

	i = weekday(new_year, new_month, new_day)
	week_day = list(days.get(i))
	month = list(months.get(new_month))

	month.extend(year)
	day.extend(month)
	week_day.extend(day)

	return [''.join(week_day), i]

def last_connexion(time):

	new_date = known_data_ui.new_date()

	last_date = order(time[:10])
	date = order(new_date[:10])

	words = {1: ('hier', last_date[0]), 6: ('hier', last_date[0]), 0: ('aujourd\'hui', last_date[0])}
	num = abs(date[1] - last_date[1])

	if num in words:
		return f"{words.get(num)[0]}, {words.get(num)[1]} à {time[11:19]}"
	else:
		return f"{last_date[0]} à {time[11:19]}"

def salutation(time):
	return 'Bonjour' if time in range(6, 16) else 'Bonsoir'