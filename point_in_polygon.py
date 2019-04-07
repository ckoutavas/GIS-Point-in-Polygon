# Fusion table query for PIP

from pandas.io.json import json_normalize
import requests
import pandas as pd

# google fusion table api url
uri = 'https://www.googleapis.com/fusiontables/v2/query?'

# query uses sql with the param st_intersects which contains the coor for the polygon. Get info from kml file
query = {
         'sql': 'select * from 123456 where ST_INTERSECTS(col6, POLYGON(LATLNG(41.731162077,-87.9148656613999), LATLNG(41.7302177089,-87.9148307136999), . . . ))',
    'key': 'my_api_key',
        }


response = requests.post(uri, data=query)
print(response)

data = response.json()
df = json_normalize(data, 'rows')
df.columns = data['columns']
df['Boundary'] = 'boundary name'
print(f'df: {len(df.drop_duplicates())}\n')
