'''
Shubham is preparing for his End semester exams and there are total K topics which he has to cover so 
that he can perform well in it. He has decided that he will study the topics sequentially. So, he is going to start from "MONDAY".

Shubham has got a very tight schedule and for each day of the week he already knows how many 
topics will he be able to study on a particular day.

It is guaranteed that Shubham will not skip any day and will follow the routine sincerely, 
Determine on which day of the week will he be able to complete all the topics. (1st day of week is assumed to be MONDAY).

INPUT:-

First line of each test file contains the number of test cases T, Each test case will contain a 
positive integer K followed by array A in the next line which has 7 integers denoting the number 
of topics which Shubham will be able to cover on a particular day of week A[0] will be for MONDAY, 
A[1] will be for TUESDAY ,..., A[6] will be SUNDAY.

OUTPUT:-

For each test case print the day of week in capital letters on which he will complete his syllabus.

CONSTRAINTS:-

1<=T<=10^3
1<=K<=10^9
0<=A[i]<=10^9

Note : Solution will be available after end of test. Like our page Codeboom for solutions.

SAMPLE INPUT 
3
7
1 1 1 1 1 1 1
2
1 1 0 0 0 0 0
1
0 0 0 0 0 0 1
SAMPLE OUTPUT 
SUNDAY
TUESDAY
SUNDAY
'''

days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
for _ in range(int(input())):
  n=int(input())
  a=[int(x) for x in input().split()]
  i,sm=0,0
  while sm<n:
    sm+=a[i]
    i=(i+1)%7
  print(days[i-1])
