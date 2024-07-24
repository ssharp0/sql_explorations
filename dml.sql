-- Insert example data into StarSystems
INSERT INTO StarSystems (Name, StarType, DistanceFromEarth)
VALUES 
('Solar System', 'G-Type Main-Sequence', 0),
('Alpha Centauri', 'G-Type Main-Sequence', 4.37);

-- Insert example data into Planets
INSERT INTO Planets (Name, StarSystemID, Diameter, Mass, OrbitalPeriod, Atmosphere)
VALUES 
('Earth', 1, 12742, 5.97, 365.25, 'Nitrogen, Oxygen'),
('Mars', 1, 6779, 0.641, 687, 'Carbon Dioxide');

-- Insert example data into Moons
INSERT INTO Moons (Name, PlanetID, Diameter, OrbitalPeriod)
VALUES 
('Moon', 1, 3474.8, 27.3),
('Phobos', 2, 22.4, 0.319);

-- Insert example data into Missions
INSERT INTO Missions (Name, LaunchDate, TargetPlanetID, TargetMoonID, MissionType)
VALUES 
('Apollo 11', '1969-07-16', 1, 1, 'Lunar Landing'),
('Mars Rover', '2020-07-30', 2, NULL, 'Mars Exploration');

-- Update the distance of Alpha Centauri
UPDATE StarSystems 
SET DistanceFromEarth = 4.24 
WHERE Name = 'Alpha Centauri';

-- Update the atmosphere of Proxima b
UPDATE Planets 
SET Atmosphere = 'Carbon Dioxide, Nitrogen' 
WHERE Name = 'Proxima b';

-- Update the distance of Alpha Centauri
UPDATE StarSystems 
SET DistanceFromEarth = 4.24 
WHERE Name = 'Alpha Centauri';

-- Update the atmosphere of Proxima b
UPDATE Planets 
SET Atmosphere = 'Carbon Dioxide, Nitrogen' 
WHERE Name = 'Proxima b';

-- Delete a specific moon
DELETE FROM Moons 
WHERE Name = 'Proxima b I';

-- Delete a specific mission
DELETE FROM Missions 
WHERE Name = 'Proxima Centauri Mission';

-- Select all star systems
SELECT * FROM StarSystems;

-- Select specific columns from planets
SELECT Name, Diameter, Mass 
FROM Planets;

-- Select all moons orbiting a specific planet
SELECT * FROM Moons 
WHERE PlanetID = 1;

-- Select missions targeting a specific planet
SELECT * FROM Missions 
WHERE TargetPlanetID = 1;

-- Find planets that are larger than the average diameter of planets in their star system
SELECT p1.Name AS PlanetName, p1.StarSystemID, p1.Diameter
FROM Planets p1
WHERE p1.Diameter > (
    SELECT AVG(p2.Diameter)
    FROM Planets p2
    WHERE p2.StarSystemID = p1.StarSystemID
);

-- Rank planets by diameter within each star system and calculate the average diameter of the top 2 planets in each star system
WITH RankedPlanets AS (
    SELECT p.Name, p.StarSystemID, p.Diameter,
           RANK() OVER (PARTITION BY p.StarSystemID ORDER BY p.Diameter DESC) AS DiameterRank
    FROM Planets p
)
SELECT StarSystemID, AVG(Diameter) AS AvgTop2Diameters
FROM RankedPlanets
WHERE DiameterRank <= 2
GROUP BY StarSystemID;

-- Count of rows in each table
SELECT 'StarSystems' AS TableName, COUNT(*) AS RowCount FROM StarSystems
UNION ALL
SELECT 'Planets', COUNT(*) FROM Planets
UNION ALL
SELECT 'Moons', COUNT(*) FROM Moons
UNION ALL
SELECT 'Missions', COUNT(*) FROM Missions;

-- Identify null values in important columns
SELECT 'Planets' AS TableName, 'Name' AS ColumnName, COUNT(*) AS NullCount
FROM Planets WHERE Name IS NULL
UNION ALL
SELECT 'Planets', 'Diameter', COUNT(*) FROM Planets WHERE Diameter IS NULL
UNION ALL
SELECT 'Moons', 'Name', COUNT(*) FROM Moons WHERE Name IS NULL;

