#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:01:46 2020

@author: student
"""
# FLAMES game

n1=input("Enter the name").lower().replace(" ","")
n2=input("Enter the name").lower().replace(" ","")
d1=list(set(n1)-set(n2))
d2=list(set(n2)-set(n1))  #removing matchning letters
c=d1+d2                   #concatination of two list
count=len(c)              #length of c

'''
here count =0 means two name are identically equal
so we no need to find flames for those names
'''

if count>0:
    list1=["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    '''
    here the while loop will iterate untill the length of list
    should be 1 bcz we have to get only one relationship b/w
    two members 
    ''' 
    while len(list1)>1:
        c=count%len(list1)
        i=c-1           # bcz index is starts from 0
        if i>=0:
            left=list1[:i]
            right=list1[i+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("relationship is",list1[0])
else:
    print("plz don't enter the same names")


