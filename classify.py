import pandas as pd

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