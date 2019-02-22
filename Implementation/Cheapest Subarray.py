'''
Visuals can be deceptive, and so can be the titles of the contest, but not every time you'll be asked tough 
questions in an EASY contest.

In this problem, you will be given an array of integers and you need to tell the cost of the cheapest possible 
subarray of length at least two.

A subarray is the sequence of consecutive elements of the array and the cost of a subarray is the sum of minimum and 
the maximum value in the subarray. 

Note: In an array of length n, there are (n)(n-1)/2 subarrays whose length is atleast 2.

Input Format:

The first line contains a single integer t  denoting the number of test cases.

The first line of each test case contains  n i.e the number of elements in the array. Next lines contains  n space-separated integers Ai

Output Format:

Print t lines each containing a single integer. ith integer denotes the cost of the cheapest subarray for the ith array.

SAMPLE INPUT 
2
2
3 2
3
3 4 2
SAMPLE OUTPUT 
5
6
Explanation
The only possible subarray of length atleast 2 is [3, 2], Its cost is minimum + maximum = 2 + 3 = 5;
Three subarrays of lengths at least 2 are possible i.e. [3, 4], [4, 2] and [3, 4, 2]. The minimum possible cost is
6 for the subarrays [4, 2] and [3, 4, 2]
'''


t=int(input())
for i in range(t):
    n=int(input())
    L=[int(x) for x in input().split(" ")]
    l=[]
    l.append([L[i:i+j] for i in range(0,len(L)) for j in range(2,len(L)-i+1)])
    #print(l)
    mnx=[]
    for k in l:
        for q in k:
            #print(q)
            mnx.append(min(q)+max(q))
    print(min(mnx))

    mini=50000
    for i in range(1,n):
        tot=arr[i]+arr[i-1]
        if(tot<mini): mini=tot
    print(mini)
