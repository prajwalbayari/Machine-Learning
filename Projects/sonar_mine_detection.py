# building a system in Python that can predict whether an object is either Rock or Mine
# with SONAR Data. For this use case, we are using Logistic Regression Model for our prediction.

#Importing the dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Data preprocessing
sonar_data=pd.read_csv(r"C:\Users\Prajwal\Desktop\Machine Learning\Datasets\CopyOfSonarData.csv") #Read csv file
# print(sonar_data.head()) #First 5 rows
# print(sonar_data.shape) #Number of rows and cols

#Statistics
# print(sonar_data.describe())

# print(sonar_data.iloc[:,-1].value_counts()) #M->mine R->rock

#Grup data by mine and rock
# print(sonar_data.groupby(sonar_data.columns[-1]).mean())

#Separating the data and labels
X=sonar_data.iloc[:,:-1]
Y=sonar_data.iloc[:,-1]
# print(X.shape,Y.shape)

#Training the data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)
# print(X_test.shape,X_train.shape,X.shape)
# print(Y_test.shape,Y_train.shape,Y.shape)

#Model training
model=LogisticRegression()

#Training the model with training data
model.fit(X_train,Y_train)

#Model evaluation

#Accuracy of the training data

X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)
print('Accuracy on training data is: ',training_data_accuracy)

#Accuracy of the testing data

X_test_prediction=model.predict(X_test)
testing_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print('Accuracy on testing data is: ',testing_data_accuracy)

#Making a predictive system

input_data=(0.0260,0.0363,0.0136,0.0272,0.0214,0.0338,0.0655,0.1400,0.1843,0.2354,0.2720,0.2442,0.1665,0.0336,0.1302,0.1708,0.2177,0.3175,0.3714,0.4552,0.5700,0.7397,0.8062,0.8837,0.9432,1.0000,0.9375,0.7603,0.7123,0.8358,0.7622,0.4567,0.1715,0.1549,0.1641,0.1869,0.2655,0.1713,0.0959,0.0768,0.0847,0.2076,0.2505,0.1862,0.1439,0.1470,0.0991,0.0041,0.0154,0.0116,0.0181,0.0146,0.0129,0.0047,0.0039,0.0061,0.0040,0.0036,0.0061,0.0115
)
#changing the input_data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#Reshape the numpy array as we are predicting for 1 instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
if(prediction[0]=='R'):
    print("Based on the prediction the object is a Rock")
else:
    print("Based on the prediction the object is a Mine")