-- creates a function `SafeDiv` that devides (and  returns)
-- the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION IF NOT EXISTS SafeDiv(
	a INT,
	b INT
)
BEGIN
	DECLARE result FLOAT DEFAULT 0;
	IF b != 0 THEN
		SET result = a / b;
	END IF;
	RETURN result;
END $$ ;
