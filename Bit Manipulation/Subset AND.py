'''
You are given a number Z and a set S with N elements. Your job is to find a sub set of S such that the AND of the given number and this subset is zero. If this sub set is possible print "Yes" otherwise print "No"

Input
First line contains number of test case T. Each test case contains two lines , first line contains two numbers Z and N , where Z is given number and N is size of set S . Second line contains N elements of the subset S.

Output
For each test case print Yes if the subset is possible else print No .

Constraints:
1<=T<=100
1<=N<=1000
0<=Ai<=Z<=1000000
SAMPLE INPUT

3
10 2
2 0
10 3
1 1 1
5 3
1 5 3

SAMPLE OUTPUT
Yes
Yes
No
'''
t=int(input())
for i in range(t):
    z,n=map(int,input().split(" "))
    a=[int(x) for x in input().split()]
    for j in a:
        if j&z==0:
            print("Yes")
            break
    else:
        print("No")
