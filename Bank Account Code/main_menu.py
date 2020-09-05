from center_text import center_text

def main_menu():

	style = '***************************************'
	print('',
		  center_text(style),
		  center_text("*            MENU PRINCIPAL           *"),
		  center_text("*                                     *"),
		  center_text("* 1. CREATION D'UN NOUVEAU COMPTE     *"),
		  center_text("* 2. CONNEXION A UN COMPTE EXISTANT   *"),
		  center_text("* 3. MODIFICATION DES DONNÉES         *"),
		  center_text("* 4. TRANSFERT D'ARGENT               *"),
		  center_text("* 5. SUPPRESSION D'UN COMPTE EXISTANT *"),
		  center_text("* 6. DECONNEXION                      *"),
		  center_text("*                                     *"),
		  center_text(style), sep='\n')