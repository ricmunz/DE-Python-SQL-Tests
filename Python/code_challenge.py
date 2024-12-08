"""
Endpoint URL: https://data.pa.gov/resource/mcba-yywm.json

Endpoint Query Return Sample:
[
  {
    "countyname": "SCHUYLKILL",
    "party": "NOP",
    "dateofbirth": "1946-11-11T00:00:00.000",
    "mailapplicationtype": "MAILIN",
    "appissuedate": "2020-08-27T00:00:00.000",
    "appreturndate": "2020-08-27T00:00:00.000",
    "ballotsentdate": "2020-08-27T00:00:00.000",
    "ballotreturneddate": "2020-10-23T00:00:00.000",
    "legislative": "123RD LEGISLATIVE DISTRICT",
    "senate": "29TH SENATORIAL DISTRICT",
    "congressional": "9TH CONGRESSIONAL DISTRICT"
  },
  {
    "countyname": "DELAWARE",
    "party": "D",
    "dateofbirth": "2002-07-25T00:00:00.000",
    "mailapplicationtype": "OLMAILV",
    "appissuedate": "2020-09-01T00:00:00.000",
    "appreturndate": "2020-09-01T00:00:00.000",
    "ballotsentdate": "2020-10-03T00:00:00.000",
    "ballotreturneddate": "2020-10-21T00:00:00.000",
    "legislative": "161ST LEGISLATIVE DISTRICT",
    "senate": "26TH SENATORIAL DISTRICT",
    "congressional": "5TH CONGRESSIONAL DISTRICT"
  },
  ...
]
"""
import requests
import pandas as pd
from re import sub

API_URL = "https://data.pa.gov/resource/mcba-yywm.json"

# Function to fetch data from API into DataFrame with optional specified data types
def fetch_data_and_load_to_dataframe(endpoint_url, column_dtypes=None):
    """
    Sends a GET request to the API, retrieves raw data, and loads it into a DataFrame.
    Automatically converts columns with the 'Floating Timestamp' type (per the dataset documentation) to datetime.
    Some birth dates will show up as 1/1/1800 for confidentiality reasons. A flag is added to handle these
    differently during later analysis operations. 

    :param api_url: The URL of the API endpoint.
    :param column_dtypes: (optional) A dictionary specifying the desired data types for specific columns.
    :return: A Pandas DataFrame with the data, or None if the request fails.

    Note:
        Dataset documentation: https://data.pa.gov/Government-Efficiency-Citizen-Engagement/2020-General-Election-Mail-Ballot-Requests-Departm/mcba-yywm/about_data.
    """
    try:
        # Fetching data from API
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        
        # Load raw data directly into a DataFrame
        df = pd.DataFrame(response.json())
        
        # Columns of Floating Timestamp type in dataset documentation ("2014-10-13T00:00:00.000")
        floating_timestamp_columns = [
            'dateofbirth',
            'appissuedate',
            'appreturndate',
            'ballotsentdate',
            'ballotreturneddate'
        ]
        
        # Convert the Floating Timestamp columns to datetime
        for col in floating_timestamp_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])
        
        # Add confidentiality flag for birth dates set to 1/1/1800 (per dataset documentation)
        # to allow for exclusion from later correlation analysis
        if 'dateofbirth' in df.columns:
            df['is_confidential'] = df['dateofbirth'] == pd.to_datetime('1800-01-01')
            
        # Assign data types to other columns if provided
        if column_dtypes:
            df = df.astype(column_dtypes)

        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# Function to separate invalid data (rows with null values on ANY column) onto another DataFrame
def remove_and_separate_invalid_data(df):
    """
    This function removes rows with any null values from a DataFrame
    and stores them in a separate DataFrame called 'invalid_data'.
    
    :param df: The DataFrame to check and clean.
    :return: invalid_data_df, which contains rows with null values.
    """
    # Identify rows with null values in any column
    invalid_data = df[df.isnull().any(axis=1)]
    
    # Remove rows with null values from the original DataFrame
    df.dropna(inplace=True)

    return invalid_data

# Function to print the first 5 rows of DataFrame with a header 
def print_df_head(df):
    """
    Displays few rows of the DataFrame.
    
    :param df: The DataFrame to display.
    """
    if df is not None:
        print("First 5 rows:")
        print(df.head())


# Function to display DataFrame information and first few rows
def display_dataframe_info(df):
    """
    Displays basic information and the first few rows of the DataFrame.
    
    :param df: The DataFrame to display info for.
    """
    if df is not None:
        print("DataFrame Info:")
        print(df.info(), "\n")
        print_df_head(df)

