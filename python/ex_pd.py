import pandas as pd
import numpy as np


# generate dataframe from a dictionary of lists
def gen_df_from_dict_of_lists(data):
    df = pd.DataFrame(data)
    return df


# generate dataframe from a list of dictionaries
def gen_df_from_list_of_dicts(data):
    df = pd.DataFrame(data)
    return df


# generate dataframe from lists of lists (incl. np arrays)
def gen_df_from_lists_of_lists(data, cols):
    df = pd.DataFrame(data, columns=cols)
    return df


# dictionary of lists
d1 = {
    "Name": ["Bob", "Sam", "Joe", "April"],
    "Age": [32, 35, 31, 19],
    "Gender": ["M", "F", "M", "F"],
    "Height": [165, 130, 190, 160]
}

# list of dictionaries
d2 = [
    {"Name": "Bob", "Age": 32, "Gender": "M"},
    {"Name": "Sam", "Age": 35, "Gender": "F"},
    {"Name": "Joe", "Age": 31, "Gender": "M"},
]

# list of lists
d3 = [
    ["Bob", 32, "M"],
    ["Sam", 35, "F"],
    ["Joe", 31, "M"]
]
# cols for lists of lists
cols3 = ["Name", "Age", "Gender"]

# np array
d4 = np.array(d3)


print('\n')
print('--------DICT WITH LISTS---------')
df1 = gen_df_from_dict_of_lists(d1)
print(df1)
print(f'Index: {df1.index}')
print('--------------------------------')

print('\n')
print('---DICT WITH LISTS TRANSPOSED---')
print(df1.T)
print('--------------------------------')

print('\n')
print('-------LISTS WITH DICTS---------')
df2 = gen_df_from_list_of_dicts(d2)
print(df2)
print('--------------------------------')

print('\n')
print('---------LIST WITH LISTS--------')
df3 = gen_df_from_lists_of_lists(d3, cols3)
print(df3)
print('--------------------------------')

print('\n')
print('--------DF WITH NP ARRAY--------')
df4 = gen_df_from_lists_of_lists(d4, cols3)
print(df4)
print('--------------------------------')

print('\n-------ACCESSING ELEMENTS-------')
print(df1["Name"])
print('----')
print(df1[["Name", "Gender"]])
print('----')
print(df1.iloc[1, 1])
print('----')
print(df1.loc[:, ["Name", "Gender"]])
print('----')
print(df1.loc[1, ["Name"]])
print('----')
print(df1.loc[2, :])
print('----')
print(df1.columns)
print('----')
print(df1.describe())
print('----')
print(df1["Age"].describe())
print('----')
print(df1.sort_values(by="Age"))

print('\n-------LOOPING THROUGH DATA-------')

print('\n - Iterate By Column & Its Data')
for col in df1:
    print(f'col: {col}')
    print(f'vals:\n {df1[col]}\n')

print('\n - Iterrows')
for idx, row in df1.iterrows():
    print('\n', idx, row)

print('\n - Iterrows')
for row in df1.itertuples():
    print(df1.index, row.Name)

print('\n - Iterrows')
for row in df1.itertuples():
    print(row)

print('\n-------Using Apply-------')

print('\n - Double Age Values (w/ apply()')
df1_func1 = df1['Age'].apply(lambda x: x * 2)
print(df1_func1)

print('\n - Double Age Values + Height')
df1_func2 = df1['Age'].apply(lambda x: x * 2) + df1["Height"]
print(df1_func2)

print('\n - Grabbing a Value')
df1_func3 = df1['Age'][0]
print(df1_func3)

print('\n-------Setting a Value-------')

print('\n - Setting a value with "loc" (label)')
df1.loc[0, 'Age'] = 99
print(df1)

print('\n-------Filtering-------')

print('\n - Using A Condition (Age > 32)')
print(df1["Age"] > 32)

print('\n - Using A Condition  (Age > 32) - Another Way')
print(df1.loc[df1["Age"] > 32])

print('\n - Using Two Conditions (Age > 32 AND/& Height > 150)')
print(df1.loc[(df1["Age"] > 32) & (df1["Height"] > 150)])

print('\n - Using Two Conditions (Age > 36 OR/| Height > 170)')
print(df1.loc[(df1["Age"] > 36) | (df1["Height"] > 170)])

print('\n-------Create New Columns-------')

print('\n - Create A New Column (Age + Height)')
df1["Age + Height"] = df1["Age"] + df1["Height"]
print(df1)

print('\n - Create A New Column Based Off Condition (Age > 33, T/F)')
new_df = df1.copy()
new_df["Over 33"] = new_df["Age"] > 33
print(new_df)

print('\n - Create A New Column With Value Based Off Condition (Age > 33, T="Yes", F="No"')
new_df = df1.copy()
new_df = (new_df["Age"] > 33).map({True: 'Yes', False: 'No'})
print(new_df)

