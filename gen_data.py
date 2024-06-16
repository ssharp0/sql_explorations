import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Function to generate random star systems
def generate_star_systems(n):
    names = [f'StarSystem_{i}' for i in range(n)]
    star_types = [
        'G-Type Main-Sequence',
        'K-Type Main-Sequence',
        'M-Type Main-Sequence'
        ]
    distances = np.round(np.random.uniform(0.1, 100, n), 2)
    star_systems = pd.DataFrame({
        'Name': names,
        'StarType': np.random.choice(star_types, n),
        'DistanceFromEarth': distances
    })
    return star_systems


# Function to generate random planets
def generate_planets(n, star_systems):
    names = [f'Planet_{i}' for i in range(n)]
    star_system_ids = np.random.choice(star_systems.index + 1, n)
    diameters = np.round(np.random.uniform(3000, 150000, n), 2)
    masses = np.round(np.random.uniform(0.1, 100, n), 2)
    orbital_periods = np.round(np.random.uniform(1, 1000, n), 2)
    atmospheres = ['Nitrogen, Oxygen', 'Carbon Dioxide', 'Methane, Hydrogen']
    planets = pd.DataFrame({
        'Name': names,
        'StarSystemID': star_system_ids,
        'Diameter': diameters,
        'Mass': masses,
        'OrbitalPeriod': orbital_periods,
        'Atmosphere': np.random.choice(atmospheres, n)
    })
    return planets


# Function to generate random moons
def generate_moons(n, planets):
    names = [f'Moon_{i}' for i in range(n)]
    planet_ids = np.random.choice(planets.index + 1, n)
    diameters = np.round(np.random.uniform(100, 5000, n), 2)
    orbital_periods = np.round(np.random.uniform(1, 30, n), 2)
    moons = pd.DataFrame({
        'Name': names,
        'PlanetID': planet_ids,
        'Diameter': diameters,
        'OrbitalPeriod': orbital_periods
    })
    return moons
