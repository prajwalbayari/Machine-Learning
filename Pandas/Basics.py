import pandas as pd
from sklearn.datasets import fetch_california_housing   
import numpy as np

california_dataset=fetch_california_housing()
# print(type(california_dataset))
# print(california_dataset)

#Creating pandas dataframe
cal_df=pd.DataFrame(california_dataset.data,columns=california_dataset.feature_names)
# print(cal_df.head()) #First 5 values of the dataframe
# print(cal_df.shape) #Shape of dataframe

#Impoering form csv files
cars_df=pd.read_csv(r"C:\Users\Prajwal\Desktop\Machine Learning\Datasets\cars_sampled.csv")
# print(type(cars_df))
# print(cars_df.head())
# print(cars_df.shape)

#Exporting a dataframe to a csv file
# cal_df.to_csv("California.csv")

#Creating df with random values
# random_df=pd.DataFrame(np.random.randint(1,1000,(20,10)))
# print(random_df)

#Inspecting properties of dataframe

# print(cal_df.shape) #Number of rows and columns
# print(cal_df.head()) #First 5 rows
# print(cal_df.tail()) #Last 5 rows
# print(cal_df.info()) #Information about dataframe
# print(cal_df.isnull().sum()) #Number of missing values

# print(cars_df.value_counts('brand')) #Counting the number of unique values
# print(cal_df.groupby('HouseAge').mean()) #Listing based on mean values

#Statistical measures
# print(cal_df.count()) #Number of values in all rows
# print(cal_df.mean()) #Mean values column wise
# print(cal_df.std()) #Standard deviation column wise   
# print(cal_df.min()) #minimum in each column
# print(cal_df.max()) #maximum in each column

#All statistical at once
# print(cal_df.describe())

#Manipulating a dataframe
# cal_df["Try"]=0.1 #Adding a column to a dataframe
# print(cal_df.head())

# print(cal_df.head())
# cal_df.drop(index=0,axis=0) #Deleting a row
# cal_df.drop(columns="Longitude",axis=1) #Deleting a column
# print(cal_df.head())

#Locating a row using an index value
# print(cal_df.iloc[2])

#Locating a particular column
# print(cal_df.iloc[:,0]) #First column
# print(cal_df.iloc[:,-1]) #Last column

#Correlation
print(cal_df.corr())