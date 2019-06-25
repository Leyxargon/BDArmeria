-- RIPULISCE DB
DROP TABLE COMMISSARIATO;
DROP TABLE DENUNCIA;
DROP TABLE PERSONA;
DROP TABLE DIPENDENTE;
DROP TABLE TURNI_PROGRAMMATI;
DROP TABLE TURNI_EFFETTUATI;
DROP TABLE VENDITA;
DROP TABLE EQUIPAGGIAMENTO;
DROP TABLE ARMA;
DROP TABLE MUNIZIONI;
DROP TABLE ACCESSORIO;
DROP TABLE CONTIENE;
DROP TABLE FORNITURA;
DROP TABLE FORNITORE;
DROP TABLE VENDUTO;
DROP TABLE CLIENTE;

-- CREAZIONE TABELLE
CREATE TABLE COMMISSARIATO(
	PEC					VARCHAR2(50) PRIMARY KEY,
	NOME_COMM			VARCHAR2(50),
	CAP_COMM			NUMBER(5),
	VIA_COMM			VARCHAR(40),
	CITTA_COMM			VARCHAR(20)
);

CREATE TABLE DENUNCIA(
	CODICE_PROGRESSIVO			NUMBER(10) PRIMARY KEY,
	DATA_DENUNCIA				DATE,
	PEC							VARCHAR2(50),
	CF							VARCHAR2(16),
	MATRICOLA					VARCHAR2(7),
	CONSTRAINTS FK_PEC			FOREIGN KEY (PEC)				REFERENCES COMMISSARIATO(PEC),
	CONSTRAINTS FK_CF1			FOREIGN KEY (CF)				REFERENCES PERSONA(CF),
	CONSTRAINTS FK_MAT			FOREIGN KEY (MATRICOLA)			REFERENCES EQUIPAGGIAMENTO(MATRICOLA)
);

CREATE TABLE PERSONA(
	CF							VARCHAR2(16) PRIMARY KEY,
	NOME						VARCHAR2(20),
	COGNOME						VARCHAR2(20),
	DATA_NASCITA				DATE,
	VIA							VARCHAR2(50),
	CAP							NUMBER(5),
	CITTA						VARCHAR2(20)
);

CREATE TABLE DIPENDENTE(
	NUM_TESSERINO				NUMBER(10) PRIMARY KEY,
	CF_DIP						VARCHAR2(16),
	CONSTRAINTS	FK_CF_DIP 		FOREIGN KEY (CF_DIP) 			REFERENCES PERSONA(CF)
);

CREATE TABLE TURNI_PROGRAMMATI(
	DATA_TP						DATE,
	ORA_TP						TIME,
	NUM_TESSERINO				NUMBER(10),
	CONSTRAINTS PK_TP 			PRIMARY KEY (DATA_TP,ORA_TP),
	CONSTRAINTS FK_NUM_TES1 	FOREIGN KEY (NUM_TESSERINO)		REFERENCES DIPENDENTE(NUM_TESSERINO)
);

CREATE TABLE TURNI_EFFETTUATI(
	DATA_TE						DATE,
	ORA_TE						TIME,
	NUM_TESSERINO				NUMBER(10),
	CONSTRAINTS PK_TE 			PRIMARY KEY (DATA_TE,ORA_TE),
	CONSTRAINTS FK_NUM_TES2 	FOREIGN KEY (NUM_TESSERINO)		REFERENCES DIPENDENTE(NUM_TESSERINO)
);

CREATE TABLE VENDITA(
	NUM_PROG					NUMBER(10) PRIMARY KEY,
	DATA_V						DATE,
	ORA_V						TIME,
	IMPORTO						NUMBER(19,4),
	NUM_TESSERINO				NUMBER(10),
	CONSTRAINTS FK_NUM_TES3		FOREIGN KEY (NUM_TESSERINO) 	REFERENCES DIPENDENTE(NUM_TESSERINO)
);

