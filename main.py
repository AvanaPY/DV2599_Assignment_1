# Blekinge Institute of Technology
# Authors:
#   Emil Karlström & Samuel Jonsson
# Programme: DVAMI19h
# Course: DV2599
# Assignment 1

import pandas as pd
import numpy as np
from data import discretizise, training_validation_split
from hypothesis import hypothesis
from classify import classify

freq_depth = 2
capital_run_depth = 2

data_df, bins_df = discretizise(freq_depth=freq_depth, 
                                capital_run_depth=capital_run_depth)

# Split data into training and validation data
# This function also randomizes the rows
train_data, validation_data = training_validation_split(data_df, ratio=0.95);

H = hypothesis(train_data)

print(train_data)
print(validation_data)

validation_df = classify(validation_data, H)
validation_train_df = classify(data_df, H)

# Validation data metrics
v = pd.crosstab(validation_df["is_spam"], validation_df["classified_as"], rownames=["Actual"], colnames=["Predicted"])
print('Validation confusion matrix')
print(v)

# Full data metrics
v = pd.crosstab(validation_train_df["is_spam"], validation_train_df["classified_as"], rownames=["Actual"], colnames=["Predicted"])
print('Validation train confusion matrix')
print(v)