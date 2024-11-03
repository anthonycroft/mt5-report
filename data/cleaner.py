import pandas as pd

def clean(data):
    # Locate the start positions of the three tables in the data
    positions_start = data[data.iloc[:, 0] == 'Positions'].index[0]
    orders_start = data[data.iloc[:, 0] == 'Orders'].index[0]
    deals_start = data[data.iloc[:, 0] == 'Deals'].index[0]

    
    # Extract tables and set the second row as the header
    positions = data.iloc[positions_start + 2 : orders_start, :]  # Skip header row by +2
    positions.columns = data.iloc[positions_start + 1]  # Set new header from the second row
    
    orders = data.iloc[orders_start + 2 : deals_start, :]
    orders.columns = data.iloc[orders_start + 1]
    
    deals = data.iloc[deals_start + 2 :, :]
    deals.columns = data.iloc[deals_start + 1]
    
    # drop columns with NaN headers
    positions = positions.loc[:, ~positions.columns.isna()]
    orders = orders.loc[:, ~orders.columns.isna()]
    deals = deals.loc[:, ~deals.columns.isna()]

    
    # delete rows in deals table where first column is NaN
    deals = deals.dropna(subset=[deals.columns[0]])

    
    # Regular expression pattern for timestamp format YYYY.MM.DD hh:mm:ss
    pattern = r"^\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}$"


    # Filter rows where the timestamp matches the expected format
    deals = deals[deals["Time"].str.match(pattern, na=False)]


    
    # Reset index if needed
    positions = positions.reset_index(drop=True)
    orders = orders.reset_index(drop=True)
    deals = deals.reset_index(drop=True)

    print('Positions:')
    print(positions)
    print('Orders:')
    print(orders)
    print('Deals:')
    print(deals)