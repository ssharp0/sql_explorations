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
