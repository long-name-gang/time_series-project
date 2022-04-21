# Import for data manipulation
import pandas as pd
import numpy as np

# Import to acquire df
import env
import os

# Create function to pull data
def get_superstore(use_cache=True):  
    '''
    This functions recieves a boolean as input to see if the user wants to recieve a fresh copy from the database.
    Then the fucntion checks to see if the file being requested already exists.
    Runs a query for the data using the assigned url.
    Creates a new csv if needed.
    Then returns the superstore dataframe.
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

def split_percent_superstore(df):
    '''
    This function takes in a df and returns three samples of the data
    for train, validate and test.
    '''
    
    # The funciton assigns size as a portion of the df
    
    # The train set is 50 percent of the data
    train_size = int(len(df) * 0.5)
    
    # The validate set is 30 percent of the data
    validate_size = int(len(df) * 0.3)
    
    # Below the function assigns an end point for the validate data 
    # and a starting point for the test data
    validate_end_index = train_size + validate_size
    
    # Below the function assigns the data to individual subsets
    train = df[:train_size]
    validate = df[train_size:validate_end_index]
    test = df[validate_end_index:]

    # The function then returns the train, validate and test splits
    return train, validate, test

def split_year_superstore(df):
    '''
    This function takes in a. df and returns three samples of the data
    for train, validate and test.
    '''
    # The df is split by year with train being 2014 and 2015
    train = df[:'2015']
    # Validate is 2016
    validate = df['2016']
    # Test is 2017
    test = df['2017']
    # Return the split datasets
    return train, validate, test