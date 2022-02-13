# importing libaries
import os
from urllib import response
import geoip2.webservice
import pandas as pd
from dotenv import load_dotenv

# defining environment variables
load_dotenv()

acc_number = os.getenv('MAXMIND_ACCOUNT_NUMBER')
api_key = os.getenv('MAXMIND_ACCOUNT_API_KEY')
test_ip = os.getenv('TEST_IP')

# testing whether csv file imported successfully
nodes_jan = pd.read_csv ('test_import.csv')
print(nodes_jan)

# finding the city location for a single node with that IP address
with geoip2.webservice.Client(acc_number, api_key, host='geolite.info') as client:
    response = client.city(test_ip)

    print(response.city)

# adding new variable to the dataframe ('city') and iterating over each node so that each gets a 'city' value
city = []
for value in nodes_jan['Host']:
    with geoip2.webservice.Client(acc_number, api_key, host='geolite.info') as client:
        response = client.city(value)

        city.append(response.city)

nodes_jan['City'] = city
print(nodes_jan)

# exporting the dataframe as a csv file with nodes and respective cities
nodes_jan.to_csv ('test_export.csv')