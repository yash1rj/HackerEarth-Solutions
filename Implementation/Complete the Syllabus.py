'''
Ash is preparing for his End semester exams and there are total K topics which he has to cover so that he can perform well in it. 
He has decided that he will study the topics sequentially. So, he is going to start from "MONDAY". 
Ash has got a very tight schedule and for each day of the week he already knows how many topics 
will he be able to study on a particular day.

It is guaranteed that Ash will not skip any day and will follow the routine sincerely, 
Determine on which day of the week will he be able to complete all the topics. (1st day of week is assumed to be MONDAY).

INPUT:-

First line of each test file contains the number of test cases T, 
Each test case will contain a positive integer K followed by array A in the next line which 
has 7 integers denoting the number of topics which Ash will be able to cover on a particular day 
of week A[0] will be for MONDAY, A[1] will be for TUESDAY ,..., A[6] will be SUNDAY.

OUTPUT:-
For each test case print the day of week in capital letters on which he will complete his syllabus.

SAMPLE INPUT 
3
7
1 1 1 1 1 1 1
2
1 1 0 0 0 0 0
10
0 0 0 0 0 0 1

SAMPLE OUTPUT 
SUNDAY
TUESDAY
SUNDAY

Explanation
For the first test case its quiet evident that Ash will complete the syllabus on SUNDAY.
For the second on every MONDAY and TUESDAY he is going to complete one topic but there are only 2 of them , 
so he will complete it on TUESDAY.
For the last test case Ash is going to cover 1 topic on every SUNDAY so he will complete all the topics on SUNDAY.
'''
t=int(input())
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
for i in range(t):
    a=int(input())
    b=[int(x) for x in input().split()]
    #print(b)
    i=0
    sm=0
    while sm<a:
        sm+=b[i]
        i=(i+1)%7
    print(days[i-1])
