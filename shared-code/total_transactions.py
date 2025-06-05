import pandas as pd
import dataiku

def monthly_total_transactions(df, date_col='PurchaseDate', marketplace_col='MerchantURL', quantity_col='Quantity', price_col='UnitPrice'):
    """
    Groups transaction data by month and marketplace, and calculates total transaction value.

    :parameters:
    - df: pandas DataFrame containing the transaction data
    - date_col: name of the column with invoice dates
    - marketplace_col: name of the column with marketplace names
    - quantity_col: name of the column with number of units sold
    - price_col: name of the column with price per unit

    :return:
    - DataFrame with columns: ['month', 'marketplace', 'total_transaction_value']
    """
    # Ensure date column is datetime type
    try:
        df = df.copy()
        df[date_col] = pd.to_datetime(df[date_col])
    except:
        return "Error: No DateTime"

    # Ensure a numeric type for unit price
    if df[price_col].dtype == 'object' or pd.api.types.is_string_dtype(df[price_col]):
        # Convert to numeric (int or float)
        df[price_col] = df[price_col].str.replace(',', '.', regex=False)  # Replace commas with dots
        df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
    
    # Calculate transaction value
    df['transaction_value'] = df[quantity_col] * df[price_col]

    # Create a 'month' column (e.g., 2024-05)
    df['month'] = df[date_col].dt.to_period('M').dt.to_timestamp()

    # Group by month and marketplace, summing transaction values
    df_gby = (
        df.groupby(['month', marketplace_col])['transaction_value']
        .sum()
        .reset_index()
        .rename(columns={'transaction_value': 'total_transaction_value'})
    )

    return df_gby
