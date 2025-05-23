CREATE DATABASE IF NOT EXISTS playground;
USE playground;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100),
    salary DECIMAL(10,2)
);

INSERT INTO employees (id, name , age, department, salary)
VALUES
(1, 'Vishal', 19, 'Data Engineering', 35000.00),
(2, 'Ravi', 22, 'Marketing', 25000.00),
(3, 'Sneha', 24, 'HR', 30000.00),
(4, 'Raj', 21, 'Data Engineering', 32000.00),
(5, 'Mehra', 23, 'Finance', 28000.00);

SELECT * FROM employees;

SELECT name, salary FROM employees;

SELECT * FROM employees WHERE department = 'Data Engineering';

SELECT * FROM employees WHERE salary > 36000;

SELECT * FROM employees ORDER BY salary DESC;

SELECT AVG(salary) as avg_salary FROM employees;

SELECT department, COUNT(*) AS total_employees FROM employees GROUP BY department;