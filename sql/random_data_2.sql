DELIMITER $$

CREATE PROCEDURE GeneratePlanetaryData(IN num_star_systems INT)
BEGIN
    DECLARE star_system_counter INT DEFAULT 0;
    DECLARE planet_counter INT DEFAULT 0;
    DECLARE moon_counter INT DEFAULT 0;
    
    -- Insert star systems
    WHILE star_system_counter < num_star_systems DO
        INSERT INTO StarSystems (Name, StarType, DistanceFromEarth)
        VALUES (
            CONCAT('StarSystem_', FLOOR(RAND() * 9999)),
            CASE FLOOR(RAND() * 7)
                WHEN 0 THEN 'O'
                WHEN 1 THEN 'B'
                WHEN 2 THEN 'A'
                WHEN 3 THEN 'F'
                WHEN 4 THEN 'G'
                WHEN 5 THEN 'K'
                ELSE 'M'
            END,
            ROUND(RAND() * 1000, 2)
        );
        
        SET star_system_counter = star_system_counter + 1;
    END WHILE;
    
    -- For each star system, add planets
    SET planet_counter = 0;
    WHILE planet_counter < num_star_systems * 5 DO
        INSERT INTO Planets (
            Name,
            StarSystemID,
            Diameter,
            Mass,
            OrbitalPeriod,
            Atmosphere
        )
        VALUES (
            CONCAT('Planet_', FLOOR(RAND() * 9999)),
            FLOOR(RAND() * num_star_systems) + 1,
            ROUND(RAND() * 200000 + 3000, 2),
            ROUND(RAND() * 5000000000000 + 1000000000000, 2),
            ROUND(RAND() * 1000 + 1, 2),
            CASE FLOOR(RAND() * 5)
                WHEN 0 THEN 'Hydrogen/Helium'
                WHEN 1 THEN 'Carbon Dioxide'
                WHEN 2 THEN 'Nitrogen/Oxygen'
                WHEN 3 THEN 'Methane/Ammmonia'
                ELSE 'Vacuum'
            END
        );
        
        SET planet_counter = planet_counter + 1;
    END WHILE;
    
    -- Add moons to planets
    SET moon_counter = 0;
    WHILE moon_counter < num_star_systems * 10 DO
        INSERT INTO Moons (
            Name,
            PlanetID,
            Diameter,
            OrbitalPeriod
        )
        VALUES (
            CONCAT('Moon_', FLOOR(RAND() * 9999)),
            FLOOR(RAND() * (num_star_systems * 5)) + 1,
            ROUND(RAND() * 5000 + 1000, 2),
            ROUND(RAND() * 30 + 1, 2)
        );
        
        SET moon_counter = moon_counter + 1;
    END WHILE;
    
    -- Add missions
    INSERT INTO Missions (
        Name,
        LaunchDate,
        TargetPlanetID,
        TargetMoonID,
        MissionType
    )
    SELECT 
        CONCAT('Mission_', FLOOR(RAND() * 9999)),
        DATE_ADD(CURDATE(), INTERVAL FLOOR(RAND() * 365 * 10) DAY),
        FLOOR(RAND() * (num_star_systems * 5)) + 1,
        FLOOR(RAND() * (num_star_systems * 10)) + 1,
        CASE FLOOR(RAND() * 4)
            WHEN 0 THEN 'Exploration'
            WHEN 1 THEN 'Research'
            WHEN 2 THEN 'Resource Extraction'
            ELSE 'Colonization'
        END
    LIMIT num_star_systems * 2;
END$$

DELIMITER ;
