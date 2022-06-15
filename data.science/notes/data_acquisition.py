# Import requests library to perform HTTP requests
import requests

# Number of commuters
num_commuters = 'B08303_001E'

# Name of geographical level
geo_name = 'NAME'

# Type of geographical data
geo_level = 'state'

# Number of geographical data
amt = '*'

url = 'https://api.census.gov/data/2020/acs/acs5?get={name},{commuters}&for={level}:{amt}'.format(name=geo_name, commuters=num_commuters, level=geo_level, amt=amt)

# Make a GET request of the constructed URL
r = requests.get(url)

# Access data as JSON string
#r_text = r.text
#print(type(r_text))

# Access decoded JSON data as Python list
r_json = r.json()
#print(type(r_json))

# Import CSV library
import csv

''' Convert r_json to CSV, write each sublist as a comma-separated row of data to file.

1. Create a variable called 'file'. 
2. Use open() to open a file.
3. Open it with mode='w' for writing mode. 
4. The newline='' ensures that newlines are always interpreted correctly.
5. Use the writer() function from the csv library to make a writer object. 
6. Use the writerows() method to write each row of data into comma-separated format.
'''
with open('census.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(r_json)

# Import pandas
import pandas as pd

# Store the census CSV file into a pandas DataFrame
census_df = pd.read_csv('census.csv')

# Rename columns
census_df.columns = ['name', 'total_commutes', 'state_id']

# Print dataframe
print(census_df)