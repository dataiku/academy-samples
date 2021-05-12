import pandas as pd

def imputeLocationAvg(df, col_name):
    try:
        return df[col_name].fillna(df[col_name + '_avg'])
    except KeyError:
        try:
            return df[col_name].fillna(df['mode_' + col_name])
        except KeyError:
            return df[col_name]