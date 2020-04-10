# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script to demonstare different ways to read a file

Author: Jagadeesh P
Date Time: 10/04/2020 10:51:00 AM
"""

import pandas as pd

# One complication in creating CSV files is if you have commas, semicolons, or tabs
# actually in one of the text fields that you want to store. In this case, it’s important to
# use a “quote character” in the CSV file to create these fields.

df=pd.read_csv("/Users/prabu/Documents/python-tutorial/Source_Files/user_device.csv" 
               , sep=',', quotechar='"' , encoding='utf8')
df