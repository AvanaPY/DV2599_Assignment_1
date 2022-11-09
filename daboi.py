# Blekinge Institute of Technology
# Authors:
#   Emil Karlström & Samuel Jonsson
# Programme: DVAMI19h
# Course: DV2599
# Assignment 1

import pandas as pd

def daboi(D : pd.DataFrame):
    x = D.iloc[0]
    H = instance_to_hypothesis(x)
    
    for xi in range(1, min(D.shape[0], 50)): #TODO: Remove 50
        x = D.iloc[xi]
        if x.loc["is_spam"] != 0:
            H = LGG_Conj(H, x)

    H = H.drop(index=["is_spam"])
    return H
    
def LGG_Conj(H : pd.Series, x : pd.Series):
    for column in H.index:
        if H.loc[column] != x.loc[column]:
            H = H.drop(column)
    return H

def instance_to_hypothesis(x : pd.Series):
    return x