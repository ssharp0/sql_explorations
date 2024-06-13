-- Create the database
CREATE DATABASE IF NOT EXISTS PlanetsDB;

-- Use the created database
USE PlanetsDB;

-- Create the Star Systems table
CREATE TABLE StarSystems (
    StarSystemID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    StarType VARCHAR(50),
    DistanceFromEarth DOUBLE
);

-- Create the Planets table
CREATE TABLE Planets (
    PlanetID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    StarSystemID INT,
    Diameter DOUBLE,
    Mass DOUBLE,
    OrbitalPeriod DOUBLE,
    Atmosphere VARCHAR(255),
    FOREIGN KEY (StarSystemID) REFERENCES StarSystems(StarSystemID)
);

-- Create the Moons table
CREATE TABLE Moons (
    MoonID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    PlanetID INT,
    Diameter DOUBLE,
    OrbitalPeriod DOUBLE,
    FOREIGN KEY (PlanetID) REFERENCES Planets(PlanetID)
);

-- Create the Missions table
CREATE TABLE Missions (
    MissionID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    LaunchDate DATE,
    TargetPlanetID INT,
    TargetMoonID INT,
    MissionType VARCHAR(100),
    FOREIGN KEY (TargetPlanetID) REFERENCES Planets(PlanetID),
    FOREIGN KEY (TargetMoonID) REFERENCES Moons(MoonID)
);
