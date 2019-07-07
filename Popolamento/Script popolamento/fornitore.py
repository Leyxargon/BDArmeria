import random
import string

def randomPIVA():
	return str(random.randint(11111111111,99999999999))

def randomTEL():
	return str(3)+str(random.randint(30,99))+str(random.randint(1111111,9999999))

def randomDen():
	p1 = ['F.lli', 'Fornitori']
	p11 = [0.3,0.7]
	p2 = ['Esposito','Rossi','Russo','Sorrentino','Izzo','Fusco','Salvini','Di Maio','Zingaretti','Meloni','Albertazzi','Zorzi','Bianchi','Aliperti','Tascone','Miele','Neri','Musella','Venuso','Bellini','Martino','Palmieri','Donnarumma','Martinelli']
	p3 = ['Srl', 'SaS','Company','Group']
	return str(random.choices(p1,p11,k=1)).replace('[','').replace(']','').replace('\'','')+' '+random.choice(p2)+' '+random.choice(p3)
	

for i in range (0, 5):
	print("INSERT INTO FORNITORE (P_IVA_FORN,DENOMINAZIONE,TELEFONO_FORN)", file=open("popolamento_fornitore.sql","a"))
	print("VALUES ({},'{}',{});".format(randomPIVA(),randomDen(),randomTEL()), file=open("popolamento_fornitore.sql","a"))