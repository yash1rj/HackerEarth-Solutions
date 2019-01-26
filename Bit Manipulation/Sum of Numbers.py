'''
Given an array of N elements, check if it is possible to obtain a sum of S, by choosing some (or none) elements 
of the array and adding them.

Input:
First line of the input contains number of test cases T. Each test case has three lines.
First line has N, the number of elements in array.
Second line contains N space separated integers denoting the elements of the array. 
Third line contains a single integer denoting S.

Output:
For each test case, print "YES" if S can be obtained by choosing some(or none) elements of the array and adding them. Otherwise Print "NO".

Note that 0 can always be obtained by choosing none.

Constraints
1 ≤ T ≤10
1 ≤ N ≤ 15
-10^6 ≤ A[i] ≤ 10^6 for 0 ≤ i < N

SAMPLE INPUT 
3
5
3 2 0 7 -1
8
3
-1 3 3
4
3
4 -5 1
5
SAMPLE OUTPUT 
YES
NO
YES
'''

from itertools import combinations
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split(" ")]
    #print(a)
    s=int(input())
    flg=0
    l=[]
    for j in range(1,n+1):
        l.append(list(combinations(a,j)))
    #print(l)
    for q in l:
        for w in q:
            if sum(w)==s:
                flg=1
                break
        if flg==1:
            break
    if flg==1:
        print("YES")
    else:
        print("NO")
