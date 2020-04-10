# Python Pandas read_csv

CSV (comma-separated value) files are a common file format for transferring and storing data. The ability to read, manipulate, and write data to and from CSV files using Python is a key skill to master for any data analyst.

# Load CSV files to Python Pandas

The basic process of loading data from a CSV file into a Pandas DataFrame (with all going well) is achieved using the “read_csv” function in Pandas:

# Load the Pandas libraries with alias 'pd'
import pandas as pd


# Read data from file 'filename.csv'
data = pd.read_csv("filename.csv")


# Preview the first 5 lines of the loaded data
data.head()






Source: [shanelynn](https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files)
