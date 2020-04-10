# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script to demonstare different ways to read a file

Author: Jagadeesh P
Date Time: 10/04/2020 10:51:00 AM
"""

import pandas as pd
# Find out your current working directory

import os
print(os.getcwd())

# Out: /Users/shane/Documents/blog
# Display all of the files found in your current working directory

print(os.listdir(os.getcwd()))
# Out: ['test_delimted.ssv', 'CSV Blog.ipynb', 'test_data.csv']

#to change the working directory
os.chdir(r"C:\Users\prabu\Documents\python-tutorial\Source_Files")

print(os.listdir(os.getcwd()))


#Read the CSV file
df=pd.read_csv("user_usage.csv")
df


# When specifying file names to the read_csv function, you can supply both absolute or relative file paths.

# It’s recommended and preferred to use relative paths
# where possible in applications, because absolute paths are
# unlikely to work on different computers due to different directory structures.

os.getcwd()
# load the file using relative path
os.chdir("/Users/prabu/Documents/python-tutorial/Source_Files")
os.listdir(os.getcwd())
