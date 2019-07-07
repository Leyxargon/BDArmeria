import random
import string

def randomVia():
	p1 = ['Roma','Garibaldi','Marconi','Mazzini','Dante','Cavour','Matteotti','Verdi','IV Novembre','Giovanni XXIII','Antonio Gramsci','Alcide De Gasperi','Turati','San Rocco','San Francesco','San Martino','Sant\' Antonio','Piave','Vittorio Veneto','Risorgimento','Nino Bixio','Silvio Pellico','Manzoni','Michelangelo Buonarroti','Torquato Tasso','Giovanni Boccaccio','Don Minzoni','Vittorio Emanuele','Alessandro Volta','Galileo Galilei','Fiume','Gorizia','Goffredo Mameli','Giacomo Puccini','Leonardo Da Vinci','Giovanni Pascoli','Suarez','Armando Diaz','Giuseppe Di Vittorio','John Fitzgerald Kennedy']
	return 'Via '+random.choice(p1)+' '+str(random.randint(1,199))
	
def randomCitta():
	p1 = ['Napoli','Caserta','Salerno','Avellino','Benevento','Pozzuoli','Giugliano in Campania','Aversa','Torre del Greco','Castel Volturno','Bacoli','Battipaglia','Pontecagnano Faiano','Somma Vesuviana','Sarno','Sorrento','Pompei','Mondragone','Ottaviano','San Giuseppe Vesuviano','Portici','San Giorgio a Cremano','Villa Literno','Eboli','Angri','Cava de\' Tirreni','Atripalda','Ariano Irpino']
	p2 = [40,6,10,5,3,7,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	c = str(random.choices(p1,p2,k=1))
	cc = c.replace('[','').replace(']','')
	return cc
	
def randomNome():
	p1 = ['Francesco','Francesca','Giovanni','Giovanna','Mario','Maria','Raffaele','Raffaella','Giuseppe','Giusy','Dario','Daria','Salvatore','Alessandro','Alessandra','Gennaro','Vincenzo','Vincenza','Ciro','Antonio','Antonia','Emanuele','Emanuela','Matteo','Sara','Paolo','Paola','Luca','Nicola','Michele','Noemi','Davide','Rita']
	return random.choice(p1)
	
def randomCognome():
	p1 = ['Rossi','Russo','Ferrari','Esposito','Bianchi','Romano','Colombo','Ricci','Marino','Greco','Bruno','Gallo','Conti','Bianco','Mancini','Costa','Giordano','Rizzo','Moretti','Barbieri','Santoro']
	return random.choice(p1)
	
def randomCF(cognome, nome, datanascita):
	CFcog = cognome[0].upper()+cognome[1].upper()+cognome[2].upper()
	CFnom = nome[0].upper()+nome[1].upper()+nome[2].upper()
	CFan = datanascita[8]+datanascita[9]
	if datanascita in '-01':
		CFme = 'A'
	elif datanascita in '-02':
		CFme = 'B'
	elif datanascita in '-03':
		CFme = 'C'
	elif datanascita in '-04':
		CFme = 'D'
	elif datanascita in '-05':
		CFme = 'E'
	elif datanascita in '-06':
		CFme = 'H'
	elif datanascita in '-07':
		CFme = 'L'
	elif datanascita in '-08':
		CFme = 'M'
	elif datanascita in '-09':
		CFme = 'P'
	elif datanascita in '-10':
		CFme = 'R'
	elif datanascita in '-11':
		CFme = 'S'
	else:
		CFme = 'T'
	CFgi = datanascita[0]+datanascita[1]
	CFct = random.choice(string.ascii_uppercase)+str(random.randint(100,999))
	CFfin = random.choice(string.ascii_uppercase)
	return CFcog+CFnom+CFan+CFme+CFgi+CFct+CFfin

def randomDN():
	aa = str(random.randint(1940,1999))
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
	
for i in range (0, 5):
	nome = randomNome()
	cognome = randomCognome()
	datanascita = randomDN()
	CF = randomCF(cognome, nome, datanascita)
	print("INSERT INTO PERSONA (CF,NOME,COGNOME,DATA_NASCITA,VIA,CAP,CITTA)", file=open("popolamento_persona.sql","a"))
	print("VALUES ('{}','{}','{}',to_date('{}', 'dd-mm-yyyy'),'{}','_',{});".format(CF, nome, cognome, datanascita, randomVia(),randomCitta()), file=open("popolamento_persona.sql","a"))