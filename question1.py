# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 01:54:23 2016

@author: Ramanuja
"""
'''
Your task is to count the number of molecules in a cup of soda which contains distilled water, carbon dioxide, and glucose. You have a machine that counts the number of atoms of carbon, hydrogen, and oxygen in a given sample.

Input Format

The input consists of a single line with three space separated integers: c, h, and o

where

c is the count of carbon atoms

h is the count of hydrogen atoms

o is the count of oxygen atoms

Constraints

0 â‰¤ c, h, o < 1010

Output Format

If the number of atoms is consistent with a mixture containing only water, carbon dioxide, and glucose molecules, the output should consist of a single line containing three space separated integers: the number of water molecules, the number of carbon dioxide molecules, and the number of glucose molecules.

If the number of atoms is not consistent with a mixture containing only water, carbon dioxide, and glucose molecules, the output should consist of a line containing the word Error

Sample Input

10 0 20
Sample Output

0 10 0
Explanation

The input indicates that there are 10 carbon atoms and 20 oxygen atoms. The only way that this could occur would be if there were 0 water molecules, 10 carbon dioxide molecules, and 0 glucose molecules.

Note that there are additional sample inputs available if you click on the Run Code button.
'''
def myGauss(m):
    #eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    #now backsolve by substitution
    ans = []
    m.reverse() #makes it easier to backsolve
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                #substitute in all known coefficients
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                #the equation is now reduced to ax + b = c form
                #solve with (c - b) / a
                ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans
    
a = []#youjusthave to build linear equation of 3 variable and then pass it to gauss elimination method

print myGauss(a)
