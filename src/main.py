import pandas as pd
# Don't show warnings
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import numpy as np
import os 
import sys
import argparse

from do_statistics import reportYear, burnedPlot, firesPlot

##################################################################
# Setting up the parser
parser = argparse.ArgumentParser(
                                description = """
                                This is a program to automate the reports from California wilfires.
                                It calculates the number of fires and the total burned surface by year.
                                The results can be plotted.
                                """)              

parser.add_argument("--variable", help = "The chosen variable for groupping the data by. It has to be either 'Year' or 'HaBurned'", type= str)
parser.add_argument("--value", help= "The aggregation operation. It has to be either 'sum' or 'count'", type= str)
parser.add_argument("--print", help= "Choose True or False to print out the plots", type= bool, default= False)
#####################################################################

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

