-- 1.Create a Customers table / collection with the following fields: id (unique identifier), name, email, address, and phone_number.

CREATE TABLE Customers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    address VARCHAR(255),
    phone_number VARCHAR(20) 
)

-- 2 Insert five rows / documents into the Customers table / collection with data of your choice.

INSERT INTO Customers (name, email, address, phone_number)
VALUES
    ('John Doe', 'john@example.com', '123 Main St, City', '555-1234'),
    ('Jane Smith', 'jane@example.com', '456 Elm St, Town', '555-5678'),
    ('Michael Johnson', 'michael@example.com', '789 Oak St, Village', '555-9876'),
    ('Emily Brown', 'emily@example.com', '987 Pine St, Hamlet', '555-4321'),
    ('William Davis', 'william@example.com', '654 Birch St, Village', '555-8765');


-- 3 Write a query to fetch all data from the Customers table / collection
SELECT * FROM Customers;

-- 4 Write a query to select only the name and email fields for all customers.
SELECT name, email * FROM Customers

-- 5Write a query to select only the name and email fields for all customers.
SELECT * FROM Customers WHERE id = 1

-- 6. Write a query to fetch all customers whose name starts with 'A'.

SELECT * FROM Customers WHERE name LIKE 'A%';

-- 7 .fetch all customers, ordered by name in descending order.
SELECT * FROM Customers ORDER BY email DESC

-- 8 update the address of the customer with id 4.
UPDATE Customers 
SET address = "this is new address"
WHERE id = 1

-- 9 query to fetch the top 3 customers when ordered by id in ascending order.
SELECT * FROM Customers
ORDER BY id ASC
LIMIT = 3

-- 10 query to fetch the top 3 customers when ordered by id in ascending order.
DELETE FROM Customers
WHERE id = 3

-- 11 count the number of customers

SELECT count(*) AS total_customer
FROM Customers

-- 12 Write a query to fetch all customers except the first two when ordered by id in ascending order.
SELECT * FROM Customers
ORDER BY id ASC
LIMIT -1
 OFFSET 2

--  13 fetch all customers whose id is greater than 2 and name starts with 'B'.
SELECT * FROM Customers
WHERE id>2 AND LIKE 'B%'

-- 14 query to fetch all customers whose id is less than 3 or name ends with 's'
SELECT * FROM Customers 
WHERE id<3 AND LIKE '%s'

-- 15

 SELECT *
FROM Customers
WHERE phone_number IS NULL OR phone_number = ''
