-- create a table
-- add not null and unique constraints
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country NOT NULL DEFAULT "US" CHECK (country IN ('US', 'CO', 'TN')),
	PRIMARY KEY (id),
)
