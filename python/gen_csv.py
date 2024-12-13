import pandas as pd
import random
from datetime import datetime, timedelta


# Load the Excel file and display the content to the user
def load_excel_file(file_path):
    df = pd.read_excel(file_path)
    print("Excel File Content:")
    print(df)
    return df


# Parse the Excel file to extract necessary information
def parse_excel_file(df):
    fields = df.iloc[0, 1:].values
    include = df.iloc[1, 1:].values
    range_required = df.iloc[2, 1:].values
    values = df.iloc[3, 1:].values
    return fields, include, range_required, values


# Generate Randomized Data
def generate_random_data(fields, include, range_required, values, num_rows=1000):
    data = []
    for _ in range(num_rows):
        row = []
        for i, field in enumerate(fields):
            if include[i] == 'Y':
                if range_required[i] == 'Y':
                    if field == 'Date':
                        min_date, max_date = values[i].split('-')
                        start_date = datetime.strptime(min_date.strip(), "%m/%d/%Y")
                        end_date = datetime.strptime(max_date.strip(), "%m/%d/%Y")
                        delta = end_date - start_date
                        random_days = random.randint(0, delta.days)
                        random_value = start_date + timedelta(days=random_days)
                    else:
                        min_value, max_value = map(int, values[i].split('-'))
                        random_value = random.randint(min_value, max_value)
                else:
                    options = [option.strip() for option in values[i].split(',')]
                    random_value = random.choice(options)
                row.append(random_value)
            else:
                row.append(None)
        data.append(row)

    return pd.DataFrame(data, columns=[field for i, field in enumerate(fields) if include[i] == 'Y'])


# Save to CSV
def save_to_csv(data, output_file):
    data.to_csv(output_file, index=False)
    print(f"Randomized data saved to {output_file}")


# Main function to run the script
def main():
    file_path = "./example_store_data.xlsx"  # Replace with your Excel file path
    output_file = "./randomized_data.csv"

    # Load and display the Excel file content
    df = load_excel_file(file_path)

    # Parse the Excel file
    fields, include, range_required, values = parse_excel_file(df)

    # Generate Randomized Data
    data = generate_random_data(fields, include, range_required, values)

    # Save to CSV
    save_to_csv(data, output_file)


if __name__ == "__main__":
    main()
