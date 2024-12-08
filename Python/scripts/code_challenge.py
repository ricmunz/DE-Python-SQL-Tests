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

API_URL = "https://data.pa.gov/resource/mcba-yywm.json"

# Function to fetch data from API into DataFrame with optional specified data types
def fetch_data_and_load_to_dataframe(endpoint_url, column_dtypes=None):
    """
    Sends a GET request to the API, retrieves raw data, and loads it into a DataFrame.
    Automatically converts columns with the 'Floating Timestamp' type (per the dataset documentation)
    to datetime64[D] (year, month, day) since time component in dataset is always '00:00:00.000'.

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
        
        # Convert the Floating Timestamp columns to datetime64[D] to reduce memory overhead
        for col in floating_timestamp_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col]).dt.date
                
        # Assign data types to other columns if provided
        if column_dtypes:
            df = df.astype(column_dtypes)

        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# Function to display DataFrame information and first few rows
def display_dataframe_info(df):
    """
    Displays basic information and the first few rows of the DataFrame.
    
    :param df: The DataFrame to display info for.
    """
    if df is not None:
        print("DataFrame Info:")
        print(df.info())
        print("\nFirst 5 rows:")
        print(df.head())


def main():

    # API endpoint URL defined at the top of file, under imports.
        
    # Fetch data from API and load into DataFrame (no optional dtypes specified)
    application_in = fetch_data_and_load_to_dataframe(API_URL)

    # Display DataFrame information
    display_dataframe_info(application_in)

if __name__ == '__main__':
    # Run the main function
    main()
    
    
    

# [x]• You will ingest the raw data into a structure (data type of your choosing) called “application_in”.

# []• Remove all rows from application_in that contain null values in ANY column and place them in a data structure (data type of your choosing) named “invalid_data”.

# []• Convert all state senate district (senate) entries in application_in to snake case.

# []• Create a new field in application_in, “yr_born”, that contains each voter’s year of birth (dateofbirth). The data type should be an integer. The yr_born field should appear immediately right of “dateofbirth”.

# []• How does applicant age (in years) and party designation (party) relate to overall vote by mail requests?

# []• What was the median latency from when each legislative district (legislative) issued their application and when the ballot was returned?

# []• What is the congressional district (congressional) that has the highest frequency of ballot requests?

# []• Create a visualization demonstrating the republican and democratic application counts in each county.



