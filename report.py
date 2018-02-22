#!/usr/bin/env python
import requests

try:
    # get the data and capture the response
    response = requests.get('http://ir.eia.gov/ngs/wngsr.json')

    # have to change the encoding :(
    response.encoding = 'utf-8-sig'

except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

# pull the json data
data = response.json()

# print the desired data
print( data['series'][0]['data'][0] )
