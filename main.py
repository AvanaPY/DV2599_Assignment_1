# Blekinge Institute of Technology
# Authors:
#   Emil Karlström & Samuel Jonsson
# Programme: DVAMI19h
# Course: DV2599
# Assignment 1

from discretify_data import discretizise
from daboi import daboi
from classify import classify_with_hypothesis
data_df, bins_df = discretizise()

is_spam = data_df["is_spam"]
no_class_df = data_df.drop(columns=["is_spam"])

H = daboi(data_df)
print(H)

data_df["classified_as"] = classify_with_hypothesis(no_class_df, H)["class"]
data_df["correct"] = data_df["classified_as"] == data_df["is_spam"]
vc = data_df["correct"].value_counts()
f = vc.loc[False]
t = vc.loc[True]

print(vc)
print(f'Accuracy: {t / (f + t) * 100:.2f}%')

print(data_df)