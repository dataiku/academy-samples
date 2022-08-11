# Define function to bin column values.
def bin_values(revenue, v):
    if revenue >= v:
        val = 1
    elif revenue < v:
        val = 0
    else:
        val = revenue
    return val
