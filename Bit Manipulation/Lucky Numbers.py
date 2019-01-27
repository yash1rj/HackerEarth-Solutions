'''
Golu wants to find out the sum of Lucky numbers.Lucky numbers are those numbers which contain exactly two set bits.This task is very diffcult for him.So Help Golu to find sum of those numbers which exactly contain two set bits upto a given number N.

3 5 10 are lucky numbers where 7 14 are not.
INPUT
First line contain number of test cases T.Each test case contains a single number N.
OUTPUT
Print sum of all Lucky Numbers upto N.Output may be large so take modulo with 1000000007.

Constraints

1<=T<=105
1<=N<=1018

NOTE: Since value of test cases and n is really large, please use fast I/O optimization techniques.
SAMPLE INPUT

1
5

SAMPLE OUTPUT

8

'''
from sys import stdin, stdout
t=int(stdin.readline())
for i in range(t):
    n=int(stdin.readline())
    sm=0
    for j in range(1,n+1):
        if str(bin(j)).count("1")==2:
            sm=sm+j%1000000007
    stdout.write(str(sm) + '\n')
