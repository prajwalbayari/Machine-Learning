import seaborn as sns #Has some built in datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#total bill vs tip datasets
tips=sns.load_dataset('tips')
# print(tips.head())

#setting a default theme
sns.set_theme()

#Visulaize the data
# sns.relplot(data=tips, x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
# plt.show()

#iris dataset
iris=sns.load_dataset('iris')
# print(iris.head())

# sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)
# sns.scatterplot(x='sepal_length',y='petal_width',hue='species',data=iris)
# plt.show()

#Loading the titanic dataset
titanic=sns.load_dataset('titanic')

#Count plot
# sns.countplot(x='class',data=titanic) #Number of people based on class
# sns.countplot(x='survived',data=titanic) #Number of people whho survived
# plt.show()

#Bar chart
# sns.barplot(x='sex',y='survived',hue='class',data=titanic)
# plt.show()

from sklearn.datasets import fetch_california_housing

house_cal=fetch_california_housing()
house=pd.DataFrame(house_cal.data,columns=house_cal.feature_names)
house['PRICE']=house_cal.target

# print(house.head())

#Distribution plot
# sns.displot(house['PRICE'])
# plt.show()

#Correlation
cor=house.corr()
#Heat map
plt.figure(figsize=(10,10))
sns.heatmap(cor,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')
plt.show()