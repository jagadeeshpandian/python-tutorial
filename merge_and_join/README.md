# Merge and Join DataFrames with Pandas in Python

Merging and joining dataframes is a core process that any aspiring data analyst will need to master.


user_usage.csv – A first dataset containing users monthly mobile usage
                 statistics

user_device.csv – A second dataset containing details of an individual
                  “use” of the system, with dates and device information.

android_devices.csv – A third dataset with device and manufacturer data,
                      which lists all Android devices and their model code, obtained from Google here.

We can load these CSV files as Pandas DataFrames into pandas using the Pandas read_csv command, and examine the contents using the DataFrame head() command.

There are linking attributes between the sample datasets that are important to note – “use_id” is shared between the user_usage and user_device, and the “device” column of user_device and “Model” column of the devices dataset contain common codes.

# Sample problem              

We would like to determine if the usage patterns for users differ between different devices. For example, do users using Samsung devices use more call minutes than those using LG devices? This is a toy problem given the small sample size in these dataset, but is a perfect example of where merges are required.

We want to form a single dataframe with columns for user usage figures (calls per month, sms per month etc) and also columns with device information (model, manufacturer, etc). We will need to “merge” (or “join”) our sample datasets together into one single dataset for analysis.





Source: [shanelynn](https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/)        
