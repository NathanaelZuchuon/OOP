import data

# Import of all widgets and some built-in functions
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial

# Import of my required functions
from card_ui import _doc
from sys import argv, exit
from separator_ui import sep
from __init__ui import Guichet
from currenties import currentie
from fixed_costs import remove_costs
from file_mode import file, cost_file
from del_account_ui import del_account
from collect_data_ui import getAttributes
from known_data_ui import new_date, transfer
from modify_file import modify_file, add_costs
from order_ui import last_connexion, salutation
from data_request_ui import getLimit, addAccount
from card import azur_min, gold_min, premium_min, visa_min, vip_min
from card import azur_max, gold_max, premium_max, visa_max, vip_max
from card import azur_perc, gold_perc, premium_perc, visa_perc, vip_perc

__author__ = 'Nathanaël Zuchuon'
__version__ = '1.5.0'

# Create a subclass of QMainWindow.

class MainWindow(QMainWindow):

	def __init__(self):

		super().__init__()
		self.value = None

		# Set main window's title
		self.setWindowTitle('Guichet Automatique')

		# Creating the menu bar
		self._createMenuBar()

		# Creating the main menu
		self._createMainMenu()

	def getNewData(self):

		global list_users, list_amount, list_limits, chief
		global list_card, list_msg, list_time, list_codes

		list_users = data.name()
		list_amount = data.amount()
		list_limits = data.limit()
		list_card = data.card()
		list_msg = data.msg()
		list_time = data.time()
		list_codes = data.password()

	def method(self):
		pass

	def _createCentralWidget(self):

		""" Set the central widget and the general layout.
		When this method is called, the display is cleared
		to avoid adding additional widgets. """

		self.setGeometry(400, 50, 460, 480)
		self.generalLayout = QVBoxLayout()
		self.centralWidget = QWidget()
		self.setCentralWidget(self.centralWidget)
		self.centralWidget.setLayout(self.generalLayout)

	def _createMenuBar(self):

		bar = self.menuBar()
		bar.setFont(QFont("High Tower Text", 11))

		menu = bar.addMenu("Menu")
		menu.setFont(QFont("High Tower Text", 11))

		cancel = QAction("Retour", self)
		menu.addAction(cancel)

		quit = QAction("Quitter", self)
		menu.addAction(quit)

		menu.triggered[QAction].connect(self.process_triggered)

	def process_triggered(self, action):

		if action.text() == "Quitter":

			self._createDialogBox('quitter')

			if self.value:
				self._createMessageBox('Déconnexion',
					f"Votre fidélité, notre satisfaction {chr(10024)}")
				self.close()

		else:
			self._createMainMenu() # Return to the main menu

	def _createPushButton(self, text, font=None):

		button = QPushButton()

		button.setText(text)

		if font is not None:
			button.setFont(font)

		return button

	def add_QLabel(self, layout, index):

		for i in range(index):
			layout.addRow(QLabel())

	def _createMainMenu(self):

		self._createCentralWidget()
		self.setGeometry(400, 50, 465, 500)

		title = QLabel()
		title.setText("MENU PRINCIPAL")
		title.setAlignment(Qt.AlignCenter)
		title.setFont(QFont("Berlin Sans FB", 14))

		font = QFont("Berlin Sans FB", 11)

		text = [
			'Création d\'un nouveau compte',
			'Connexion à un compte',
			'Modification des données',
			'Suppression d\'un compte',
			'Transfert d\'argent',
			]

		slots = [
			self._createAccount,
			self._connectToAccount,
			self._modifyData,
			self._deleteAccount,
			self._transferMoney,
			]

		widgets = []
		for i in text:
			button = self._createPushButton(i, font)
			widgets.append(button)

		fbox = QFormLayout()

		fbox.addRow(title)
		self.add_QLabel(fbox, 3)

		for i in range(len(widgets)):
			widgets[i].clicked.connect(slots[i])

		for i in widgets:

			fbox.addRow(i)
			self.add_QLabel(fbox, 3)

		self.generalLayout.addLayout(fbox)

	def _createTitle(self, title):

		self.title = QLabel()

		self.title.setText(title)
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setFont(QFont("Berlin Sans FB", 14))

	def _createCards(self):

		self.CBox = QComboBox()

		self.CBox.setFont(QFont("Comic Sans Ms", 10))
		self.CBox.addItem('')
		self.CBox.addItems(['AZUR', 'GOLD', 'PREMIUM', 'VISA', 'VIP'])
		self.CBox.activated.connect(self.choose_card)

	def _createName(self):

		self.name = QLineEdit()

		self.name.setAlignment(Qt.AlignCenter)
		self.name.setFont(QFont("Comic Sans Ms", 14))

	def _createCode(self, display=QLineEdit.PasswordEchoOnEdit):

		self.code = QLineEdit()

		self.code.setValidator(QIntValidator())
		self.code.setEchoMode(display)
		self.code.setAlignment(Qt.AlignCenter)
		self.code.setMaxLength(4)
		self.code.textChanged.connect(partial(self.text_changed, self.code))

	def _createConfirmCode(self, display=QLineEdit.PasswordEchoOnEdit):

		self.confirm_code = QLineEdit()

		self.confirm_code.setValidator(QIntValidator())
		self.confirm_code.setEchoMode(display)
		self.confirm_code.setAlignment(Qt.AlignCenter)
		self.confirm_code.setMaxLength(4)
		self.confirm_code.textChanged.connect(partial(self.text_changed,
			self.confirm_code))

	def _createAmount(self):

		self.amount = QLineEdit()

		self.amount.setValidator(QIntValidator())
		self.amount.setAlignment(Qt.AlignCenter)
		self.amount.setFont(QFont("Comic Sans Ms", 11))
		self.amount.textChanged.connect(self._textChanged)

	def _createSaveButton(self, func):

		self.save = self._createPushButton('Save', QFont("Berlin Sans FB", 11))
		self.save.clicked.connect(func)

	def _createOkButton(self, func, operation=None):

		self.ok = self._createPushButton('Ok', QFont("Berlin Sans FB", 11))

		if operation is not None:
			self.ok.clicked.connect(partial(func, operation))
		else:
			self.ok.clicked.connect(func)

	def _createMessageBox(self, title, text):

		msg = QMessageBox()

		msg.setFont(QFont("Arial", 10))
		msg.setGeometry(500, 300, 280, 80)
		msg.setIcon(QMessageBox.Information)
		msg.setWindowTitle(title)
		msg.setText(text)
		msg.exec_()

	def _changeValue(self, widget, value=False):

		self.value = value
		widget.close()

	def _createDialogBox(self, msg, title="Demande de sortie"):

		self.dialog = QDialog()
		self.dialog.setWindowTitle(title)
		self.dialog.setGeometry(500, 300, 280, 80)

		vbox = QVBoxLayout()
		hbox = QHBoxLayout()

		y = self._createPushButton('Oui')
		n = self._createPushButton('Non')

		y.clicked.connect(partial(self._changeValue, self.dialog, True))
		n.clicked.connect(partial(self._changeValue, self.dialog))

		confirm_msg = QLabel()
		confirm_msg.setFont(QFont("High Tower Text", 11))
		confirm_msg.setAlignment(Qt.AlignCenter)
		confirm_msg.setText(f'Voulez-vous vraiment {msg} ?')

		hbox.addWidget(y)
		hbox.addStretch()
		hbox.addWidget(n)

		vbox.addWidget(confirm_msg)
		vbox.addLayout(hbox)

		self.dialog.setLayout(vbox)
		self.dialog.exec_()

	def _collect_data(self, operation):

		global name, code

		name = QLabel()
		code = QLabel()

		name.setText("Nom:")
		name.setFont(QFont("Berlin Sans FB", 11))

		code.setText("Code:")
		code.setFont(QFont("Berlin Sans FB", 11))

		self._createCentralWidget()

		self._createTitle('COLLECTE DES DONNÉES')
		self._createName()
		self._createCode(QLineEdit.Password)
		self._createOkButton(self.validation, operation)

		self.addLabels([self.name, self.code], self.ok, [name, code], ['', ''])

	def validation(self, operation):

		self.getNewData()

		if self.name.text() not in list_users:
			msg_name = self.redFont('Compte inexistant')
		else:
			msg_name = ''
			self.index = list_users.index(self.name.text())


		if msg_name == self.redFont('Compte inexistant'):
			msg_code = ''
		elif self.code.text() == '':
			msg_code = self.redFont('Veuillez entrer votre code')
		elif self.code.text() != list_codes[self.index]:
			msg_code = self.redFont('Code incorrect')
		else:
			msg_code = ''


		msgs = [msg_name, msg_code]

		self.addLabels([self.name, self.code], self.ok, [name, code], msgs)

		if all([i == '' for i in msgs]):

			if operation == 'connexion':
				self.connect()

			if operation == 'modification':
				self._modify()

			if operation == 'transfer':
				self._transfer()

			if operation == 'deletion':
				self._delete()

	def _createAccount(self):

		self._createCentralWidget()
		self._createFields()

	def _connectToAccount(self):
		self._collect_data('connexion')

	def _modifyData(self):
		self._collect_data('modification')

	def _deleteAccount(self):
		self._collect_data('deletion')

	def _transferMoney(self):
		self._collect_data('transfer')

	def connect(self):

		self.getNewData()
		self._createCentralWidget()
		self.setGeometry(400, 50, 465, 500)

		new_time, fbox, font = new_date(), QFormLayout(), QFont("Consolas", 11)

		polite = QLabel()
		connexion = QLabel()
		transfer_text = QLabel()
		which_operation = QLabel()

		polite.setFont(font)
		polite.setText(f'{salutation(int(new_time[11:13]))} '
					f'{list_users[self.index]},\n'
					'Bienvenue à < By Zuch & Co. > votre banque virtuelle')
		polite.setAlignment(Qt.AlignCenter)

		fbox.addRow(polite)
		fbox.addRow(QLabel())

		if list_time[self.index] != '':

			connexion.setFont(font)
			connexion.setText('Date & heure de la dernière connexion:\n'
							f'{last_connexion(list_time[self.index])}')
			connexion.setAlignment(Qt.AlignLeft)

			fbox.addRow(connexion)
			fbox.addRow(QLabel())

		if list_msg[self.index] != []:

			transfer_text.setFont(font)
			transfer_text.setText('Transfert(s) reçu(s):\n'+
				transfer(list_msg[self.index]))
			transfer_text.setAlignment(Qt.AlignLeft)

			fbox.addRow(transfer_text)
			fbox.addRow(QLabel())

		which_operation.setText(
			'Quelle opération voudriez-vous effectuer sur votre compte ?')
		which_operation.setAlignment(Qt.AlignCenter)
		which_operation.setFont(font)

		fbox.addRow(which_operation)
		fbox.addRow(QLabel())

		guichet = Guichet(list_users[self.index], list_codes[self.index],
			list_amount[self.index], list_limits[self.index],
			list_card[self.index], list_msg[self.index],
			new_time, self.index)

		options = [
			"Consultation de compte",
			"Dépôt d'argent",
			"Retrait d'argent",
			"Retrait du solde effectif",
			"Voir limite du compte",
			"Voir caractéristiques de la carte",
			"Voir total des frais",
			"Pour plus d'informations...",
			"Déconnexion",
			]

		slots = [
			guichet.account_consultation,
			self.method,
			self.method,
			guichet.all_withdrawal,
			guichet.see_limit,
			guichet.see_card,
			guichet.return_the_costs,
			guichet._help,
			guichet.logout,
			]

		widgets = []
		for i in options:

			option = QLabel()

			option.setFont(font)
			option.setText('<a href="#">' + i + '</a>')
			widgets.append(option)

			fbox.addRow(option)
			fbox.addRow(QLabel())

		for i in range(len(widgets)):

			widget = widgets[i]
			widget.linkActivated.connect(
				partial(self.operation, widget.text(), slots[i], guichet)
				)

		self.generalLayout.addLayout(fbox)

	def operation(self, option, method, instance):

		global amount, _option

		_option = option.replace('<a href="#">', '')
		_option = _option.replace('</a>', '')

		special_funcs = [
			'Dépôt d\'argent',
			'Retrait d\'argent',
			'Retrait du solde effectif',
			'Déconnexion',
			]

		if _option in special_funcs:
			
			if _option == 'Déconnexion':

				def layout(arg, amount):
					return f'* Solde à la {arg}: {currentie(sep(amount))}\n'

				self._createMessageBox(
					_option,
					(
					method()+
					layout('connexion', list_amount[self.index])+
					layout('déconnexion', instance.amount)+
					f"\nÀ bientôt {list_users[self.index]} ."
					)
					)
				self._createMainMenu()

			elif _option == 'Retrait du solde effectif':
				self._createMessageBox(_option, instance.all_withdrawal())

			elif _option == 'Retrait d\'argent':

				self._createAmount()
				self._createOkButton(self.withdrawal_validation, instance)

				amount = QLabel()
				amount.setText("Montant de retrait:")
				amount.setFont(QFont("Berlin Sans FB", 11))

				self.addSingleLabel(self.amount, self.ok, amount, '', _option)
				dialog.close()

			elif _option == 'Dépôt d\'argent':

				self._createAmount()
				self._createOkButton(self.deposit_validation, instance)

				amount = QLabel()
				amount.setText("Montant de dépôt:")
				amount.setFont(QFont("Berlin Sans FB", 11))

				self.addSingleLabel(self.amount, self.ok, amount, '', _option)
				dialog.close()

		else:
			self._createMessageBox(_option, method())

	def deposit_validation(self, instance):

		if self.amount.text() == '':
			msg = 'Veuillez entrer un montant'
		elif int(self.amount.text().replace('  ', '')) < getLimit(list_card[self.index].upper()):
			msg = ('Vous ne pouvez pas entrer moins de '+
				f'{currentie(sep(getLimit(list_card[self.index].upper())))}')
		else:
			msg = ''

		msg = self.redFont(msg)

		if msg == '<FONT COLOR="RED"></FONT>':
			instance.addAmount(int(self.amount.text().replace('  ', '')), '+')
			dialog.close()

		else:
			dialog.close()
			self.addSingleLabel(self.amount, self.ok, amount, msg, _option)

	def withdrawal_validation(self, instance):

		withdraws = {'azur': azur_max, 'gold': gold_max, 'premium': premium_max,
				'visa': visa_max, 'vip': vip_max}
		max_withdraw = withdraws.get(list_card[self.index])

		costs = {'azur': azur_perc, 'gold': gold_perc, 'premium': premium_perc,
				'visa': visa_perc, 'vip': vip_perc}
		cost = costs.get(list_card[self.index])

		if self.amount.text() == '':
			msg = 'Veuillez entrer un montant'
		elif int(self.amount.text().replace('  ', '')) < getLimit(list_card[self.index].upper()):
			msg = ('Vous ne pouvez pas entrer moins de '+
				f'{currentie(sep(getLimit(list_card[self.index].upper())))}')
		elif instance.amount - int(self.amount.text().replace('  ', '')) < list_limits[self.index]:
			msg = 'Solde restant inférieur à la limite'
		elif sum(instance._withdraw_amount) >= max_withdraw:
			msg = 'Vous ne pouvez plus effectuer de retrait'
		else:

			new_list = instance._withdraw_amount.copy()
			new_list.append(int(self.amount.text().replace('  ', '')))

			if (int(self.amount.text().replace('  ', '')) > max_withdraw) or (sum(new_list) > max_withdraw):
				msg = 'Vous ne pouvez pas effectué un retrait d\'un tel montant.'
			else:
				msg = ''

		msg = self.redFont(msg)

		if msg == '<FONT COLOR="RED"></FONT>':

			bank_chief = data.bank_chief()

			if instance.user in bank_chief:
				new_amount = int(self.amount.text().replace('  ', ''))

			else:

				_cost = remove_costs(int(self.amount.text().replace('  ', '')), cost)
				instance._all_costs.append(_cost)
				new_amount = int(self.amount.text().replace('  ', '')) + _cost

			instance.addAmount(new_amount, '-', instance._withdraw_amount)
			dialog.close()

		else:
			dialog.close()
			self.addSingleLabel(self.amount, self.ok, amount, msg, _option)

	def _createWidget(self, title):

		global generalLayout, dialog

		generalLayout = QVBoxLayout()
		dialog = QDialog()
		dialog.setLayout(generalLayout)
		dialog.setWindowTitle(title)
		dialog.setGeometry(500, 300, 280, 80)

	def _modify(self):

		global name, code, card

		name = QLabel()
		code = QLabel()
		card = QLabel()

		name.setText("Nouveau nom:")
		name.setFont(QFont("Berlin Sans FB", 11))

		code.setText("Nouveau code:")
		code.setFont(QFont("Berlin Sans FB", 11))

		card.setText("Nouvelle carte:")
		card.setFont(QFont("Berlin Sans FB", 11))

		self._createCentralWidget()

		self._createTitle('MODIFICATION DES DONNÉES')
		self._createName()
		self._createCode()
		self._createCards()
		self._createSaveButton(self._modify_validation)

		self.addLabels([self.name, self.code, self.CBox], self.save,
				[name, code, card], ['', '', ''])

	def _modify_validation(self):

		self.getNewData()

		if self.name.text() == '':
			msg_name = self.redFont('Veuillez entrer votre nouveau nom')
		elif self.name.text() == list_users[self.index]:
			msg_name = ''
		elif self.name.text() in list_users:
			msg_name = self.redFont('Compte existant')
		else:
			msg_name = ''


		if self.code.text() == '':
			msg_code = self.redFont('Veuillez entrer votre nouveau code')
		elif len(self.code.text()) < 4:
			msg_code = self.redFont('Veuillez entrer un code à 4 chiffres')
		else:
			msg_code = ''


		if self.CBox.currentText() == '':
			msg_card = self.redFont('Veuillez choisir un type de carte')
		else:
			limit = getLimit(self.CBox.currentText())
			if list_amount[self.index] < limit:
				msg_card = self.redFont('La limite de cette carte est supérieur à <br>'
					f'votre solde actuel ({currentie(sep(list_amount[self.index]))})')
			else:
				msg_card = ''

		msgs = [msg_name, msg_code, msg_card]

		self.addLabels([self.name, self.code, self.CBox], self.save,
				[name, code, card], msgs)

		if all([i == '' for i in msgs]):

			self._createDialogBox('modifier vos données', 'Demande d\'autorisation')

			if self.value:

				file_name, limit = file(), getLimit(self.CBox.currentText())
				guichet = Guichet(self.name.text(), self.code.text(),
					list_amount[self.index], limit,
					self.CBox.currentText().lower(), list_msg[self.index],
					list_time[self.index], None)

				modify_file(file_name, self.index, 'modification', guichet)

				confirm_msg = QLabel()
				confirm_msg.setText(f"{self.name.text()}\n"
					"Vos données ont été modifiées\n"
					f"avec succès {chr(10024)} {chr(10024)}")
				confirm_msg.setAlignment(Qt.AlignCenter)
				confirm_msg.setFont(QFont("Berlin Sans FB", 14))

				self._createCentralWidget()
				self.generalLayout.addWidget(confirm_msg)

	def _delete(self):

		self._createDialogBox('supprimer votre compte', 'Demande d\'autorisation')

		if self.value:

			self.getNewData()

			del_account(list_amount[self.index], self.index)
			#				^						^
			#				|						|
			# : (the user's amount, the user's position in the storage file)

			confirm_msg = QLabel()
			confirm_msg.setText(f"{self.name.text()}\n"
				"Votre compte a été supprimé\n"
				f"avec succès {chr(10024)} {chr(10024)}")
			confirm_msg.setAlignment(Qt.AlignCenter)
			confirm_msg.setFont(QFont("Berlin Sans FB", 14))

			self._createCentralWidget()
			self.generalLayout.addWidget(confirm_msg)

	def _transfer(self):

		global name, amount

		name = QLabel()
		amount = QLabel()

		name.setText("Nom du destinataire:")
		name.setFont(QFont("Berlin Sans FB", 11))

		amount.setText("Montant de transfert:")
		amount.setFont(QFont("Berlin Sans FB", 11))

		self._createCentralWidget()

		self._createTitle('TRANSFERT D\'ARGENT')

		self._name = QLineEdit()

		self._name.setAlignment(Qt.AlignCenter)
		self._name.setFont(QFont("Comic Sans Ms", 14))

		self._createAmount()
		self._createOkButton(self._transfer_validation)

		self.addLabels([self._name, self.amount], self.ok, [name, amount], ['', ''])

	def _transfer_validation(self):

		self.getNewData()

		cards = {'azur': azur_min, 'gold': gold_min, 'premium': premium_min,
				'visa': visa_min, 'vip': vip_min}

		if self._name.text() not in list_users:
			msg_name = self.redFont('Compte inexistant')
		elif self._name.text() == list_users[self.index]:
			msg_name = self.redFont('Auto-transfert impossible')
		else:
			msg_name = ''


		if self.amount.text() == '':
			msg_amount = self.redFont('Veuillez entrer un montant')
		elif msg_name == self.redFont('Compte inexistant'):
			msg_amount = ''
		elif msg_name == self.redFont('Auto-transfert impossible'):
			msg_amount = ''
		elif int(self.amount.text().replace('  ', '')) < cards.get(list_card[self.index]):
			msg_amount = self.redFont('Vous ne pouvez entrer moins '
						f'de {currentie(sep(cards.get(list_card[self.index])))}')
		elif list_amount[self.index] - int(self.amount.text().replace('  ', '')) < list_limits[self.index]:
			new_balance = currentie(sep(list_amount[self.index] - 
				int(self.amount.text().replace('  ', ''))))
			msg_amount = self.redFont('Votre nouveau solde'
						+f" ({new_balance}) <br>"
						+f" sera inférieur à votre limite ({currentie(sep(list_limits[self.index]))})")
		else:
			msg_amount = ''

		msgs = [msg_name, msg_amount]

		self.addLabels([self._name, self.amount], self.ok, [name, amount], msgs)

		if all([i == '' for i in msgs]):

			date = new_date()
			bank_chief = data.bank_chief()

			costs = {'azur': azur_perc, 'gold': gold_perc, 'premium': premium_perc,
					'visa': visa_perc, 'vip': vip_perc}

			if list_users[self.index] not in bank_chief:
				cost = costs.get(list_card[self.index])
				_cost = remove_costs(int(self.amount.text().replace('  ', '')), cost)
			else:
				_cost = 0

			list_amount[self.index]-=(_cost+int(self.amount.text().replace('  ', '')))

			_file_name = cost_file()
			add_costs(_file_name, _cost)

			recipient_index = list_users.index(self._name.text())
			list_amount[recipient_index]+=int(self.amount.text().replace('  ', ''))

			file_name = file()

			guichet = Guichet(list_users[self.index], list_codes[self.index],
				list_amount[self.index], list_limits[self.index],
				list_card[self.index], list_msg[self.index],
				list_time[self.index], self.index)

			recipient_guichet = Guichet(self._name.text(), list_codes[recipient_index],
				list_amount[recipient_index], list_limits[recipient_index],
				list_card[recipient_index], list_msg[recipient_index],
				list_time[recipient_index], recipient_index)

			modify_file(file_name, self.index, 'modification', guichet)
			modify_file(file_name, recipient_index, 'transfer',
				recipient_guichet, (list_users[self.index],
					int(self.amount.text().replace('  ', '')), date))

			confirm_msg = QLabel()
			confirm_msg.setText(f"{list_users[self.index]}\n"
				"Votre transfert a été effectué\n"
				f"avec succès {chr(10024)} {chr(10024)}")
			confirm_msg.setAlignment(Qt.AlignCenter)
			confirm_msg.setFont(QFont("Berlin Sans FB", 14))

			self._createCentralWidget()
			self.generalLayout.addWidget(confirm_msg)

	def _createFields(self):

		global name, code, confirm_code, card, amount

		self._createTitle('CRÉATION D\'UN NOUVEAU COMPTE')
		self._createName()
		self._createCode()
		self._createConfirmCode()
		self._createCards()
		self._createAmount()
		self._createSaveButton(self.verify_validation)

		name = QLabel()
		code = QLabel()
		confirm_code = QLabel()
		card = QLabel()
		amount = QLabel()

		name.setText("Nom:")
		name.setFont(QFont("Berlin Sans FB", 11))

		code.setText("Code:")
		code.setFont(QFont("Berlin Sans FB", 11))

		confirm_code.setText("Confirmation du code:")
		confirm_code.setFont(QFont("Berlin Sans FB", 11))

		card.setText("Types de carte:")
		card.setFont(QFont("Berlin Sans FB", 11))

		amount.setText("Montant de création:")
		amount.setFont(QFont("Berlin Sans FB", 11))

		self.addLabels([self.name, self.code, self.confirm_code, self.CBox, self.amount],
			self.save, [name, code, confirm_code, card, amount], ['', '', '', '', ''])

	def verify_validation(self):

		self.getNewData()

		if self.name.text() == '':
			msg_name = self.redFont('Veuillez entrer votre nom')
		elif self.name.text() in list_users:
			msg_name = self.redFont('Compte existant')
		else:
			msg_name = ''


		if (len(self.code.text()) < 4):
			msg_code = self.redFont('Veuillez entrer un code à 4 chiffres')
		else:
			msg_code = ''


		if (len(self.confirm_code.text()) < 4):
			msg_confirm_code = self.redFont('Veuillez entrer un code à 4 chiffres')
		if self.confirm_code.text() != self.code.text():
			msg_confirm_code = self.redFont('Code incorrect')
		else:
			msg_confirm_code = ''


		if self.CBox.currentText() == '':
			msg_card = self.redFont('Veuillez choisir un type de carte')
		else:
			limit = getLimit(self.CBox.currentText())
			msg_card = ''


		if self.amount.text() == '':
			msg_amount = self.redFont('Veuillez entrer un montant')
		elif msg_card == self.redFont('Veuillez choisir un type de carte'):
			msg_amount = self.redFont('Choisissez d\'abord un type de carte')
		elif int(self.amount.text().replace('  ', '')) < limit:
			msg_amount = self.redFont(' Ce montant est inférieur à votre limite')
		else:
			msg_amount = ''

		msgs = [msg_name, msg_code, msg_confirm_code, msg_card, msg_amount]

		self.addLabels([self.name, self.code, self.confirm_code, self.CBox, self.amount],
			self.save, [name, code, confirm_code, card, amount], msgs)

		if all([i == '' for i in msgs]):

			addAccount(file(), self.name.text(), self.code.text(),
				limit, self.amount.text(), self.CBox.currentText())

			confirm_msg = QLabel()
			confirm_msg.setText(f"{self.name.text()}\n"
				"Bienvenue à < By Zuch & Co. > votre banque virtuelle\n"
				f"Votre compte a été créé avec succès {chr(10024)} {chr(10024)}")
			confirm_msg.setAlignment(Qt.AlignCenter)
			confirm_msg.setFont(QFont("Berlin Sans FB", 14))

			self._createCentralWidget()
			self.generalLayout.addWidget(confirm_msg)

	def choose_card(self, select):

		if select != 0:

			card_name = self.CBox.currentText()
			self._createMessageBox(card_name,
				_doc(card_name.lower()))

	def _textChanged(self, text):

		if text == '':
			pass

		elif ('-' in text) or ('+' in text):

			text = text.replace('-', '')
			text = text.replace('+', '')
			text = text.replace('  ', '')

			if text != '':
				text = sep(int(text)) # It's the thousand separator

		else:

			text = text.replace('  ', '')
			text = sep(int(text))

		self.amount.setText(text)

	def text_changed(self, widget):

		if ('-' in widget.text()) or ('+' in widget.text()):

			text = widget.text().replace('-', '')
			text = widget.text().replace('+', '')
			widget.setText('')
			widget.setText(text)

	def addLabels(self, widgets, button, labels, errors):

		fbox = QFormLayout()

		fbox.addRow(self.title)
		fbox.addRow(QLabel())

		for i in range(len(errors)):

			fbox.addRow(labels[i], widgets[i])

			msg = QLabel()
			msg.setText(errors[i])
			msg.setAlignment(Qt.AlignRight)
			fbox.addRow(msg)

		self._createCentralWidget()
		self.generalLayout.addLayout(fbox)
		self.generalLayout.addWidget(button)

	def addSingleLabel(self, widget, button, label, error, option):

		fbox, msg = QFormLayout(), QLabel()

		fbox.addRow(label, widget)
		msg.setText(error)
		msg.setAlignment(Qt.AlignRight)
		fbox.addRow(msg)
		fbox.addRow(button)

		self._createWidget(option)
		generalLayout.addLayout(fbox)
		dialog.setLayout(generalLayout)
		dialog.exec_()
		dialog.close()

	def redFont(self, text):
		return '<FONT COLOR="RED">' + text + '</FONT>'

def window():
	""" Main function """

	app = QApplication(argv)
	app.setStyle('Fusion')

	win = MainWindow()
	win.show()
	exit(app.exec_())

window()