-- Count the number of planets in each star system that have a diameter greater than 10,000 km
SELECT StarSystemID,
       COUNT(CASE WHEN Diameter > 10000 THEN 1 END) AS LargePlanetsCount
FROM Planets
GROUP BY StarSystemID;

-- Calculate the number of missions launched each year
SELECT YEAR(LaunchDate) AS LaunchYear, COUNT(*) AS MissionsCount
FROM Missions
GROUP BY YEAR(LaunchDate)
ORDER BY LaunchYear;

-- Generate INSERT statements dynamically based on existing table data
SELECT CONCAT('INSERT INTO Planets (Name, StarSystemID, Diameter, Mass, OrbitalPeriod, Atmosphere) VALUES (',
              QUOTE(Name), ', ', StarSystemID, ', ', Diameter, ', ', Mass, ', ', OrbitalPeriod, ', ', QUOTE(Atmosphere), ');') AS InsertStatement
FROM Planets;

-- Find planets that are heavier than the average mass of planets in their star system
SELECT p1.Name AS PlanetName, p1.StarSystemID, p1.Mass
FROM Planets p1
WHERE p1.Mass > (
    SELECT AVG(p2.Mass)
    FROM Planets p2
    WHERE p2.StarSystemID = p1.StarSystemID
);

-- Rank planets by orbital period within each star system and calculate the average orbital period of the top 3 planets in each star system
WITH RankedPlanets AS (
    SELECT p.Name, p.StarSystemID, p.OrbitalPeriod,
           RANK() OVER (PARTITION BY p.StarSystemID ORDER BY p.OrbitalPeriod DESC) AS OrbitalPeriodRank
    FROM Planets p
)
SELECT StarSystemID, AVG(OrbitalPeriod) AS AvgTop3OrbitalPeriods
FROM RankedPlanets
WHERE OrbitalPeriodRank <= 3
GROUP BY StarSystemID;

-- Count the number of distinct atmospheres and the number of planets with each atmosphere
SELECT Atmosphere, COUNT(*) AS PlanetsCount
FROM Planets
GROUP BY Atmosphere;

-- Identify null values in the Missions table
SELECT 'Missions' AS TableName, 'LaunchDate' AS ColumnName, COUNT(*) AS NullCount
FROM Missions WHERE LaunchDate IS NULL
UNION ALL
SELECT 'Missions', 'MissionType', COUNT(*) FROM Missions WHERE MissionType IS NULL;

-- Conditional Aggregates Example
-- Calculate the total mass of planets in each star system, but only include planets with an orbital period less than 500 days
SELECT StarSystemID,
       SUM(CASE WHEN OrbitalPeriod < 500 THEN Mass ELSE 0 END) AS TotalMass
FROM Planets
GROUP BY StarSystemID;

-- Find the number of missions launched each month
SELECT YEAR(LaunchDate) AS LaunchYear, MONTH(LaunchDate) AS LaunchMonth, COUNT(*) AS MissionsCount
FROM Missions
GROUP BY YEAR(LaunchDate), MONTH(LaunchDate)
ORDER BY LaunchYear, LaunchMonth;

-- Generate UPDATE statements dynamically based on existing table data
SELECT CONCAT('UPDATE Planets SET Mass = ', Mass, ' WHERE PlanetID = ', PlanetID, ';') AS UpdateStatement
FROM Planets;

-- Calculate the average diameter of planets in each star system, and for each planet, calculate the difference from the average
WITH AvgDiameter AS (
    SELECT StarSystemID, AVG(Diameter) AS AvgDiameter
    FROM Planets
    GROUP BY StarSystemID
)
SELECT p.Name, p.StarSystemID, p.Diameter,
       ad.AvgDiameter,
       p.Diameter - ad.AvgDiameter AS DiameterDifference
FROM Planets p
JOIN AvgDiameter ad ON p.StarSystemID = ad.StarSystemID;

