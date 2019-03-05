'''
You are given an array A of N integers and an integer M.

You simply have to find the maximum triplet sum which is divisible by M.

In other words  find three numbers a[ i ],a[ j ] and a[ k ] such that,

(a[ i ] + a[ j ] + a[ k ] )%M =0 and sum is maximum (i ,j , k are distinct and 1<=i,j,k<=N ).

INPUT

In the First line you are given an integer N and an integer M.

The next line contains N integers.

OUTPUT

Find the Maximum Triplet sum which is divisible by M.

If no such Triplet exists print -1.

SAMPLE INPUT 
4 3
2 3 1 5
SAMPLE OUTPUT 
9
Explanation
The maximum Triplet sum is obtained by 5+3+1=9
'''

from itertools import combinations
n,m=map(int,input().split(" "))
a=[int(x) for x in input().split()]
l=[]
sm=0
for i in list(combinations(a,3)):
    asm=sum(i)
    if asm>=sm and asm%m==0:
        l.append(asm)
        q=i
if len(l)==0:
    print("-1")
else:
    print(max(l))
