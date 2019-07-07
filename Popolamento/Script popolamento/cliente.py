import random
import string

def randomPDA():
	return str(random.randint(11111,99999))+'-'+random.choice(string.ascii_uppercase)
	
def randomTEL():
	return str(3)+str(random.randint(30,99))+str(random.randint(1111111,9999999))
	
for i in range (0, 5):
	print("INSERT INTO CLIENTE (NUM_PORTO_ARMI,CF_CLI,TELEFONO)", file=open("popolamento_cliente.sql","a"))
	print("VALUES ('{}','(cf_cli)',{});".format(randomPDA(),randomTEL()), file=open("popolamento_cliente.sql","a"))