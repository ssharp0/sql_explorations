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


# Function to get random dates for missions
def generate_launch_dates():
    current_time = datetime.now()
    duration = timedelta(days=np.random.randint(0, 365 * 50))
    return current_time - duration


# Function to generate random missions
def generate_missions(n, planets, moons):
    names = [f'Mission_{i}' for i in range(n)]
    launch_dates = [generate_launch_dates() for _ in range(n)]
    target_planet_ids = np.random.choice(planets.index + 1, n)
    target_moon_ids = np.random.choice(moons.index + 1, n)
    mission_types = ['Lunar Landing', 'Mars Exploration', 'Asteroid Study']
    missions = pd.DataFrame({
        'Name': names,
        'LaunchDate': launch_dates,
        'TargetPlanetID': target_planet_ids,
        'TargetMoonID': target_moon_ids,
        'MissionType': np.random.choice(mission_types, n)
    })
    return missions


# Generate data
num_star_systems = 5
num_planets = 10
num_moons = 20
num_missions = 15

star_systems = generate_star_systems(num_star_systems)
planets = generate_planets(num_planets, star_systems)
moons = generate_moons(num_moons, planets)
missions = generate_missions(num_missions, planets, moons)

# Display the data
print("Star Systems:\n", star_systems)
print("\nPlanets:\n", planets)
print("\nMoons:\n", moons)
print("\nMissions:\n", missions)

# Visualize the data with Matplotlib
# Example: Histogram of planet diameters
plt.hist(planets['Diameter'], bins=10, alpha=0.75)
plt.title('Histogram of Planet Diameters')
plt.xlabel('Diameter')
plt.ylabel('Frequency')
plt.show()

# Example: Scatter plot of planet mass vs. diameter
plt.scatter(planets['Diameter'], planets['Mass'], alpha=0.75)
plt.title('Planet Mass vs. Diameter')
plt.xlabel('Diameter')
plt.ylabel('Mass')
plt.show()
