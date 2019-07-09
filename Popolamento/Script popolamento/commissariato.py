import random

def randomPec():
	p1 = ['comm','upgsp','ammin.comm']
	p2 = ['castelvolturno.ce','aversa.ce','sessaaurunca.ce','smcapuavetere.ce','maddaloni.ce','afragola.na','vomero.na','arenella.na','chiaiano.na','decumani.na','montecalvario.na','posillipo.na','giugliano.na','palazzodigiustizia.na','torredelgreco.na','torreannunziata.na','sangiuseppevesuviano.na','sangiorgioacremano.na','portici.na']
	return random.choice(p1)+'.'+random.choice(p2)+'@'+'pecps.poliziadistato.it'

	
def randomViaComm():
	p1 = ['Roma','Garibaldi','Marconi','Mazzini','Dante','Cavour','Matteotti','Verdi','IV Novembre','Giovanni XXIII','Antonio Gramsci','Alcide De Gasperi','Turati','San Rocco','San Francesco','San Martino','Sant\' Antonio','Piave','Vittorio Veneto','Risorgimento','Nino Bixio','Silvio Pellico','Manzoni']
	return 'Via '+random.choice(p1)+' '+str(random.randint(1,199))

def randomCittaPec(pec):
	if 'castelvolturno' in pec:
		return 'Castel Volturno'
	elif 'aversa' in pec:
		return 'Aversa'
	elif 'sessaaurunca' in pec:
		return 'Sessa Aurunca'
	elif 'smcapuavetere' in pec:
		return 'Santa Maria Capua Vetere'
	elif 'maddaloni' in pec:
		return 'Maddaloni'
	elif 'afragola' in pec:
		return 'Afragola'
	elif 'vomero' in pec or 'arenella' in pec or 'chiaiano' in pec or 'decumani' in pec or 'montecalvario' in pec or 'posillipo' in pec or 'palazzodigiustizia' in pec:
		return 'Napoli'
	elif 'giugliano' in pec:
		return 'Giugliano in Campania'
	elif 'torreannunziata' in pec:
		return 'Torre Annunziata'
	elif 'torredelgreco' in pec:
		return 'Torre del Greco'
	elif 'sangiorgioacremano' in pec:
		return 'San Giorgio a Cremano'
	elif 'sangiuseppevesuviano' in pec:
		return 'San Giuseppe Vesuviano'
	elif 'portici' in pec:
		return 'Portici'
	else:
		return 'CITTA'

def randomNomeComm(pec,citta):
	p1 = ['Amministrativa', 'RP', 'Amministrativa e sociale', 'Denunce', 'Corrispondenza']
	if citta == 'Napoli':
		if 'vomero' in pec:
			return 'Commissariato Napoli '+'Vomero - Ufficio '+random.choice(p1)
		elif 'arenella' in pec:
			return 'Commissariato Napoli '+'Arenella - Ufficio '+random.choice(p1)
		elif 'chiaiano' in pec:
			return 'Commissariato Napoli '+'Chiaiano - Ufficio '+random.choice(p1)
		elif 'decumani' in pec:
			return 'Commissariato Napoli '+'Decumani - Ufficio '+random.choice(p1)
		elif 'montecalvario' in pec:
			return 'Commissariato Napoli '+'Montecalvario - Ufficio '+random.choice(p1)
		elif 'posillipo' in pec:
			return 'Commissariato Napoli '+'Posillipo - Ufficio '+random.choice(p1)
		elif 'palazzodigiustizia' in pec:
			return 'Commissariato Napoli '+'Palazzo di Giustizia - Ufficio '+random.choice(p1)
	else:
		if citta == 'Castel Volturno':
			return 'Commissariato Castel Volturno - Ufficio '+random.choice(p1)
		elif citta == 'Aversa':
			return 'Commissariato Aversa - Ufficio '+random.choice(p1)
		elif citta == 'Sessa Aurunca':
			return 'Commissariato Sessa Aurunca - Ufficio '+random.choice(p1)
		elif citta == 'Santa Maria Capua Vetere':
			return 'Commissariato S. Maria Capua Vetere - Ufficio '+random.choice(p1)
		elif citta == 'Maddaloni':
			return 'Commissariato Maddaloni - Ufficio '+random.choice(p1)
		elif citta == 'Afragola':
			return 'Commissariato Afragola - Ufficio '+random.choice(p1)
		elif citta == 'Giugliano in Campania':
			return 'Commissariato Giugliano - Ufficio '+random.choice(p1)
		elif citta == 'Torre Annunziata':
			return 'Commissariato Torre Annunziata - Ufficio '+random.choice(p1)
		elif citta == 'Torre del Greco':
			return 'Commissariato Torre del Greco - Ufficio '+random.choice(p1)
		elif citta == 'San Giorgio a Cremano':
			return 'Commissariato S. Giorgio a Cremano - Ufficio '+random.choice(p1)
		elif citta == 'San Giuseppe Vesuviano':
			return 'Commissariato S. Giuseppe Vesuviano - Ufficio '+random.choice(p1)
		elif citta == 'Portici':
			return 'Commissariato Portici - Ufficio '+random.choice(p1)
		else:
			return 'Commissariato Ufficio '+random.choice(p1)

for i in range (0, 5):
	pec = randomPec()
	citta = randomCittaPec(pec)
	print("INSERT INTO COMMISSARIATO (PEC, NOME_COMM, CAP_COMM, VIA_COMM, CITTA_COMM)", file=open("popolamento_commissariato.sql","a"))
	print("VALUES ('{}','{}',_____,'{}','{}');".format(pec, randomNomeComm(pec,citta), randomViaComm(), citta), file=open("popolamento_commissariato.sql","a"))