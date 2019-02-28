'''
You have a shortage of attendance in a certain class, unfortunately, 
the godfather of your department is handling that class, he has a habit of giving strange questions.

He wrote some numbers in the blackboard and then randomly erased some of 
the digits present in the numbers. You can assume star in place of the blank digits. 
If you are able to guess the square root of the number correctly, you will be given the 
requisite attendance necessary for attending the exam.

Note:

If there is more than one answer, choose the smallest.

Numbers on the blackboard are not preceded with 0.

Input Format:

Single input line will contain digit and * (star) denoting number on the blackboard.

Output Format:

Guessed number. (n)

And if there is no such number possible, print 0

Constraints:

1 <= n <= 100

SAMPLE INPUT 
1*1
SAMPLE OUTPUT 
11
Explanation
For the sample 1*1 the smallest possible square root of such a number is 11
'''

import math

def isPerfectSquare(x): 
  
    # Find floating point value of  
    # square root of x. 
    sr = math.sqrt(x) 
   
    # If square root is an integer 
    return ((sr - math.floor(sr)) == 0) 
  

n=list(input())
#print(n)
for i in range(len(n)):
    if n[i]=="*":
        for j in "0123456789":
            n[i]=j
            nn=int("".join(n))
            if isPerfectSquare(nn):
                print(math.ceil(nn**0.5))
                break
