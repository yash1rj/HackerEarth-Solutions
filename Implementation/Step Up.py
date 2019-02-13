'''
After completing his studies Jugnu joined a software company. his office in a huge multi-storey building. 
today he is late for his office and there is no lift for going up.

Jugnu is tall, he has to step up in a building having N number of steps. The steps are numbered as 1 to N. 
he is at the Xth step and he has to reach Yth step.

He  don't like prime number so he is going to skip the prime steps.

You are going to find which steps having his footprint and count of footprint.

Coinstraints:  

1<=T<=20

10<=N<=1000

2<=X<Y<=1000

SAMPLE INPUT 
2
2 10
3 15
SAMPLE OUTPUT 
4
6
8
9
10
5
4
6
8
9
10
12
14
15
8
Explanation
Input:

First input is number of test case.

Second input is X and Y in a same line for first test case.

Third input is X and Y in a same line for second test case.

Output:

4, 6, 8, 9 and 10 is footprint and 5 is count of footprint of first test case.
4, 6, 8, 9, 10, 12, 14 and 15 is footprint and 8 is count of footprint of second test case.
'''

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

t=int(input())
for i in range(t):
    x,y=map(int,input().split(" "))
    cnt=0
    for j in range(x,y+1):
        if chk_prime(j)==False:
            print(j)
            cnt+=1
    print(cnt)
