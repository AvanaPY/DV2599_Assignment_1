# Blekinge Institute of Technology
# Authors:
#   Emil Karlström & Samuel Jonsson
# Programme: DVAMI19h
# Course: DV2599
# Assignment 1

import pandas as pd
import numpy as np
import math

# Categorizes a column according to an array of numbers to be used as bins, and an array of labels 
def make_category(df : pd.DataFrame, col_name : str, new_df : pd.DataFrame, bins : list, labels : list):
    new_df[f'BINNED_{col_name}'] = pd.cut(df[col_name],
                                            bins=bins, labels=labels,
                                            right=False)

# Generates n^depth bins for an array of numbers by recursively 
# splitting the array at the median and doing so to the two subsequent subarrays
def generate_bins(lst : list, depth = 3, bins=None, start_index=None, end_index=None, insert_at=0):

    if bins is None:
        bins = []
    if start_index is None or end_index is None:
        start_index = 0
        end_index = len(lst) - 1
        
    if depth < 1:
        return bins, list(range(0,len(bins) - 1))
    
    median_index = math.floor((end_index + start_index) / 2)
    med = lst[median_index]
    generate_bins(lst, depth - 1, 
                    bins=bins, start_index=median_index, end_index=end_index, insert_at=insert_at)

    bins.insert(insert_at, med)
    return generate_bins(lst, depth - 1, bins=bins, start_index=start_index, end_index=median_index-1, insert_at=insert_at)

def discretizise():
    df = pd.read_csv("spambase.csv")
    new_df = pd.DataFrame()

    bin_df = pd.DataFrame()

    # I don't know if nas exist but if nas no exist, now they not exist guarantee
    df.fillna(0.0)

    # Discretizise the frequency columns
    columns = df.columns.to_list()[:-1]
    word_char_freq_cols = [s for s in columns if s.startswith(("word_freq", "char_freq"))]

    for column in word_char_freq_cols:
        sorted_column = sorted(df[column].unique())
        column_bins, labels = generate_bins(sorted_column, depth=3, bins=[0, max(sorted_column)+1], insert_at=1)

        bin_df[column] = [len(labels)]

        make_category(df, column, new_df, 
                    bins = column_bins,
                    labels = labels)

    # Discretizise the remaining columns

    sorted_capital_run = sorted(df["capital_run_length_average"].unique())
    bins, labels = generate_bins(sorted_capital_run, depth=3, bins=[0, max(sorted_capital_run)+1], insert_at=1)
    make_category(df, "capital_run_length_average", new_df, bins=bins, labels=labels)
    bin_df["capital_run_length_average"] = [len(labels)]

    sorted_capital_run = sorted(df["capital_run_length_longest"].unique())
    bins, labels = generate_bins(sorted_capital_run, depth=2, bins=[0, max(sorted_capital_run)+1], insert_at=1)
    make_category(df, "capital_run_length_longest", new_df, bins=bins, labels=labels)
    bin_df["capital_run_length_longest"] = [len(labels)]

    sorted_capital_run = sorted(df["capital_run_length_total"].unique())
    bins, labels = generate_bins(sorted_capital_run, depth=2, bins=[0, max(sorted_capital_run)+1], insert_at=1)
    make_category(df, "capital_run_length_total", new_df, bins=bins, labels=labels)
    bin_df["capital_run_length_total"] = [len(labels)]

    # Keep the category column
    category_column = df.columns.to_list()[-1]
    new_df["is_spam"] = df[category_column]

    return new_df, bin_df