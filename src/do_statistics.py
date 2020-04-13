import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import numpy as np
import os, sys
from data_cleaning import df_final as df
##########################
# Functions
# Grouping data 
def reportYear(variable, value):
    # Depending on the variables, the calculation is different
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

# Burned area by year
# Print the plot for burned area by year
def burnedPlot(tablaBurned):   
    plt.bar(tablaBurned.Year, tablaBurned.Ha_burned, color=('orangered'))
    plt.xticks(tablaBurned.Year)
    plt.ylabel('Hectares')
    plt.title("Total burned area (2013-2019)")
    plt.savefig('../output/burnedArea.png')
    return plt.show()

# Number of wildfires
# Print the plot for number of wildfires per year
def firesPlot(tablaN):
    plt.plot(tablaN.Year, tablaN.Count, color=('red'))
    plt.xticks(tablaN.Year)
    plt.ylabel('Number of fires')
    plt.title("Evolution of wildfires (2013-2019)")
    plt.savefig('../output/nfires.png')
    return plt.show()

# Basic statistics per county
