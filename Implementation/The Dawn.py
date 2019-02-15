'''
You are given a integer N denoting the multiplication of two numbers A and B. 
You have to find the minimum value of A+B for any integer A and B.

Constraints

1<=N<=10^13
Problem Setter - siddhant

SAMPLE INPUT 
24
SAMPLE OUTPUT 
10
Explanation
consider A = 6 and B = 4.
'''

n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
#print(l)
mn=[]
for j in range(n):
    for k in reversed(l):
        if j*k==n:
            mn.append(j+k)
print(min(mn))
