# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:00:34 2019

@author: BharathPatwari
"""
#Functions
def add1(a,b): # colon is to terminator of the function 
    return a+b # Tab intendation is important

def CalculateEMI(ROI,Tenure,RBIRepo,Penalty):
    return ROI+Tenure+RBIRepo+Penalty

#Optonal Parametes : Default values of paramaeters
def add3(a,b,c=20,d=40):
    tmp=a+b+c
    return tmp+d

print(add1(10,20))

print(add3(1,2))



