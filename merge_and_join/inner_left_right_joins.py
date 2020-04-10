# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script to demonstare different ways to read a file

Author: Jagadeesh P
Date Time: 10/04/2020 10:51:00 AM
"""

# Inner, Left, and right merge types

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

# let’s look at the sizes or shapes of our inputs and outputs to the merge command:

print("User_Usage dimensions: {}".format(user_usage.shape))
print("User_Device dimensions: {}".format(user_device.shape))
print("Result dimensions: {}".format(result.shape))

# =============================================================================
# Other Merge Types
# =============================================================================

# =============================================================================
# There are four different types of merges available in Pandas.
# 
# Inner Merge / Inner join – The default Pandas behaviour, only keep rows
#                            where the merge “on” value exists in both the
#                            left and right dataframes.
# Left Merge / Left outer join – (aka left merge or left join) Keep every
#                                row in the left dataframe. Where there are
#                                missing values of the “on” variable in the
#                                right dataframe, add empty / NaN values in
#                                the result.
# Right Merge / Right outer join – (aka right merge or right join) Keep
#                                  every row in the right dataframe. Where
#                                  there are missing values of the “on” variable
#                                  in the left column, add empty / NaN values in the result.
# Outer Merge / Full outer join – A full outer join returns all the rows from
#                                 the left dataframe, all the rows from the right
#                                 dataframe, and matches up rows where possible,
#                                 with NaNs elsewhere.
# =============================================================================

result = pd.merge(user_usage,
                 user_device[['use_id', 'platform', 'device']],
                 on='use_id', 
                 how='left')

result.head()

# =============================================================================
# Using merge indicator to track merges - _merge is the indictor column
# =============================================================================


result = pd.merge(user_usage,
                 user_device[['use_id', 'platform', 'device']],
                 on='use_id', 
                 how='outer', 
                 indicator=True)

result

# =============================================================================
# Calculating statistics based on device
# =============================================================================
users=result.groupby("platform").agg({"use_id": "count"});
users


