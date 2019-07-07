import random
import string

def randomNL():
	return str(random.randint(1111111111,9999999999))

for i in range (0, 5):
	print("INSERT INTO MUNIZIONI (NUM_LOTTO,CODICE_PRODOTTO)", file=open("popolamento_munizioni.sql","a"))
	print("VALUES ('{}','(codice_prodotto)');".format(randomNL()), file=open("popolamento_munizioni.sql","a"))