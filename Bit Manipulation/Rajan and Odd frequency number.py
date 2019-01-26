'''
Given an array of numbers of size (2*n+1).Raja is unable to find the number which is present odd number of times.
It is guaranteed that only one such number exists.Can you help Raja in finding the number which is present odd number of times?

Input
First line contains value of n.
Second line contains (2*n+1) array elements. 
Output
Print the required number.

SAMPLE INPUT 
2
1 2 3 2 1
SAMPLE OUTPUT 
3
Explanation
For first input only 3 is the number which is present odd number of times.
'''
from collections import Counter
n=int(input())
a=[x for x in input().split(" ")]
d=dict(Counter(a))
for i in d:
    if d[i]%2!=0:
        print(i)
