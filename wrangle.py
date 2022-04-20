# Import for data manipulation
import pandas as pd
import numpy as np

# Import to acquire df
import env
import os

# Create function to pull data
def get_superstore(use_cache=True):  
    '''
    This function receives a boolean as input to see if the user wants to 
    receive a fresh copy of the data from the database. Then it checks to 
    see if the file being requested already exists as a local .csv. It runs 
    a query for the data using the assigned url, creates a new .csv if needed, 
    then returns the superstore dataframe.
    ''' 
    # Check for previously saved version
    filename = 'ssdb.csv'
    if os.path.exists(filename) and use_cache:
        return pd.read_csv(filename)    
    # Notify user of db pull
    print('Acquiring df')   
    # Create URL to pull data
    url = env.get_db_url('superstore_db')    
    # Create SQL pull
    ssdb = pd.read_sql('''
    SELECT *
    FROM orders
    JOIN categories
    USING(`Category ID`)
    JOIN customers
    USING(`Customer ID`)
    JOIN products
    USING(`Product ID`)
    JOIN regions
    USING(`Region ID`)
    ''', url)    
    # Notify user that df is saving
    print('Saving CSV')   
    # Save file to csv
    ssdb.to_csv('ssdb.csv',index=False)   
    # Return df
    return ssdb

# Create function to prep df
def prep_superstore(df):
    '''
    This function takes in a dataframe and returns it with the following changes.
    '''
    # Change column names to all lowercase with _ instead of space
    df.columns = [col.lower().replace(' ','_') for col in df]

    # Drop redundant columns
    df = df.drop(columns=['region_id','product_id','category_id','customer_id'],)

    # Set date columns to datetime type
    df.order_date = pd.to_datetime(df.order_date)
    df.ship_date = pd.to_datetime(df.ship_date)

    # Set order date as index
    df = df.set_index('order_date').sort_index()

    # Create column for number of days to ship
    df['days_to_ship'] = df['ship_date'] - df.index
    
    # Set postal code to object type
    df.postal_code = df.postal_code.astype('object')

    # Return df
    return df