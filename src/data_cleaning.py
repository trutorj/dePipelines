#!/usr/bin/env python
# coding: utf-8

#########################################################
#           Data cleaning and merging                   #
######################################################### 
# Imports
import pandas as pd
# Ampliar el número de columnas
pd.options.display.max_rows = 999
import numpy as np
import re

# Functions
# Evaluate the NA's
def evaluar_NA(data):
    # Pandas series denoting features and the sum of their null values
    null_sum = data.isna().sum()
    # Total
    total = null_sum.sort_values(ascending=False)
    # Percentage
    percent = ( ((null_sum / len(data.index))*100).round(2) ).sort_values(ascending=False) 
    # concatenate along the columns to create the complete dataframe
    df_NA = pd.concat([total, percent], axis=1, keys=['Number of NA', 'Percent NA'])   
    return df_NA

######################################
# Import the dataset
data = pd.read_csv('../input/California_Fire_Incidents.csv')
#print(data.shape)
#print(data.columns)

# Asses the NAs
evaluar_NA(data)

# Select the columns of interest
df = data[['AcresBurned', 'ArchiveYear', 'Counties', 'CountyIds', 'Extinguished', 'Fatalities', 
           'Latitude', 'Location','Longitude', 'MajorIncident', 'Name', 
           'Started', 'UniqueId']]


# Check and drop for duplicates in column of 'UniqueID'
df.drop_duplicates(subset ="UniqueId", keep = False, inplace = True) 
#print(df.shape)

# Asses the NAs again
evaluar_NA(df)

# Impute 0 to all NA's values in 'Fatalities column'
df.Fatalities = df.Fatalities.fillna(0)

# Create a column for burnt area in hectareas
df["HaBurned"] = (df["AcresBurned"]*0.404686).round(2)

# Rename "Archive Year column"
df = df.rename(columns = {"ArchiveYear": "Year"})

# Cast 'Counties' column as string
df["Counties"].astype("string")

# Import the Census table
from census import df_census

# Rename columns
df_census = df_census.rename(columns = {"CTYNAME":"Counties", "POP":"Population", "DENSITY": "Density"})
# Extract the word County from CTYNAME column to match with df_fires 
#table
df_census["Counties"] = df_census["Counties"].str.rstrip(' County')
# Convert columns to adequate types
df_census["Counties"].astype("string")
df_census["Population"].astype("int32")

# MERGING the two dataframes
# Check 'Counties' column  are comparables
#print(df.loc[1,["Counties"]]==df_census.loc[19,["Counties"]])

# Join both datasets by 'County' column
df_final = pd.merge(df, df_census, left_on='Counties', right_on='Counties')

df_final

