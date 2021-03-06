'''
India is a cricket crazy nation. Chang also loves cricket and computations related to cricket. 
Chang has created a Cricket app.This app analyses the performance of a cricketer. 
If a cricketer under-performs, then a negative rating is awarded. 
If performance is good, then positive rating is awarded to the cricketer.
Chang wants to analyse the performance of a cricketer over a period of N matches. 
Chang wants to find consistency of a cricketer. So he wants to find out the maximum consistent sum 
of cricket rating of a batsman or a bowler only if his overall rating is positive over that period. Help chang in doing so.

Input

The first line contain number of matches "N" over which the analysis is to be done. 
The second line contains those ratings of a batsman/bowler in those N matches.

Output

Print a single integer ie. the maximum consistent sum of rating of the cricketer if it is positive otherwise output 0 (zero).

SAMPLE INPUT 
8
-1 -4  4 -2 0 1 4 -5
SAMPLE OUTPUT 
7
Explanation
here the maximum consistent and continuous sum of rating is 4+(-2)+0+1+4=7.

'''

def maxSubArraySum(a,size): 
      
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 

n=int(input())
a=[int(x) for x in input().split()]
print(maxSubArraySum(a,n))
