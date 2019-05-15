# -*- coding: utf-8 -*-
"""
Created on Mon May 14 07:56:28 2019

@author: Bharath Patwari
"""
#DecissionTree and Predict methods are very important in this example. This is the real starting/building of ML
#Here we will be playing with more columns. However DecisionTreeClassifier algorithm works only on numeric/continuous data/columns
#Henceforth we need to convert  catogerical columns to dummy columns
#This technique is called one-hot encoding

import pandas as pd
from sklearn import tree
from sklearn import model_selection
#import io
#import pydot #if we need to use any external .exe files.... Here we are using dot.exe
import os
#from sklearn import model_selection
os.chdir("D:/Data Science/Bharath_Repo/DataScience/SampleData/")


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#Read the train data file 
titanic_train=pd.read_csv("D:\Data Science\Bharath_Repo\DataScience\SampleData/train.csv")


#EDA
titanic_train.shape
titanic_train.info()

#Convert categoric to One hot encoding using get_dummies
titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.info()
titanic_train1.describe

#now the drop non numerical columns where we will not be applying logic. Something like we will not apply logic on names, passengerID ticket id etc...
X_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket','Survived'],1) 
y_train = titanic_train['Survived']

dt = tree.DecisionTreeClassifier()
#Build the decision tree model
param_grid = {'max_depth':[8, 10, 15], 'min_samples_split':[2, 4, 6], 'criterion':['gini', 'entropy']}


dt_grid=model_selection.GridSearchCV(dt,param_grid,cv=5,n_jobs=5) #n_jobs : Threading or no of cores
print(type(dt_grid))

dt_grid.fit(X_train,y_train)

dt_grid.cv_results_

dt_grid.best_score_
dt_grid.best_params_

#predict the outcome using decission tree
titanic_test = pd.read_csv("D:\Data Science\Bharath_Repo\DataScience\SampleData/test.csv")
#titanic_test.info() #Found that one row has Fare = null in test data. Instead of dropping this column, let's take the mean of it.
titanic_test.Fare[titanic_test['Fare'].isnull()] = titanic_test['Fare'].mean()

#Now apply same get_dummies and drop columns on test data as well like above we did for train data
titanic_test1 = pd.get_dummies(titanic_test, columns=['Pclass', 'Sex', 'Embarked'])
X_test = titanic_test1.drop(['PassengerId','Age','Cabin','Ticket', 'Name'], 1)
#Apply the model on Furture/test data
titanic_test1.info()
titanic_test['Survived'] = dt_grid.predict(X_test)
titanic_test.to_csv("Submission_Grid.csv", columns=['PassengerId', 'Survived'], index=False)