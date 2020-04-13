import pandas as pd
# Don't show warnings
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import argparse
from b_statistics import basic_st
from do_statistics import reportYear, burnedPlot, firesPlot
from pdf_generator import create_pdf
##################################################################
def parse():
    parser = argparse.ArgumentParser(
                                    description = """
                                        This is a program to automate the reports from California wilfires.
                                        It calculates several basic statistics and data for each county. To acces this
                                        data, flag --county_stats.
                                        Besides, it groups the number of fires and the total burned surface by year
                                        for the period 2013-1019. 
                                        The results can be plotted and saved into a pdf.
                                     """)              

    parser.add_argument("--county_stats", default=False, action= "store_true", help = "Flag to print out the basic statistics by county")
    parser.add_argument("--variable", help = "The chosen variable for groupping the data by. It has to be either 'Year' or 'HaBurned'", type= str)
    parser.add_argument("--value", help= "The aggregation operation. It has to be either 'sum' or 'count'", type= str)
    parser.add_argument("--print", default=False, action="store_true", help= "Flag to print out the plots")
    parser.add_argument("--pdf", default=False, action= "store_true", help= "Flag to save a pdf with the report in the output folder")
    parser.parse_args()
    args = parser.parse_args()
    return args

def main():
    args = parse()
    if (args.county_stats == True):
        print(basic_st)

    if (args.variable == 'HaBurned') and (args.value == 'sum'):
        burned_year = reportYear(args.variable, args.value)
        print(burned_year)
        if args.print == True:
            burnedPlot(burned_year)
            #createPdF
    if args.variable == 'Year' and args.value == 'count':
        nfires_year = reportYear(args.variable, args.value)
        print(nfires_year)
        if args.print == True:
            firesPlot(nfires_year)
    if args.pdf == True:
        create_pdf(args.variable, args.value)
if __name__ == '__main__':
    main()
