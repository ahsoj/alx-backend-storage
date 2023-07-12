-- create a table
-- add not null and unique constraints
CREATE TABLE IF [NOT EXISTS] users(
	id INT NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	name varchar(255)
)
