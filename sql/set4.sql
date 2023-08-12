-- 36.  Write a query to find the ride with the highest and lowest fare
SELECT *
FROM rides
ORDER BY fare DESC
LIMIT 1;

SELECT *
FROM rides
ORDER BY fare ASC
LIMIT 1;

-- 37.Write a query to find the average fare and distance for each driver_id.
SELECT driver_id, AVG(fare) AS average_fare, AVG(distance) AS average_distance
FROM rides
GROUP BY driver_id;
