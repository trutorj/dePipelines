import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import numpy as np
import os 
import sys
import argparse

# Functions
# Grouping data 
def reportYear(variable, value):
    from data_cleaning import df_final as df
    #variable= "Year"
    #variable= "HaBurned"
    #value = 'sum'
    #value = 'count'
    # Burned area by year
    if (variable == 'Year' and value == 'sum') or (variable == 'HaBurned' and value == 'count'):
        raise ValueError("ValueError. That's not possible. See help.")
    elif (variable == 'Year' and value == 'count'):
        # Number of fires by year
        nfires_year = df.groupby(["Year"]).agg({'Year': ['count']})               
        nfires_year = nfires_year.reset_index()
        nfires_year.columns = ["_".join(x) for x in nfires_year.columns.ravel()]
        nfires_year = nfires_year.rename(columns ={'Year_':'Year','Year_count':'Count'})
        return nfires_year
    elif (variable == 'HaBurned' and value == 'sum'):
        #Burned area by year
        burned_year = df.groupby(["Year"]).agg({'HaBurned': ['sum']})               
        burned_year = burned_year.reset_index()
        burned_year.columns = ["_".join(x) for x in burned_year.columns.ravel()]
        burned_year = burned_year.rename(columns ={'Year_':'Year','HaBurned_sum':'Ha_burned'})
        return burned_year 

# Burn area by year
def burnedPlot():   
    plt.bar(burned_year.Year, burned_year.Ha_burned, color=('orangered'))
    plt.xticks(burned_year.Year)
    plt.ylabel('Hectares')
    plt.title("Total burned area (2013-2019)")
    return plt.show()

# Number of wildfires
def firesPlot():
    plt.plot(nfires_year.Year, nfires_year.Count, color=('red'))
    plt.xticks(nfires_year.Year)
    plt.ylabel('Number of fires')
    plt.title("Evolution of wildfires (2013-2019)")
    return plt.show()

# Setting up the parser
parser = argparse.ArgumentParser(
                                description = """
                                This is a program to automate the reports from California wilfires.
                                It calculates the number of fires and the total burned surface by year.
                                The results can be plotted.
                                """
                                )              

parser.add_argument("--variable", help = "The chosen variable for groupping the data by. It has to be either 'Year' or 'HaBurned'", type= str)
parser.add_argument("--value", help= "The aggregation operation. It has to be either 'sum' if varable is HaBurned or 'count' is variable is", type= str)
parser.add_argument("--print", help= "Choose True or False to print out the plots", type= bool, default= False)
args = parser.parse_args()
print(args)
if args.variable == 'HaBurned' and args.value == 'sum':
    burned_year = reportYear(args.variable, args.value)
    print(burned_year)
    if args.print == True:
        burnedPlot()
    
if args.variable == 'Year' and args.value == 'count':
    nfires_year = reportYear(args.variable, args.value)
    print(nfires_year)
    if args.print == True:
        firesPlot()






