'''
Our Prime Minister has some secret numbers, so as in any case of emergency he can use it to contact 
the Avengers to save him. But these numbers has some special features, they are prime and sum of each 
individual's digit is also prime.Like 23, it is prime number and sum of it's digits (2+3)= 5, is also a prime number.
For your information, Avengers are Earth's Mightiest Heroes , consisting of Iron Man, Captain America, Thor, Hulk and many more.
So your task is to print all the such numbers  in a given range, a,b (both included), in ascending order.
Save your PM.

Input:
Single line containing two space separated integers, a and b respectively.

Output:
All the integers between a to b (including a and b), that satisfy conditions mentioned in statement, separated by single space.

Constraints:
1<= a,b <=1000000

SAMPLE INPUT 
10 50

SAMPLE OUTPUT 
11 23 29 41 43 47

Explanation:
Here a=10, b=50.
All the numbers between these which satisfy the property explained in question are
11 23 29 41 43 47, in ascending order.
11 (1+1=2 is prime)
23 (2+3=5 is prime)
29 (2+9=11 is prime)
41 (4+1=5 is prime)
43 (4+3=7 is prime)
47 (4+7=11 is prime)
'''
# Write your code here
import math
def chk_prime(n):
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

def sum_digit(num):
    sum=0
    while num!=0:
        r=num%10
        sum+=r
        num=num//10
    return sum
    
a=input().split(" ")

start=int(a[0])
end=int(a[1])+1

cp=chk_prime
sd=sum_digit
for i in range(start,end):
    if cp(i):
        s=sd(i)
        if cp(s):
            print(i,end=" ")
