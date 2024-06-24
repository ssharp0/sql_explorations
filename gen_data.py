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


# Function to generate value for SQL INSERT
def check_value(val):
    is_str = isinstance(val, str)
    is_date = isinstance(val, datetime)
    is_str__or_date = True if (is_str or is_date) else False
    return is_str__or_date


# Function to generate SQL INSERT statements from DataFrame
def generate_insert_stmt(df, table_name):
    insert_statements = []
    for row in df.itertuples(index=False):
        values = ', '.join(
            [f"'{str(val)}'" if check_value(val) else str(val) for val in row])
        statement = f"INSERT INTO {table_name} VALUES ({values});"
        insert_statements.append(statement)
    return insert_statements


# Function to print insert statements
def print_stmts():
    # Generate and print INSERT statements
    print("\nINSERT Statements for StarSystems:")
    for stmt in generate_insert_stmt(star_systems.reset_index(), 'StarSystems'):
        print(stmt)

    print("\nINSERT Statements for Planets:")
    for stmt in generate_insert_stmt(planets.reset_index(), 'Planets'):
        print(stmt)

    print("\nINSERT Statements for Moons:")
    for stmt in generate_insert_stmt(moons.reset_index(), 'Moons'):
        print(stmt)

    print("\nINSERT Statements for Missions:")
    for stmt in generate_insert_stmt(missions.reset_index(), 'Missions'):
        print(stmt)


# print statements
print_stmts()


# Function to generate SQL INSERT statements from DataFrame
def gen_insert_stmts(df, table_name):
    insert_statements = []
    for row in df.itertuples(index=False):
        values = ', '.join(
            [f"'{str(val)}'" if check_value(val) else str(val) for val in row]
        )
        statement = f"INSERT INTO {table_name} VALUES ({values});"
        insert_statements.append(statement)
    return insert_statements


# Function to save SQL INSERT statements to a file
def save_statements_to_file(statements, file_name):
    with open(file_name, 'w') as file:
        for statement in statements:
            file.write(statement + '\n')


# Generate SQL INSERT statements
star_systems_stmts = gen_insert_stmts(star_systems.reset_index(), 'StarSystems')
planets_stmts = gen_insert_stmts(planets.reset_index(), 'Planets')
moons_stmts = gen_insert_stmts(moons.reset_index(), 'Moons')
missions_stmts = gen_insert_stmts(missions.reset_index(), 'Missions')

# Combine all statements
all_stmts = star_systems_stmts + planets_stmts + moons_stmts + missions_stmts

# Save to .sql file
save_statements_to_file(all_stmts, 'random_data.sql')


# Function to generate SELECT statements for a table
def generate_select_statement(table_name):
    return f"SELECT * FROM {table_name};"


# Function to print the SELECT statements for each table
def print_select_statements():
    tables = ['StarSystems', 'Planets', 'Moons', 'Missions']
    print("\n")
    for table in tables:
        select_statement = generate_select_statement(table)
        print(f"SELECT statement for {table}:\n{select_statement}\n")


# Call the function to print the SELECT statements
print_select_statements()


def get_table_name():
    table_name = input("Enter the table name: ")
    return table_name


def get_fields():
    fields = []
    while True:
        field_name = input("Enter the field name (or type 'done' to finish): ")
        if field_name.lower() == 'done':
            break
        field_type = input(f"Enter the data type for {field_name}: ")
        constraints = input(f"Enter any constraints for {field_name} (e.g., PRIMARY KEY, NOT NULL, UNIQUE) or press Enter to skip: ")
        fields.append((field_name, field_type, constraints))
    return fields


def create_table_statement(table_name, fields):
    field_definitions = ",\n    ".join([f"{name} {data_type} {constraints}".strip() for name, data_type, constraints in fields])
    create_statement = f"CREATE TABLE {table_name} (\n    {field_definitions}\n);"
    return create_statement


def interactive_table_creation():
    table_name = get_table_name()
    fields = get_fields()
    create_statement = create_table_statement(table_name, fields)
    print("\nSQL CREATE TABLE statement:")
    print(create_statement)
    save_to_file = input("Would you like to save this statement to a file? (yes/no): ").lower()
    if save_to_file == 'yes':
        file_name = input("Enter the file name (with .sql extension): ")
        with open(file_name, 'w') as file:
            file.write(create_statement)
        print(f"SQL statement saved to {file_name}")


def validate_data_type(data_type):
    valid_data_types = ['INT', 'VARCHAR', 'TEXT', 'DATE', 'BOOLEAN', 'FLOAT', 'DOUBLE']
    return data_type.upper() in valid_data_types


def get_fields_with_validation():
    fields = []
    while True:
        field_name = input("Enter the field name (or type 'done' to finish): ")
        if field_name.lower() == 'done':
            break
        while True:
            field_type = input(f"Enter the data type for {field_name}: ")
            if validate_data_type(field_type):
                break
            else:
                print("Invalid data type. Please enter a valid SQL data type.")
        constraints = input(f"Enter any constraints for {field_name} (e.g., PRIMARY KEY, NOT NULL, UNIQUE) or press Enter to skip: ")
        fields.append((field_name, field_type, constraints))
    return fields


def get_foreign_keys():
    foreign_keys = []
    while True:
        fk_field = input("Enter the field name for foreign key (or type 'done' to finish): ")
        if fk_field.lower() == 'done':
            break
        ref_table = input(f"Enter the referenced table for {fk_field}: ")
        ref_field = input(f"Enter the referenced field in {ref_table}: ")
        foreign_keys.append((fk_field, ref_table, ref_field))
    return foreign_keys


def create_table_statement_with_fk(table_name, fields, foreign_keys):
    field_definitions = ",\n    ".join([f"{name} {data_type} {constraints}".strip() for name, data_type, constraints in fields])
    fk_definitions = ",\n    ".join([f"FOREIGN KEY ({fk_field}) REFERENCES {ref_table}({ref_field})" for fk_field, ref_table, ref_field in foreign_keys])
    create_statement = f"CREATE TABLE {table_name} (\n    {field_definitions}"
    if fk_definitions:
        create_statement += f",\n    {fk_definitions}"
    create_statement += "\n);"
    return create_statement


def interactive_table_creation_with_fk():
    table_name = get_table_name()
    fields = get_fields_with_validation()
    foreign_keys = get_foreign_keys()
    create_statement = create_table_statement_with_fk(table_name, fields, foreign_keys)
    print("\nSQL CREATE TABLE statement:")
    print(create_statement)
    save_to_file = input("Would you like to save this statement to a file? (yes/no): ").lower()
    if save_to_file == 'yes':
        file_name = input("Enter the file name (with .sql extension): ")
        with open(file_name, 'w') as file:
            file.write(create_statement)
        print(f"SQL statement saved to {file_name}")


# Call the function to start the interactive table creation
interactive_table_creation_with_fk()