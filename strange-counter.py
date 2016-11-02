'''
Question - https://www.hackerrank.com/challenges/strange-code
'''
#!/bin/python

import sys
number = int(raw_input().strip())
flag = True
n = 1
time = 0
time_ = []
while flag:
    if n ==1:
        time = 1
        time_.append(time)
    else:
        time = time + 3*(2)**(n-2)
        time_.append(time)
    temp = number - time
    if temp == 0:
        flag = False
        length = n
    elif temp < 0:
        flag = False
        length = n - 1
    else:
        pass
    #print n
    n = n + 1
X = number - time_[length-1]
print 3*(2)**(length-1) - X
    
    
