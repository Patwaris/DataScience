# -*- coding: utf-8 -*-
"""
Created on Mon May  6 07:56:28 2019

@author: Bharath Patwari
"""
import os
import io #for i/o operations
import pydot #if we need to use any external .exe file
import pandas as pd
from sklearn import tree #For Decision Tree

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#Read the train data file 
titanic_train=pd.read_csv("D:\Data Science\Bharath_Repo\DataScience\SampleData/train.csv")

titanic_train.shape
titanic_train.info()

titanic_train1=pd.get_dummies(titanic_train,columns=['Pclass','Sex','Embarked'])
titanic_train1.shape
titanic_train1.info()
titanic_train1.describe()

X_titanic_train=titanic_train[['Pclass','SibSp','Parch']]
Y_titanic_train=titanic_train['Survived'] #Y-axis

#Build the decision tree
dt=tree.DecisionTreeClassifier()
dt.fit(X_titanic_train,Y_titanic_train)

#visualize the decision tree
objSgtringIO=io.StringIO()
tree.export_graphviz(dt,out_file=objSgtringIO,feature_names=X_titanic_train.columns)

#Use out_file=objStrinIO to get vlaues()
file1=pydot.graph_from_dot_data(objSgtringIO.getvalue())[0]

os.chdir("D:\\Data Science\\Bharath_Repo\\DataScience\\SampleData\\")
os.getcwd()
file1.write_pdf("DecisionTree.pdf")


#Predict the outcome using decision tree
#Read the test data file
titanic_test=pd.read_csv("D:\Data Science\Bharath_Repo\DataScience\SampleData/test.csv")
titanic_test.shape

X_titanic_test=titanic_test[['Pclass','SibSp','Parch']]

#Use .predict method on Test data using the model which we 
titanic_test['Survived']=dt.predict(X_titanic_test)

#To change teh directory

os.chdir("D:\\Data Science\\Bharath_Repo\\DataScience\\SampleData\\")
os.getcwd()

titanic_test.to_csv("submission_Titanic.csv",columns=['PassengerId','Survived'])


