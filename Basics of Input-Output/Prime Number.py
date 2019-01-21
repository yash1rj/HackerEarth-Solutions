"""
You are given an integer N. You need to print the series of all prime numbers till N.

Input Format

The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

Output Format

Print the desired output in single line separated by spaces.

Constraints

1<=N<=1000

SAMPLE INPUT 
9
SAMPLE OUTPUT 
2 3 5 7
"""

# Write your code here
def chk_prime(num):
    ctr=0
    for i in range(1,num+1):
        if(num%i==0):
            ctr+=1
    if(ctr==2):
        return True
    else:
        return False


rng=int(input())
for i in range(1,rng+1):
    if(chk_prime(i)==True):
        print(i, end=" ")
