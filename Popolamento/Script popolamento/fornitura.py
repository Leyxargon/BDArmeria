import random
import string
	
def randomCOF():
	return str(random.randint(1111111111,9999999999))

def randomData():
	aa = str(random.randint(2015,2018))
	m = random.randint(1,12)
	if m < 10:
		mm = str(0)+str(m)
	else:
		mm = str(m)
	if mm == '01' or mm == '03' or mm == '05' or mm == '07' or mm == '08' or mm == '10' or mm == '12':
		g = random.randint(1,31)
		if g < 10:
			gg = str(0)+str(g)
		else:
			gg = str(g)
	elif mm == '02':
		g = random.randint(1,28)
		if g < 10:
			gg = str(0)+str(g)
		else:
			gg = str(g)
	else:
		g = random.randint(1,30)
		if g < 10:
			gg = str(0)+str(g)
		else:
			gg = str(g)
	return gg+'-'+mm+'-'+aa

def randomImporto():
	return round(random.uniform(500.00,10000.00), 2)

for i in range (0, 5):
	print("INSERT INTO FORNITURA (COD_FORNITURA,DATA_SPEDIZIONE,PREZZO_LOTTO,P_IVA_FORN)", file=open("popolamento_fornitura.sql","a"))
	print("VALUES ({},to_date('{}', 'dd-mm-yyyy'),{},(p_iva_forn));".format(randomCOF(),randomData(),randomImporto()), file=open("popolamento_fornitura.sql","a"))