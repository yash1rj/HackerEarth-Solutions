'''
You have to design a new model which maps an even length palindromic number to some digit between 0 to 9.
The number is mapped to a digit x on the basis of following criteria:
1. x should appear maximum number of times in the palindromic number, that is, among all digits in the number,  
x should appear maximum number of times.
2. If more than one digit appears maximum number of times, x should be the smallest digit among them.

Given an integer N, you have to find the digit x for the Nth even length palindromic number.

Note- First 9 even length palindromic numbers are:

            11, 22, 33, 44, 55, 66, 77, 88, 99

Input :

    First line contains T, number of test cases.

    Each of the next T lines contains an integer N.

Output:

    For each test case, print the digit to which the Nth even length palindromic number is mapped.
    Answer for each test case should come in a new line.

SAMPLE INPUT 
3
1
2
10
SAMPLE OUTPUT 
1
2
0

Explanation
For case 1:

    1st even length palidromic number is 11 , so answer is 1 as 1 appears most number of times in the number.
For case 2:
    2nd even length palidromic number is 22 , so answer is 2 as 2 appears most number of times in the number.
For case 3:
    10th even length palindromic number is 1001, here both 0 and 1 appears same number of times but 0<1 so answer is 0.
'''
from collections import Counter
t=int(input())
for i in range(t):
    n=input()
    res=n+n[::-1]
    #print(res)
    dc=dict(Counter(res))
    #print(dc)
    print(max(sorted(dc), key=dc.get))
    #print(max(dc.values()))
