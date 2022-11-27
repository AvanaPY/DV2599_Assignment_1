# Blekinge Institute of Technology
# Authors:
#   Emil Karlström & Samuel Jonsson
# Programme: DVAMI19h
# Course: DV2599
# Assignment 1

import pandas as pd

def classify(data : pd.DataFrame, H : pd.Series):
    classify_df = pd.DataFrame()
    classify_df["is_spam"] = data["is_spam"]
    classify_df["classified_as"] = classify_with_hypothesis(data, H)["class"]
    classify_df["correct"]       = classify_df["classified_as"] == classify_df["is_spam"]
    return classify_df

def classify_with_hypothesis(data : pd.DataFrame, H : pd.Series):
    classes = []
    for row in range(data.shape[0]):
        cl = 1
        for col in H.index:
            if H.loc[col] != data.iloc[row].loc[col]:
                cl = 0
                break
        classes.append(cl)

    return pd.DataFrame(classes, columns=["class"])