CREATE TABLE EQUIPAGGIAMENTO(
	MATRICOLA					VARCHAR2(7) PRIMARY KEY,
	CALIBRO						NUMBER(2),
	MARCA						VARCHAR2(20),
	COD_FORNITURA				NUMBER(10),
	NUM_PORTO_ARMI				VARCHAR2(8),
	NUM_PROG					NUMBER(10),
	CONSTRAINTS FK_COD_FOR1 	FOREIGN KEY (COD_FORNITURA)		REFERENCES FORNITURA(COD_FORNITURA),
	CONSTRAINTS FK_NUM_POR_ARM	FOREIGN KEY (NUM_PORTO_ARMI)	REFERENCES CLIENTE(NUM_PORTO_ARMI),
	CONSTRAINTS FK_NUM_PROG		FOREIGN KEY (NUM_PROG)			REFERENCES VENDITA(NUM_PROG)
);

CREATE TABLE ARMA(
	MATRICOLA					VARCHAR2(7) PRIMARY KEY,
	MODELLO 					VARCHAR2(20),
	CONSTRAINTS FK_MAT1			FOREIGN KEY (MATRICOLA)			REFERENCES EQUIPAGGIAMENTO(MATRICOLA)
);

CREATE TABLE MUNIZIONI(
	MATRICOLA					VARCHAR2(7) PRIMARY KEY,
	NUM_LOTTO					NUMBER(10),
	CONSTRAINTS FK_MAT2 		FOREIGN KEY (MATRICOLA)			REFERENCES EQUIPAGGIAMENTO(MATRICOLA)
);

CREATE TABLE ACCESSORIO(
	COD_BARRE					NUMBER(13) PRIMARY KEY,
	NOME_ACC					VARCHAR2(20),
);

CREATE TABLE CONTIENE(
	COD_FORNITURA				NUMBER(10),
	COD_BARRE_ACC				NUMBER(13),
	CONSTRAINTS PK_CON			PRIMARY KEY (COD_FORNITURA,COD_BARRE_ACC),
	CONSTRAINTS FK_COD_FOR2		FOREIGN KEY (COD_FORNITURA)		REFERENCES FORNITURA(COD_FORNITURA),
	CONSTRAINTS FK_COD_B1		FOREIGN KEY (COD_BARRE_ACC) 	REFERENCES ACCESSORIO(COD_BARRE)
);

CREATE TABLE FORNITURA(
	COD_FORNITURA				NUMBER(10) PRIMARY KEY,
	DATA_SPEDIZIONE				DATE,
	PREZZO_LOTTO				NUMBER(19,4),
	P_IVA_FORN					NUMBER(11),
	CONSTRAINTS FK_P_IVA_FORN 	FOREIGN KEY (P_IVA_FORN)		REFERENCES FORNITORE(P_IVA_FORN)
);

CREATE TABLE FORNITORE(
	P_IVA_FORN 					NUMBER(11) PRIMARY KEY,
	DENOMINAZIONE				VARCHAR2(20),
	TELEFONO_FORN				NUMBER(10),
);

CREATE TABLE VENDUTO(
	CF_PERSONA					VARCHAR2(16),
	COD_BARRE_ACC				NUMBER(13),
	CONSTRAINTS PK_VEN			PRIMARY KEY (CF_PERSONA,COD_BARRE),
	CONSTRAINTS FK_CF2			FOREIGN KEY (CF_PERSONA) 		REFERENCES PERSONA(CF)
	CONSTRAINTS FK_COD_B2		FOREIGN KEY (COD_BARRE_ACC)		REFERENCES ACCESSORIO(COD_BARRE)
);

CREATE TABLE CLIENTE(
	NUM_PORTO_ARMI				VARCHAR2(8) PRIMARY KEY,
	CF_CLI						VARCHAR2(16),
	TELEFONO					NUMBER(10),
	CONSTRAINTS	FK_CF_CLI		FOREIGN KEY (CF_CLI)			REFERENCES PERSONA(CF)
);