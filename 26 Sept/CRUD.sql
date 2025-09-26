CREATE TABLE Employees (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
    );
    
INSERT INTO Employees (name, age, department, salary)
VALUES
('Simeen',22,'ML',50000),
('Shayaan',20,'AI',60000);

SELECT * from Employees;

UPDATE Employees
SET salary = 70000, department = 'Data Science'
WHERE id = 4;

DELETE FROM Employees WHERE id = 3;
    