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
