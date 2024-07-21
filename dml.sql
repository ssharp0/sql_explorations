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
