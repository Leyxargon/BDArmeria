import random
import string

def randomMod():
	m = ['Fucile d\'assalto', 'Pistola a tamburo', 'Fucile automatico', 'Fucile semiautomatico', 'Fucile a pompa', 'Fucile a canne mozze', 'SMG', 'Mitragliatrice leggera', 'Mitragliatrice pesante', 'Revolver', 'Pistola semiautomatica', 'Fucile di precisione', 'Fucile anticarro', 'Fucile da battaglia', 'Sovrapposto', 'Fucile a canna liscia']
	return random.choice(m)

def randomMatricola():
	return ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(7)])

for i in range (0, 5):
	print("INSERT INTO ARMA (MATRICOLA,MODELLO,CODICE_PRODOTTO)", file=open("popolamento_arma.sql","a"))
	print("VALUES ('{}','{}','(codice_prodotto)');".format(randomMatricola(),randomMod()), file=open("popolamento_arma.sql","a"))