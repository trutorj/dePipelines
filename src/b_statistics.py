import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import numpy as np
import os, sys
from data_cleaning import df_final as df
##########################
# Burned area by county
burned_county = ((df.groupby(["Counties"]).agg({'HaBurned': ['sum']}))
                .sort_values([('HaBurned','sum')], ascending = False))
burned_county = burned_county.reset_index()
burned_county.columns = ["_".join(x) for x in burned_county.columns.ravel()]
burned_county = burned_county.rename(columns ={'Counties_':'County','HaBurned_sum':'Ha_burned'})
#burned_county.sort_values("County")

# Largest fire
max_county = ((df.groupby(["Counties"]).agg({'HaBurned': ['max']}))
                .sort_values([('HaBurned','max')], ascending = False))
max_county = max_county.reset_index()
max_county.columns = ["_".join(x) for x in max_county.columns.ravel()]
max_county = max_county.rename(columns ={'Counties_':'County','HaBurned_max':'Largest_fire(ha)'})
#max_county..sort_values("County")

# Smallest fire
small_county = ((df.groupby(["Counties"]).agg({'HaBurned': ['min']}))
                .sort_values([('HaBurned','min')], ascending = False))
small_county = small_county.reset_index()
small_county.columns = ["_".join(x) for x in small_county.columns.ravel()]
small_county = small_county.rename(columns ={'Counties_':'County','HaBurned_min':'Smallest_fire(ha)'})
#small_county.sort_values("County")


# Number of fires by county
n_county = ((df.groupby(["Counties"]).agg({'Counties': ['count']}))
                .sort_values([('Counties','count')], ascending = False))
n_county = n_county.reset_index()
n_county.columns = ["_".join(x) for x in n_county.columns.ravel()]
n_county = n_county.rename(columns ={'Counties_':'County','Counties_count':'Number_fires'})
#n_county.sort_values("County")

# Population
pop_county = df[["Counties","Population", "Density"]]
pop_county.drop_duplicates(subset ="Counties", keep = 'first', inplace = True) 
pop_county = pop_county.rename(columns = {"Counties": "County"})
#pop_county.sort_values("County")

# Merge
basic_st = pd.merge(burned_county, max_county, left_on='County', right_on='County')
basic_st = pd.merge(basic_st, small_county, left_on='County', right_on='County')
basic_st = pd.merge(basic_st, n_county, left_on='County', right_on='County')
basic_st = pd.merge(basic_st, pop_county, left_on='County', right_on='County')

# Drop a wrong index columb and order by County name
basic_st.sort_values("County")
basic_st

