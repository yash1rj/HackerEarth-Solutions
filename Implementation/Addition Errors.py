'''
Bob is a noob mathematician and he is not very comfortable with addition of numbers.
He is unaware of the concept of carry that the addition of 2 numbers possess.
He everytime forgets to take a carry while performing addition.

Example: suppose he adds 5 and 8 so he writes only 3 instead of 13. Similarly while adding 18 and 223 he writes it as 231.
So basically he ignores the carry everytime.You task is to compute the error in his addition algorithm.
Error is defined as the absolute difference between Bob's answer and the actual answer which was expected.

Input Format
First line contains T (the number of Test Cases).
Each testcase contains 2 lines containing numbers A and B.(the numbers which Bob uses to perform an addition).

Output Format
For each testcase print the error value in a new line.

SAMPLE INPUT 
3
2
2
5
8
18
223
SAMPLE OUTPUT 
0
10
10
Explanation
Test Case 1:

Actual Answer = 2+2=4

Bob's Answer = 4

Error=0

Test Case 2:

Actual Answer = 5+8=13

Bob's Answer = 3

Error=10
'''
from itertools import zip_longest as zip
t=int(input())
for j in range(t):
    n1=int(input())
    n2=int(input())
    num1, num2, i, temp = n1, n2, 10, 0
    total = num1 + num2
    while num1 or num2:
        if (num1 % 10) + (num2 % 10) > 9: temp += i
        num1, num2, i = num1 // 10, num2 // 10, i * 10

    zres=total - temp
    #print(zres)
    ores=int(n1)+int(n2)
    #print(ores)
    print(abs(ores-zres))
