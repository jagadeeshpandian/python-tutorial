# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script to demonstare different ways to read a file

Author: Jagadeesh P
Date Time: 10/04/2020 10:51:00 AM
"""

# Merging DataFrames

# =============================================================================
# “Merging” two datasets is the process of bringing two datasets together into one, and 
# aligning the rows from each based on common attributes or columns.
# =============================================================================

import pandas as pd
import os

#to change the working directory
os.chdir(r"C:\Users\prabu\Documents\python-tutorial\Source_Files")

#Read the CSV file
user_usage=pd.read_csv("user_usage.csv")
user_device=pd.read_csv("user_device.csv")

# =============================================================================
# Merging user_usage with user_devices
# Lets see how we can correctly add the “device” and “platform” 
# columns to the user_usage dataframe using the Pandas Merge command.
# =============================================================================

result = pd.merge(user_usage,
                 user_device[['use_id', 'platform', 'device']],
                 on='use_id')
result.head()