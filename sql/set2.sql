-- 16 Create a Restaurants table / collection with the fields defined above.

CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

-- 17  Insert five rows / documents into the Restaurants table / collection with data of your choice.
INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
VALUES
    (1, 'The Food Haven', 'Italian', '123 Main St, Cityville', 4.7, TRUE),
    (2, 'Spice Junction', 'Indian', '456 Elm St, Townsville', 4.2, TRUE),
    (3, 'Sushi Delight', 'Japanese', '789 Oak St, Villageton', 4.8, FALSE),
    (4, 'Burger Bliss', 'American', '101 Maple Ave, Hamletville', 4.5, TRUE),
    (5, 'Mama Mia Pizzeria', 'Italian', '555 Pine Rd, Suburbia', 4.3, TRUE);

-- 18 Write a query to fetch all restaurants, ordered by average_rating in descending order.
SELECT * FROM Restaurants
ORDER BY average_rating DESC;

-- 19 Write a query to fetch all restaurants that offer delivery_available and have an average_rating of more than 4.
SELECT * FROM Restaurants
WHERE delivery_available = TRUE AND average_rating>4

-- 20query to fetch all restaurants where the cuisine_type field is not set or is null.
SELECT *
FROM Restaurants
WHERE cuisine_type IS NULL OR cuisine_type = '';

-- 21 Write a query to count the number of restaurants that have delivery_available.
SELECT COUNT(*) AS delivery_restaurant_count
FROM Restaurants
WHERE delivery_available = TRUE;
