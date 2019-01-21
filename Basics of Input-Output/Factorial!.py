'''
You have been given a positive integer N. You need to find and print the Factorial of this number. 
The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. 

Input Format:
The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

Output Format:
Output a single line denoting the factorial of the number N.
'''

# Write your code here
num=int(input())

def factorial(n):
    fact=1
    if(n==0 or n==1):
        return fact
    else:
        return n*factorial(n-1)
        
res=factorial(num)
print(res)
