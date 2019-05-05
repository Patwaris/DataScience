# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:25:06 2019

@author: BharathPatwari
"""

import pandas as pd
print(pd.__version__)

titanic_train=pd.read_csv("E:\DataScience-GV\Bharath-Repo\DataScience\SampleData/train.csv")

print(type(titanic_train))

#Rows and columns
titanic_train.shape

#Datatypes an nullable information
titanic_train.info()

#Statistical data
titanic_train.describe()

#column size
pd.set_option('display.max_columns',30)

#Read specific columns
titanic_train['Sex']
titanic_train.Sex

temp=titanic_train[['Survived','Fare','Embarked']]
print(type(temp))

#Access rows of a dataframe
#i th record
titanic_train.iloc[855]

titanic_train[10:20]
titanic_train.iloc[855:891]

#top 10
titanic_train.head(10)
#last 10
titanic_train.tail(10)

#access portion of both rows and columns of dataframe
titanic_train.loc[10:21]
titanic_train.loc[10:20,('Name','Age')]
titanic_train.loc[10:20,('Name','Age','Sex')]

titanic_train.loc[titanic_train.Sex=='female','Sex']
titanic_train.loc[titanic_train.Fare<=7,'Fare']

#Grouping data in dataframe
titanic_train.groupby(['Pclass']).size()
titanic_train.groupby(['Pclass','Sex']).size()
titanic_train.groupby(['Embarked','Pclass']).size()







