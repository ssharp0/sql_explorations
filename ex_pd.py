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
