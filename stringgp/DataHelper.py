import pandas as pd
import numpy as np
import math

def getCSVData(filepath : str, *, header=None, delimiter : str = None, flip = False):
    if delimiter == " ":
        df = pd.read_csv(filepath, header=header, delim_whitespace=True)
    else:
        df = pd.read_csv(filepath, header=header, delimiter=delimiter)
    df = df.sample(frac=1)
    df = df.reset_index(drop=True)
    if flip:
        df = df[df.columns[::-1]]
    return df.to_numpy()

def separateRows(dataset, percentage : float):
    percentageAmount = math.ceil(len(dataset) * percentage)
    return (dataset[:percentageAmount], dataset[percentageAmount:])

def separateColumns(dataset, columnSplit):
    return (dataset[:, :columnSplit], dataset[:, columnSplit:])

def convertToOneHotEncoding(dataset, column, *labels):
    oneHotDataset = pd.DataFrame()
    for i, label in enumerate(labels):
        dataset.insert(column + i, label, [int(b) for b in (dataset.iloc[:, column + i] == label)])

    return dataset.drop(dataset.columns[[column + len(labels)]], axis=1)

def convertInputsToInt(dataset, column, *labels : list[str], offset : int = 0):
    rows = len(dataset)
    for i in range(rows):
        for j in range(column):
            input = dataset[i][j]
            dataset[i][j] = labels.index(input) + offset

    return dataset