print('\n - Create Col With List Comprehension (Age > 33, T=1, F=0)')
new_df = df1.copy()
new_df["Over 33"] = [int(df1.loc[i, "Age"] > 33) for i in new_df.index]
print(new_df)

print('\n - Create Column Using A For Loop (Age > 33)')
# Create a new column using a for loop
new_df = df1.copy()
new_column = []
for index, row in new_df.iterrows():
    # print(f'i:{index} | row:{row}')
    if row['Age'] > 33:
        new_column.append('Older')
    else:
        new_column.append('Younger')
# Add the new column to the DataFrame
new_df['Age_Group'] = new_column
print(new_df)

print('\n-------Create Category with numpy select()-------')

print('\n - Create Category Col')
# Create a new column using multiple conditions
new_df = df1.copy()
new_df['Category'] = np.select([
    (new_df['Age'] > 60),
    (new_df['Height'] > 160),
    (new_df['Age'] > 30)
], ['Senior', 'Above Avg Height', 'Adult'], "Uknown")
print(new_df)

# age bin categories
df = pd.DataFrame(d1)
age_categories = pd.cut(df['Age'],
                        bins=[0, 18, 25, 35, 45, 55, 65],
                        labels=['< 18', '18-24', '25-34', '35-44', '45-54', '55+']
                        )
df['Age Category'] = age_categories
print(df)

# gender gounts
print('\n')
gender_counts = df['Gender'].value_counts(normalize=True) * 100
print(gender_counts)
male_ratio = df['Gender'].value_counts()['M'] / len(df)
female_ratio = df['Gender'].value_counts()['F'] / len(df)
print(f"\nMale ratio: {male_ratio:.2f}")
print(f"Female ratio: {female_ratio:.2f}")

print('\n-------Melt Dataframe-------')

print('\n')
melted_df = df.melt(id_vars=['Name'], var_name='Attribute', value_name='Value')
print(melted_df)

print('\n-------Group By-------')

print('\n')
grouped = df.groupby('Gender')
avg_age = grouped['Age'].mean()
print(avg_age)

print('\n-------Apply A Custom Function-------')


# custom function
def my_func(val):
    if val > 33:
        return 'Yes'
    else:
        return 'No'


# Apply the function to the 'Age' column
df1["Age > 33"] = df1['Age'].apply(my_func)
print(df1)


# custom function 2
def my_func2(row):
    # Get values
    name = row['Name']
    gender = row['Gender']
    # Convert Name to uppercase
    name_upper = name.upper()
    # Handle Gender condition
    if gender == 'F':
        gender_result = 'Female'
    else:
        gender_result = 'Male'
    # Return a dictionary with the transformed values
    return {
        'Name': name_upper,
        'Gender': gender_result,
        'Age': str(row['Age']),
    }


# Apply the function to the DataFrame
result_df = df1[['Name', 'Gender', 'Age']].apply(my_func2, axis=1)
print(result_df)
print(type(result_df))
print(type(df1))
# Combine the result with the original DataFrame
final_df = pd.concat([df1, result_df], axis=1)
print(final_df)


print('\n-------List Comprhension-------')
print('\n')
new_list = [x * 2 for x in range(5)]
print(new_list)
new_list = [x for x in range(5)]
print(new_list)
new_list = [x for x in new_list if x % 2 != 0]
print(new_list)


print('\n-------Working with Multi-Demensional Arrays-------')

# 1D array
print('\n')
new_list = [None] * 7
print(new_list)

# 1D array
one_d = [None] * 5
print("1D array:", one_d)
# Looping through 1D array
for item in one_d:
    print(item, end=" | ")
print("\n")
# Using enumerate for index access
for idx, item in enumerate(one_d):
    print(f"Index {idx}: {item}")
print('\n')

# 2D array
two_d = [[None] * 5 for _ in range(5)]
print("2D array:")
for row in two_d:
    print(row)
# Looping through 2D array
for i, row in enumerate(two_d):
    for j, item in enumerate(row):
        print(f"Row {i}, Column {j}: {item}")
print("\nUsing nested loops")
for i in range(5):
    for j in range(5):
        print(f"Row {i}, Column {j}: {two_d[i][j]}")
print('\n')

# 3D array
three_d = [[[None] * 3 for _ in range(3)] for _ in range(3)]
print("3D array:")
for slice_ in three_d:
    for row in slice_:
        print(row)
# Looping through 3D array
for i, slice_ in enumerate(three_d):
    for j, row in enumerate(slice_):
        for k, item in enumerate(row):
            print(f"Slice {i}, Row {j}, Column {k}: {item}")
print("\nUsing nested loops")
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(f"Slice {i}, Row {j}, Column {k}: {three_d[i][j][k]}")
