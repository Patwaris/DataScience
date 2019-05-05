# -*- coding: utf-8 -*-
"""
Created on Fri May  3 08:45:49 2019

@author: BharathPatwari
"""

#Strings
name1="Bharath Patwari"
name2='abc'

print(type(name1))
print(type(name2))

#modify string content
print(name1[1])
name1[0]='A' #'str' object does not support item assignment

name2=name1+'Hyd'
print(name2)

name1=name1.upper()
print(name1)

#replace
name1=name1.replace('BHARATH','Vivek')

name1=10
isinstance(name1,str)
isinstance(name1,int)