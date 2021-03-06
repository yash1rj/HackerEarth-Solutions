'''
Roy and Alfi reside in two different cities, Roy in city A and Alfi in city B. Roy wishes to meet her in city B.

There are two trains available from city A to city B. Roy is on his way to station A (Railway station of city A). 
It will take T0 time (in minutes) for Roy to reach station A. The two trains departs in T1 and T2 minutes respectively. 
Average velocities (in km/hr) of trains are V1 and V2 respectively. We know the distance D (in km) between city A and city B. 
Roy wants to know the minimum time (in minutes) to reach city B, if he chooses train optimally.

If its not possible to reach city B, print "-1" instead (without quotes).

Note: If the minimum time is not integral, round the value to the least integer greater than minimum time.

Input:

First line will contain integer T, number of test cases.

Second line will contain integers **T0,T1,T2,V1,V2,D** (their meanings are mentioned in problem statement)

Output:

Print the integral result, minimum time (in minutes) to reach city B in a new line.

SAMPLE INPUT 
1
5 5 8 100 90 320
SAMPLE OUTPUT 
197
Explanation
Roy reaches station A in 5 minutes, First train departs in 5 minutes and second train departs in 8 minutes, 
he will be able to catch both of them. But he has to make an optimal choice, which train reaches city B in minimum time. 
For first train 320/100HRS= 192 minutes. Total time for first train, 5+192=197 minutes

For second train 320/90 =213.33336 minutes. Least integer greater than 213.33336 is 214. 
Total time for second train 214+8=222 minutes. So optimal choice is to take 
first train, and hence the minimum time is 197 minutes.
'''

import math
t=int(input())
for i in range(t):
    t0,t1,t2,v1,v2,d=map(int,input().split(" "))
    if t0>t1 and t0>t2:
        print("-1")
    else:
        d1=(d*60)/v1
        d2=(d*60)/v2
        if(t0>t1 and t0<=t2):
            res=d2+t2
        elif (t0>t2 and t0<=t1): 
            res=d1+t1
        elif (t0<=t1 and t0<=t2):
            res=min((t1+d1),(t2+d2));
        print(math.ceil(res))
