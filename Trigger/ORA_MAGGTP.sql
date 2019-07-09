CREATE OR REPLACE TRIGGER ORA_MAGGTP
BEFORE INSERT ON TURNI_PROGRAMMATI
FOR EACH ROW
DECLARE
	ORARIO	EXCEPTION;
BEGIN
	IF :NEW.ORA_TP>'21:00' OR :NEW.ORA_TP<'07:30'  THEN
		RAISE ORARIO;
	END IF;
EXCEPTION
	WHEN ORARIO THEN
		RAISE_APPLICATION_ERROR(-20003,'Armeria Chiusa');
END;
/