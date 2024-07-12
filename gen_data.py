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


# input insert data
def get_insert_data(table_name):
    fields = input(f"Enter the fields for {table_name} (comma-separated): ").split(',')
    values = input(f"Enter the values for {table_name} (comma-separated): ").split(',')
    return fields, values


def create_insert_statement(table_name, fields, values):
    fields_str = ', '.join(fields)
    values_str = ', '.join([f"'{value}'" for value in values])
    insert_statement = f"INSERT INTO {table_name} ({fields_str}) VALUES ({values_str});"
    return insert_statement


def interactive_insert():
    table_name = input("Enter the table name for the insert operation: ")
    fields, values = get_insert_data(table_name)
    insert_statement = create_insert_statement(table_name, fields, values)
    print("\nSQL INSERT statement:")
    print(insert_statement)


# input update data
def get_update_data(table_name):
    set_clause = input(f"Enter the SET clause for {table_name} (field=value pairs, comma-separated): ").split(',')
    where_clause = input(f"Enter the WHERE clause for {table_name}: ")
    return set_clause, where_clause


def create_update_statement(table_name, set_clause, where_clause):
    set_str = ', '.join(set_clause)
    update_statement = f"UPDATE {table_name} SET {set_str} WHERE {where_clause};"
    return update_statement


def interactive_update():
    table_name = input("Enter the table name for the update operation: ")
    set_clause, where_clause = get_update_data(table_name)
    update_statement = create_update_statement(table_name, set_clause, where_clause)
    print("\nSQL UPDATE statement:")
    print(update_statement)


# input delete data
def get_delete_data(table_name):
    where_clause = input(f"Enter the WHERE clause for {table_name}: ")
    return where_clause


def create_delete_statement(table_name, where_clause):
    delete_statement = f"DELETE FROM {table_name} WHERE {where_clause};"
    return delete_statement


def interactive_delete():
    table_name = input("Enter the table name for the delete operation: ")
    where_clause = get_delete_data(table_name)
    delete_statement = create_delete_statement(table_name, where_clause)
    print("\nSQL DELETE statement:")
    print(delete_statement)


# batch insert
def batch_insert_from_csv(table_name, csv_file):
    df = pd.read_csv(csv_file)
    insert_statements = []
    for row in df.itertuples(index=False):
        fields = ', '.join(df.columns)
        values = ', '.join([f"'{str(val)}'" for val in row])
        insert_statement = f"INSERT INTO {table_name} ({fields}) VALUES ({values});"
        insert_statements.append(insert_statement)
    return insert_statements


def interactive_batch_insert():
    table_name = input("Enter the table name for the batch insert operation: ")
    csv_file = input("Enter the path to the CSV file: ")
    insert_statements = batch_insert_from_csv(table_name, csv_file)
    print("\nBatch SQL INSERT statements:")
    for stmt in insert_statements:
        print(stmt)


# print csv as table to terminal
def print_csv_as_table(csv_file):
    df = pd.read_csv(csv_file)
    print(df.to_string(index=False))


def interactive_print_csv():
    csv_file = input("Enter the path to the CSV file: ")
    print("\nCSV Data in Database Format:")
    print_csv_as_table(csv_file)


def generate_aggregate_queries():
    queries = {
        "Number of Planets in Each Star System": """
            SELECT StarSystemID, COUNT(*) AS NumberOfPlanets
            FROM Planets
            GROUP BY StarSystemID;
        """,
        "Total Diameter of All Moons": """
            SELECT SUM(Diameter) AS TotalMoonDiameter
            FROM Moons;
        """,
        "Average Mass of Planets in Each Star System": """
            SELECT StarSystemID, AVG(Mass) AS AveragePlanetMass
            FROM Planets
            GROUP BY StarSystemID;
        """,
        "Minimum and Maximum Orbital Period of Planets": """
            SELECT MIN(OrbitalPeriod) AS MinOrbitalPeriod, MAX(OrbitalPeriod) AS MaxOrbitalPeriod
            FROM Planets;
        """,
        "Number of Missions per Planet": """
            SELECT TargetPlanetID, COUNT(*) AS NumberOfMissions
            FROM Missions
            GROUP BY TargetPlanetID;
        """,
        "Total Distance of All Star Systems from Earth": """
            SELECT SUM(DistanceFromEarth) AS TotalDistance
            FROM StarSystems;
        """,
        "Average Distance of Star Systems from Earth": """
            SELECT AVG(DistanceFromEarth) AS AverageDistance
            FROM StarSystems;
        """
    }
    return queries

def print_aggregate_queries():
    queries = generate_aggregate_queries()
    for description, query in queries.items():
        print(f"\n{description}:\n{query}")

# Call the function to print the aggregate queries
print_aggregate_queries()

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Create Table")
        print("2. Insert Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Batch Insert from CSV")
        print("6. Print CSV as Table")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            interactive_table_creation_with_fk()
        elif choice == '2':
            interactive_insert()
        elif choice == '3':
            interactive_update()
        elif choice == '4':
            interactive_delete()
        elif choice == '5':
            interactive_batch_insert()
        elif choice == '6':
            interactive_print_csv()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
