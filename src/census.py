#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

#Import token and check it
mytoken = os.getenv("CENSUS")
print("VAMOOS AHÍ! tenemos APIKEY") if mytoken else print("Mal asunto, no la vemos")

# Function to get population and population density
# from the census for all California counties and to serve it
# as pandas dataframe.
def getFromCENSUS():    
    # Construct the resource url
    url='https://api.census.gov/data/2014/pep/cty?get=STNAME,CTYNAME,POP,DENSITY&for=county:*&in=state:06&DATE_=7&key='+mytoken
    # Perform the request
    res = requests.get(url)
    print(res.status_code, res.url)
    
    # Extract json from body response
    df = pd.DataFrame.from_dict(res.json())
    # Select only the needed columns and add header
    df = df[[1,2,3]]
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])
    return df

df_census = getFromCENSUS()
