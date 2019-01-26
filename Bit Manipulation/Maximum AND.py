'''
Given two numbers A and B. Find the value of pair (P,Q) such that A <= P < Q <= B value of P AND Q is maximum where AND 
is a binary operator. Refer to this link for more information about AND operator : http://en.wikipedia.org/wiki/Bitwise_operation#AND

Input:
First line of input contains number of test cases T. Each test case contains two numbers A and B.

Output: For each test case print the value of maximum AND.

*Constraints: * 
1<=T<=1000
1<= A < B <=1018

SAMPLE INPUT 
2
2 3
4 8


SAMPLE OUTPUT 
2
6
'''

'''t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    l=[]
    for j in range(a,b+1):
        for k in range(j+1,b+1):
            l.append(j&k)
    print(max(l))
import functools
import operator
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    l=[]
    for j in range(a,b+1):
        for k in range(j+1,b+1):
            l.append(functools.reduce(operator.and_, [j,k]))
    print(max(l))'''
for tt in range(int(input())):
 a,b = map(int,input().split())
 ans=0
 ans = b-1 if b&1 else b-2
 print(ans if ans>=a else a&b)
