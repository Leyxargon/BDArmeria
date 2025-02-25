CREATE OR REPLACE PROCEDURE NuovoAccessorio (
	COD_BAR				VARCHAR2,
	NOME_A				VARCHAR2,
	COD_FORN			VARCHAR2,
	DATA_SPEDIZ			DATE,
	PREZZO				NUMBER,
	P_IVA				VARCHAR2
	)
AS
	WRONGSPEDIZIONE 	EXCEPTION;
BEGIN
	-- VERIFICA CORRETTEZZA TEMPORALE DELLA DATA
	IF DATA_SPEDIZ > SYSDATE THEN
		RAISE WRONGSPEDIZIONE;
	END IF;
	
	INSERT INTO FORNITURA (COD_FORNITURA,DATA_SPEDIZIONE,PREZZO_LOTTO,P_IVA_FORN)
	VALUES (COD_FORN,DATA_SPEDIZ,PREZZO,P_IVA);
		
	INSERT INTO ACCESSORIO (COD_BARRE,NOME_ACC)
	VALUES (COD_BAR, NOME_A);
		
	INSERT INTO CONTIENE (COD_FORNITURA, COD_BARRE_ACC)
	VALUES (COD_FORN, COD_BAR);
		
EXCEPTION
	WHEN WRONGSPEDIZIONE THEN
		RAISE_APPLICATION_ERROR(-20025, 'Data non corretta');

END;
/	