class Guichet:

	"""
	This class, Guichet, is the counter the user.
	It contains all the actions that can be done on itself.
	Those action are defined as class_method. The name, code ...etc of the user 
	are the class_attributes.

	"""

	l_d = [] # This is the list of all deposit amounts carried out during the implementation of the code
	l_w = [] # This is the list of all withdraw amounts carried out during the implementation of the code
	a = d = w = counter = 0 # a = "number of account consultation(s)" ; d = "number of deposit(s)" ; w = "number of withdraw(s)" ; counter = "the exit of the cancel method loop"

	def __init__(self, user, code, amount, limit): # This is the __init__ method which initializes:
		self.user = user # the name of the user
		self.code = code # the user's code
		self.amount = amount # the counter amount creation
		self.limit = limit # the min counter amount

	def account_consultation(self): # This is the account_consultation method, 
		(guichet.a)+=1 # it's increasing by 1 the number of account consultation
		print("Votre solde est de %s ." % (self.amount)) # it's printing the user counter amount

	def deposit(self): # This is the deposit method, 
		new_amount = int(input('\nEntrer le montant de dépôt: ')) # it's asking the deposit amount
		
		if new_amount != 5: # it's verifying that the input is != for 5 because the user could cancel the operation
			self.amount+=new_amount ; (guichet.d)+=1 # it's increasing the counter amount by the deposit amount and increasing by 1 the number of deposit
			guichet.l_d.append(new_amount) # it's adding the deposit amount to the deposit list
			print("Votre solde s'élève désormais à %s ." % (self.amount)) # it's printing the new counter amount
		else:
			print('Dépôt annulé !\n') # it's printing 'deposit canceled'
			print('Voulez-vous effectuer une nouvelle opération ?') # and 'do you want to carry out a new operation ?'
			guichet.cancel() # the deposit method calls the cancel method

	def withdraw(self): # This is the withdraw method,
		new_amount = int(input('\nEntrer le montant de retrait: ')) # it's asking the withdraw amount
		
		if new_amount != 5: # it's verifying that the input is != for 5 because the user could cancel the operation
			while (self.amount-new_amount)<(self.limit): # it's verifying if the counter amount won't be less than the limit
				new_amount = int(input("Votre solde s'élèvera à %s, inférieur à la limite: recommencer le retrait... " % (self.amount-new_amount))) # it's printing the purpose for what we refuse the withdraw amount
				if new_amount == 5: # the user will want to cancel the withdraw is he hasn't the good amount
					print('Retrait annulé !\n')
					print('Voulez-vous effectuer une nouvelle opération ?')
					guichet.cancel() # the withdraw method calls the cancel method
					break # the loop is broken
			if (self.amount-new_amount)>=(self.limit): # when we are out of the loop, we verify that the new amount after the withdraw is greater than the limit
					self.amount-=new_amount ; (guichet.w)+=1 # we remove the withdraw amount to the counter amount and increase by 1 the number of withdraw
					guichet.l_w.append(new_amount) # it's adding the withdraw amount to the withdraw list
					print("Votre solde s'élève désormais à %s ." % (self.amount)) # it's printing the new counter amount
		else:
			print('Retrait annulé !\n') # it's printing 'withdraw canceled'
			print('Voulez-vous effectuer une nouvelle opération ?') # and 'do you want to carry out a new operation ?'
			guichet.cancel() # the withdraw method calls the cancel method

	def cancel(self):
				
		while guichet.counter == 0: # At I said above, counter is "the exit of the cancel method loop",
			print("\n1. Consultation de compte\n2. Dépôt d'argent\n3. Retrait d'argent\n4. Déconnexion\n") # it's printing the different operations that the user can do on his account
			num = str(input('Veuillez entrer le nombre correspondant... ')) # it's asking the number of the operation as a string in order to avoid Type- and ValueError
		
			if num == '1':
				guichet.account_consultation() # if the input is 1, -> account_consultation method

			elif num == '2':
				print("Pour annuler l'opération en cours, entrer 5 ...") # it's printing 'press 5 to cancel the operation'
				guichet.deposit() # if the input is 2, -> deposit method

			elif num == '3':
				print("Pour annuler l'opération en cours, entrer 5 ...") # it's printing 'press 5 to cancel the operation'
				guichet.withdraw() # if the input is 3, -> withdraw method

			elif num == '4':
		
				if guichet.a == 0:
					print("\nVous n'avez pas effectué de consultation.")
				elif guichet.a == 1:
					print("\nVous avez effectué une consultation.")
				else:
					print("\nVous avez effectué %s consultations." % (guichet.a))

				if guichet.d == 0:
					print("Vous n'avez pas effectué de dépôt.")
				elif guichet.d == 1:
					print("Vous avez effectué un dépôt de %s ." % (guichet.l_d[0]))
				else:
					print("Vous avez effectué %s dépôts: " % (guichet.d), end = '')
			
					for i in range(len(guichet.l_d)):
						if i == len(guichet.l_d)-1:
							print('et un de %s .' % (guichet.l_d[i]))
						else:
							print('un de %s, ' % (guichet.l_d[i]), end = '')
		
				if guichet.w == 0:
					print("Vous n'avez pas effectué de retrait.")
				elif guichet.w == 1:
					print("Vous avez effectué un retrait de %s ." % (guichet.l_w[0]))
				else:
					print("Vous avez effectué %s retraits: " % (guichet.w), end = '')
			
					for i in range(len(guichet.l_w)):
						if i == len(guichet.l_w)-1:
							print('et un de %s .' % (guichet.l_w[i]))
						else:
							print('un de %s, ' % (guichet.l_w[i]), end = '')
		
				guichet.account_consultation()
				print('\nÀ bientôt :)')
				(guichet.counter)+=1 # if the input is 4, we increase by 1 counter
				break # the cancel method is broken

			else:
				print('Entrée invalide !')

def sup(arg): # This function makes sure that the limit is greather than zero
	
	while arg<0:
		try:
			arg = int(input('Entrer un montant positif: '))
		except ValueError: # if an ValueError occurs, the limit will be 0
			arg = 0
			print('"On prendra comme montant limite 0"')

	return arg

print("CREATION D'UN NOUVEAU COMPTE BANCAIRE".center(80))

user = str(input('Entrer votre nom: '))
code = str(input('Entrer votre code: '))

try:
	limit = int(input('Entrer le montant minimal à rester dans votre compte: '))
except ValueError:
	limit = 0
	print('"On prendra comme montant limite 0"')

if limit<0:
	sup(limit)

arg = sup(limit)
amount = int(input('Entrer le montant de création du compte: '))

while arg>amount:
	amount = int(input('Veuillez entrer un montant excédant le montant limite: ')) # This will be asks while the limit is greather than the counter amount creation

guichet = Guichet(user, code, amount, arg)
print("\nBonjour %s, quelle opération voudriez-vous effectuer sur votre compte ?" % (user.capitalize()))
guichet.cancel()