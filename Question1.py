# https://pandasdmx.readthedocs.io/en/v0.2.2dev/usage.html

import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
# Define the source

# Building blocks for the URL
entrypoint = 'https://sdw-wsrest.ecb.europa.eu/service/' # Using protocol 'https'
resource = 'data'           # The resource for data queries is always'data'
flowRef ='MIR'              # Dataflow describing the data that needs to be returned, exchange rates in this case
key = 'M.AT.B.A2C.A.C.A.2250.EUR.N'    # Defining the dimension values, explained below

# Define the parameters
parameters = {
    'startPeriod': '2010-01-01',  # Start date of the time series
    'endPeriod': '2018-10-01'     # End of the time series
}
# Construct the URL: https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.CHF.EUR.SP00.A
request_url = entrypoint + resource + '/'+ flowRef + '/' + key

# Make the HTTP request
response = requests.get(request_url, params=parameters)


response = requests.get(request_url, params=parameters, headers={'Accept': 'text/csv'})

df = pd.read_csv(io.StringIO(response.text))
df.info()
print(df.head())