-- Assume we have a hierarchical table of star systems and their subsystems
WITH RECURSIVE StarSystemHierarchy AS (
    SELECT StarSystemID, Name, ParentStarSystemID, 1 AS Level
    FROM StarSystems
    WHERE ParentStarSystemID IS NULL
    UNION ALL
    SELECT ss.StarSystemID, ss.Name, ss.ParentStarSystemID, sh.Level + 1
    FROM StarSystems ss
    INNER JOIN StarSystemHierarchy sh ON ss.ParentStarSystemID = sh.StarSystemID
)
SELECT * FROM StarSystemHierarchy;

-- Correlated Subquery Example
-- Find moons that are larger than the average diameter of moons orbiting the same planet
SELECT m1.Name AS MoonName, m1.PlanetID, m1.Diameter
FROM Moons m1
WHERE m1.Diameter > (
    SELECT AVG(m2.Diameter)
    FROM Moons m2
    WHERE m2.PlanetID = m1.PlanetID
);

-- Combining CTEs and Window Functions Example
-- Calculate the cumulative sum of diameters for planets within each star system
WITH PlanetDiameters AS (
    SELECT p.Name, p.StarSystemID, p.Diameter,
           SUM(p.Diameter) OVER (PARTITION BY p.StarSystemID ORDER BY p.Diameter) AS CumulativeDiameter
    FROM Planets p
)
SELECT * FROM PlanetDiameters;

-- Data Exploration and Profiling Example
-- Identify columns with null values in the StarSystems table
SELECT 'StarSystems' AS TableName, 'Name' AS ColumnName, COUNT(*) AS NullCount
FROM StarSystems WHERE Name IS NULL
UNION ALL
SELECT 'StarSystems', 'StarType', COUNT(*) FROM StarSystems WHERE StarType IS NULL;

-- Conditional Aggregates Example
-- Count the number of moons for each planet that have an orbital period less than 10 days
SELECT PlanetID,
       COUNT(CASE WHEN OrbitalPeriod < 10 THEN 1 END) AS ShortOrbitalMoons
FROM Moons
GROUP BY PlanetID;

-- Temporal Data Analysis Example
-- Calculate the average diameter of planets launched each month
SELECT YEAR(LaunchDate) AS LaunchYear, MONTH(LaunchDate) AS LaunchMonth, AVG(p.Diameter) AS AvgDiameter
FROM Missions m
JOIN Planets p ON m.TargetPlanetID = p.PlanetID
GROUP BY YEAR(LaunchDate), MONTH(LaunchDate)
ORDER BY LaunchYear, LaunchMonth;

-- Dynamic SQL Generation Example
-- Generate INSERT statements for the StarSystems table dynamically based on existing table data
SELECT CONCAT('INSERT INTO StarSystems (Name, StarType, DistanceFromEarth) VALUES (',
              QUOTE(Name), ', ', QUOTE(StarType), ', ', DistanceFromEarth, ');') AS InsertStatement
FROM StarSystems;

-- Advanced Window Functions Example
-- Calculate the moving average of the diameter of planets within each star system
WITH MovingAverage AS (
    SELECT p.Name, p.StarSystemID, p.Diameter,
           AVG(p.Diameter) OVER (PARTITION BY p.StarSystemID ORDER BY p.Diameter ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS MovingAvgDiameter
    FROM Planets p
)
SELECT * FROM MovingAverage;

-- Recursive CTE Example
-- Find all descendant star systems of a given star system
WITH RECURSIVE DescendantStarSystems AS (
    SELECT StarSystemID, Name, ParentStarSystemID
    FROM StarSystems
    WHERE StarSystemID = 1 -- Change this to the ID of the star system you're interested in
    UNION ALL
    SELECT ss.StarSystemID, ss.Name, ss.ParentStarSystemID
    FROM StarSystems ss
    INNER JOIN DescendantStarSystems ds ON ss.ParentStarSystemID = ds.StarSystemID
)
SELECT * FROM DescendantStarSystems;
