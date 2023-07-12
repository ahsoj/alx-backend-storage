-- create a table
-- add not null and unique constraints
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
)
