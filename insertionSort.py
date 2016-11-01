# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:53:41 2016

@author: Ramanuja
"""

a = [31, 41, 59, 26, 41, 58,45,0]

for index in range(1,len(a)):
     currentvalue = a[index]
     position = index

     while position>0 and a[position-1]>currentvalue:
         a[position]=a[position-1]
         position = position-1

     a[position]=currentvalue 
