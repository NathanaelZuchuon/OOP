import data

"""This function lets me know which user it is.
"""

####### Their attributes #####
list_users = data.name()     #
list_codes = data.password() #
list_limit = data.limit()    #
list_amount = data.amount()  #
list_time = data.time()      #
list_card = data.card()      #
list_msg = data.msg()        #
##############################

def getAttributes(name):

	index = list_users.index(name)
	return (name, list_codes[index], list_limit[index], list_amount[index],
		list_card[index], list_msg[index], list_time[index], index)