# Simple function to print bold string to console.
def print_bold(text):
    """
    Prints the given text in bold in the console.

    param text: The string to be printed in bold.
    """
    # ANSI escape code for bold text
    BOLD_CODE = '\033[1m'
    ORANGE_CODE = '\033[38;5;214m'
    RESET_CODE = '\033[0m'
    
    # Print the bold text
    print(f"\n\n{BOLD_CODE}{ORANGE_CODE}{text}{RESET_CODE}")


# Converts a string to snake_case
def convert_str_to_snake_case(text):
    """
    Converts a string to snake_case.

    :param text: The string to be converted.
    :return: The string in snake_case.
    """
    return text.replace(' ', '_').lower()


# Applies convert_str_to_snake_case to all entries in a column
def convert_column_to_snake_case(df, column_name):
    """
    Converts all entries in the specified column to snake_case.
    Modifies DataFrame in place.
    Raises a ValueError if the specified column does not exist in the DataFrame. (Case sensitive)

    :param df: DataFrame with the specified column.
    :type df: pandas.DataFrame
    :param column_name: Name of the column to convert (case sensitive).
    :type column_name: str
    """
    # Validate column_name
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")
    
    # Convert entries using helper function convert_str_to_snake_case()
    df[column_name] = df[column_name].apply(convert_str_to_snake_case)
    
def add_column_year_of_birth(df):
    """
    Adds a 'yr_born' column with the year extracted from 'dateofbirth'.
    Modifies DataFrame in place.

    :param df: DataFrame with an existing 'dateofbirth' column.
    :type df: pandas.DataFrame
    """
    if 'dateofbirth' in df.columns:
        # Extract year from 'dateofbirth' and add 'yr_born' column
        df['yr_born'] = pd.to_datetime(df['dateofbirth']).dt.year
        df['yr_born'] = df['yr_born'].astype(int)
        
        # Reposition 'yr_born' next to 'dateofbirth'
        columns = df.columns.tolist()
        dateofbirth_index = columns.index('dateofbirth')
        columns.insert(dateofbirth_index + 1, columns.pop(columns.index('yr_born')))
        
        # Reorganize columns in place
        df.columns = columns



def main():

    # API endpoint URL defined at the top of file, under imports.
        
    # Fetch data from API and load into DataFrame (no optional dtypes specified)
    application_in = fetch_data_and_load_to_dataframe(API_URL)

    # Display original DataFrame information
    print_bold("application_in \t(Original)")
    display_dataframe_info(application_in)
    
    # Remove and separate all rows from application_in with null values on ANY column onto a new DataFrame 
    invalid_data = remove_and_separate_invalid_data(application_in)
    
    # Display the separate invalid_data DataFrame
    print_bold("invalid_data")
    display_dataframe_info(invalid_data)
    
    # Display modified Dataframe information
    print_bold("application_in \t(After dropping null values)")
    display_dataframe_info(application_in)
    
    # Convert senate column in application_in to snake case
    print_bold("application_in['senate'] \t(snake case)")
    convert_column_to_snake_case(application_in, 'senate')
    print(application_in['senate'].head()) # Only print senate column
    
    # Create 'yr_born'(int) column right next to 'dateofbirth'
    print_bold("application_in \t(Added 'yr_born' column)")
    display_dataframe_info(application_in)
    
    print_df_head(application_in)
    add_column_year_of_birth(application_in)
    print_df_head(application_in)    
    
    unique_values_count =  application_in['party'].nunique()
    print_bold("unique values:")
    print(unique_values_count)
    

if __name__ == '__main__':
    # Run the main function
    main()
    
    
    

# [x]• You will ingest the raw data into a structure (data type of your choosing) called “application_in”.

# [x]• Remove all rows from application_in that contain null values in ANY column and place them in a data structure (data type of your choosing) named “invalid_data”.

# [x]• Convert all state senate district (senate) entries in application_in to snake case.

# [x]• Create a new field in application_in, “yr_born”, that contains each voter’s year of birth (dateofbirth). The data type should be an integer. The yr_born field should appear immediately right of “dateofbirth”.

# []• How does applicant age (in years) and party designation (party) relate to overall vote by mail requests?

# []• What was the median latency from when each legislative district (legislative) issued their application and when the ballot was returned?

# []• What is the congressional district (congressional) that has the highest frequency of ballot requests?

# []• Create a visualization demonstrating the republican and democratic application counts in each county.



