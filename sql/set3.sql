-- 26 Create a Rides table / collection with the fields defined above.
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);


-- 27 Insert five rows / documents into the Rides table / collection with data of your choice.
INSERT INTO Rides (id, rider_name, driver_name, ride_date, fare, completed)
VALUES
    (1, 'Alice', 'John', '2023-08-10', 20.50, TRUE),
    (2, 'Bob', 'Emily', '2023-08-11', 18.75, TRUE),
    (3, 'Charlie', 'Sarah', '2023-08-12', 15.20, TRUE),
    (4, 'David', 'Jessica', '2023-08-12', 30.00, TRUE),
    (5, 'Eve', 'Michael', '2023-08-13', 25.80, FALSE);


-- 28 Write a query to fetch all rides, ordered by fare in descending order.
SELECT * FROM Rides
ORDER BY fare DESC

-- 29  Write a query to calculate the total distance and total fare for all rides.
SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare
FROM RideDetails;

-- 30 Write a query to calculate the average ride_time of all rides.
SELECT AVG(ride_time) AS average_ride_time
FROM rides;

-- 31 Write a query to fetch all rides whose start_location or end_location contains 'Downtown'.
SELECT *
FROM rides
WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';

-- 32 Write a query to count the number of rides for a given driver_id
SELECT COUNT(*) AS ride_count
FROM Rides
WHERE driver_id = your_driver_id;

-- 33 Write a query to update the fare of the ride with id 4.
UPDATE rides
SET fare = new_fare_value
WHERE id = 4;

-- 34 Write a query to delete the ride with id 2.
DELETE FROM rides
WHERE id = 2;
