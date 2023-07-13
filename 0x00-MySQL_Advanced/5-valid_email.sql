-- create a trigger that resets the atribute `valid_email`
-- only when the `email` das been changed
DELIMITER $$ ;
CREATE TRIGGER validate BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;$$
