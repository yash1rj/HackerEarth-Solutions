'''
You are given an array a of size n consisting of integers. Now, you need to find the number of distinct integers x, 
such that there exists a sequence of distinct indices i1<i2<...<im,1≤m≤k   and  a[i1] or a[i2] or ... or a[im]=x 

Here or represents the bitwise OR operator.  

Input

First line of the each input will contain two space seperated integers n and k denoting the size of the array and maximum 
size of the subset, respectively.

Next line will contain n spaced integers denoting elements of the array.

Output

Output will consists of a single integer denoting the number of unique integers that can be formed by taking Bitwise OR  of every
subset of size less than or equal to k.

SAMPLE INPUT 
3 2
1 2 4
SAMPLE OUTPUT 
6
Explanation
Array is having 3 integers: 1, 2 and 4.
Subsets having size less than or equal to 2 is {{1},{2},{4},{1,2},{1,4},{2,4}}.
Bitwise OR of the subsets thus obtained is {1,2,4,3,5,6}.
Thus total unique intgers formed by taking bitwise OR of all subsets of size less than or equal to 2 is 6.
'''

from itertools import combinations
n,k=map(int,input().split())
a=[int(x) for x in input().split(" ")]
#print(a)
#nl=[]
sl=[]
for i in range(1,k+1):
    #nl.append(list(combinations(a,i)))
    #comb=combinations(a,i)
    #for j in list(comb):
    #    nl.append(j)
    #print(nl)
    for k in list(combinations(a,i)):
        sl.append(sum(k))
print(len(set(sl)))
