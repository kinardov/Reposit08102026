CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	bday DATE,
	payment DECIMAL(12, 2)
);

INSERT INTO users (name, bday, payment) VALUES 
	('Vasia', '2001-01-01', 10000.00),
	('Vera', '2002-02-02', 20000.00);
	

SELECT 

	
	