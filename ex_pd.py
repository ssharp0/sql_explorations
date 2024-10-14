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
  
