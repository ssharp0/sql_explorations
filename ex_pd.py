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

print('-------ACCESSING ELEMENTS-------')
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
