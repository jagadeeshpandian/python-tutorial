# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script to demonstare different ways to read a file

Author: Jagadeesh P
Date Time: 10/04/2020 10:51:00 AM
"""

# ==========================================================================================
# CSV files do not contain any type information for data.
# Data types are inferred through examination of the top rows of the file, 
# which can lead to errors. 
# ==========================================================================================

# ==========================================================================================
# To manually specify the data types for different columns, the dtype parameter 
# can be used with a dictionary of column names and data types to be applied,
# for example: dtype={"name": str, "age": np.int32}.
# ==========================================================================================

# ==========================================================================================
# Note that for dates and date times, the format, columns, and other behaviour can be 
# adjusted using parse_dates, date_parser, dayfirst, keep_date parameters.
# ==========================================================================================


# ==========================================================================================
# The nrows parameter specifies how many rows from the top of CSV file to read, which is 
# useful to take a sample of a large file without loading completely. Similarly the skiprows 
# parameter allows you to specify rows to leave out, either at the start of the file 
# (provide an int), or throughout the file (provide a list of row indices). Similarly, t
# he usecols parameter can be used to specify which columns in the data to load.
# ==========================================================================================

# ==========================================================================================
#  The na_values parameter allows you to customise the characters that are recognised 
#  as missing values.
# ==========================================================================================

import pandas as pd

# Advanced CSV loading example
data = pd.read_csv(
    "/Users/prabu/Documents/python-tutorial/Source_Files/employee.csv",     # relative python path to subdirectory
    sep=',',                                    # Tab-separated value file.
    quotechar='"',                              # single quote allowed as quote character
    dtype={"salary": float},                      # Parse the salary column as an integer 
    usecols=['name', 'birth_date', 'salary'],   # Only load the three columns specified.
    parse_dates=['birth_date'],                 # Intepret the birth_date column as a date
    na_values=['.', '??']                       # Take any '.' or '??' values as NA
)

print(data)
