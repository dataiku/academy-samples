# Adding a comment

from random import random
from math import ceil

# Define function to bin column values.
def bin_values(revenue, v):
    if revenue >= v:
        val = 1
    elif revenue < v:
        val = 0
    else:
        val = revenue
    return val

def mock_drift(v, drift_threshold):
    if random() < drift_threshold:
        return ceil(v * 1.25)
    else:
        return v
