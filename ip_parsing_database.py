# importing libaries
from operator import index
from urllib import response
import geoip2.database
import pandas as pd
from sqlalchemy import false
from dotenv import load_dotenv

# defining environment variables
load_dotenv()

test_ip = os.getenv('TEST_IP')

# testing whether csv file imported successfully
nodes = pd.read_csv ('nodes.csv')
print(nodes)

# finding the city location for a single node with that IP address
with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
    response = reader.city(test_ip)

    print(response.city.name)

# adding new variable to the dataframe ('city') and iterating over each node so that each gets a 'city' value. Doing the same for latitude and longitude
city = []
latitude = []
longitude = []

for value in nodes['Host']:
    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(value)
            city.append(response.city.name)
            latitude.append(response.location.latitude)
            longitude.append(response.location.longitude)
        except:
            pass

nodes['City'] = pd.Series(city)
nodes['Latitude'] = pd.Series(latitude)
nodes['Longitude'] = pd.Series(longitude)
print(nodes)

# exporting the dataframe as a csv file with nodes and respective cities
nodes.to_csv ('nodesf.csv', index = false)