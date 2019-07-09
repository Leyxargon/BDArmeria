import random
import string

def randomCB():
	return str(random.randint(1111111111111,9999999999999))

def randomNA():
	n = ['Cartucciera','Fondina','Portacaricatori','Prolunga serbatoio','Bipiede','Calciolo','Occhiali','Cuffia isolante','Guanti','Richiamo','Tromba','Serratura grilletto','Kit pulizia','Salvapercussori','Zaino monospalla','Torcia mimetica','Visore notturno','Bersaglio in metallo','Bersaglio in cartone','Anfibi','Scarpone da montagna','Passamontagna','Ombrello mimetico','Auricolari antirumore','Stivali a tromba','Paragrilletto','Torcia frontale','DVD di caccia','Tenda mimetica']
	return random.choice(n)

for i in range (0, 5):
	print("INSERT INTO ACCESSORIO (COD_BARRE,NOME_ACC)", file=open("popolamento_accessorio.sql","a"))
	print("VALUES ('{}','{}');".format(randomCB(),randomNA()), file=open("popolamento_accessorio.sql","a"))