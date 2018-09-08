import pandas as pd
import numpy as np

# Q.1  Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

a={'name':['ashish','rajat','naveen','raghav','manish'],'age':[20,22,24,21,25],
'mail_id':['ashish@gmail.com','rajat@gmail.com','naveen@hotmail.com','raghav@yahoo.com','manish@yahoo.com',],
'phone':[9990007994,9555487547,987584795,7845874587,7845874577]}
s=pd.Dataframe(a)
print(s)


# Q.2 - Download the dataset from this link , Import the data and print the following :

a=pd.read_csv('weather.csv')

# A. First 5 rows of Dataframe 
print(a.head(5))

# B. First 10 rows of the Dataframe 
print(a.head(10))

# C.find basic statistics on the particular dataset. 
print(a.describe(include="all"))

# D. Find the last 5 rows of the dataframe 
print(a.tail(5))

# E. Extract the 2nd column and find basic statistics on it.
x2 = a.iloc[:,[1]]
print(x2.describe())


# END 
