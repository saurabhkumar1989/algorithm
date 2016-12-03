# Time to solve 40 Min 

#https://www.hackerrank.com/challenges/find-digits


#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    counter = 0
    n = int(raw_input().strip())
    number = n
    while True:#convert int in to array
        if(n==0):
            break
        digit = n%10
        if(digit):#check digit should not be zero
           
            if((number%digit)==0):# even divide or not
                
                counter = counter + 1
        n = n//10
    print counter
    
