'''
Once Rajmata is kidnapped by Bhallal Dev and Bahubali wants to free her but there is a problem. 
Rajmata is inside a room and to enter in the room ,Bahubali needs a secret code. 
There is a hint for the code and Bahubali is so frustrated that he can’t decode the hint so he asked you to help him.

Bhallal Dev gives Bahubali an array of size N and Q queries and for each queries he gives a range (Left to Right) to Bahubali.

As we know Bhallal Dev is a genious of mathematics so he defined a new keyword named AAUSATA .
To find AAUSATA Bahubali has to find mean value of array between the given range.

Input:

First line contains two integers N and Q denoting number of array elements and number of queries.

Next line contains N space separated integers denoting array elements.

Next Q lines contain two integers L and R(indices of the array).

Output:

print a single integer denoting the value of AAUSATA.

Constraints :

1<= N ,Q,L,R <= 10^6

1<= Array elements <= 10^9

NOTE:
Use Fast I/O.

SAMPLE INPUT 
5 3
1 2 3 4 5
1 3
2 4
2 5
SAMPLE OUTPUT 
2 
3
3
'''

from statistics import mean
#import numpy as np
n,q=map(int,input().split(" "))
a=[int(x) for x in input().split(" ")]
for i in range(q):
    l,r=map(int,input().split(" "))
    #cnt=r-l-1
    sm=a[l:r-1]
    print(int(mean(sm)))
    #print(int(np.mean(sm)))
    #print(int(sm/cnt))
