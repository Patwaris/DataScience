# -*- coding: utf-8 -*-
"""
Created on Mon May  6 07:56:28 2019

@author: Bharath Patwari
"""

import pandas as pd
from sklearn import tree #For Decision Tree

#Read the train data file 
titanic_train=pd.read_csv("D:\Data Science\Bharath_Repo\DataScience\SampleData/train.csv")

titanic_train.shape
titanic_train.info()

X_titanic_train=titanic_train[['Pclass','SibSp','Parch']]
Y_titanic_train=titanic_train['Survived'] #Y-axis

#Build the decision tree
dt=tree.DecisionTreeClassifier()
dt.fit(X_titanic_train,Y_titanic_train)


#Predict the outcome using decision tree
#Read the test data file
titanic_test=pd.read_csv("D:\Data Science\Bharath_Repo\DataScience\SampleData/test.csv")
titanic_test.shape

X_titanic_test=titanic_test[['Pclass','SibSp','Parch']]

#Use .predict method on Test data using the model which we 
titanic_test['Survived']=dt.predict(X_titanic_test)

#To change teh directory
import os
os.chdir("D:\\Data Science\\Bharath_Repo\\DataScience\\SampleData\\")
os.getcwd()

titanic_test.to_csv("submission_Titanic.csv")


