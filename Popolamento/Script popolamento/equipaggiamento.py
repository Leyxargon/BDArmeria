import random
import string

def randomCP():
	return random.randint(1111111111,9999999999)

def randomCalibro():
	return random.randint(10,58)
	
def randomMarca():
	m = ['Beretta','Glock','Fiocchi Munizioni','Franchi','Jager','Pardini']
	return random.choice(m)

for i in range (0, 5):
	print("INSERT INTO EQUIPAGGIAMENTO (CODICE_PRODOTTO, CALIBRO, MARCA, COD_FORNITURA, NUM_PORTO_ARMI, NUM_PROG)", file=open("popolamento_equipaggiamento.sql","a"))
	print("VALUES ('{}', {}, '{}', '(cod_fornitura)', '(num_porto_armi)', '(num_prog)');".format(randomCP(),randomCalibro(),randomMarca()), file=open("popolamento_equipaggiamento.sql","a"))