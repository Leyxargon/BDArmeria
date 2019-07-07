import random
import string

def randomNumTesserino():
	return random.randint(1111111111,9999999999)

for i in range (0, 5):
	print("INSERT INTO DIPENDENTE (NUM_TESSERINO,CF)", file=open("popolamento_dipendente.sql","a"))
	print("VALUES ('{}','(cf)');".format(randomNumTesserino()), file=open("popolamento_dipendente.sql","a"))