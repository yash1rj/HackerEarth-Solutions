'''
Monk A loves to complete all his tasks just before the deadlines for introducing unwanted thrill in his life. 
But, there is another Monk D who hates this habit of Monk A and thinks it's risky.

To test Monk A, Monk D provided him tasks for N days in the form of an array Array, where the elements 
of the array represent the number of tasks.

The number of tasks performed by Monk A on the ith day is the number of ones in the binary representation of Arrayi.

Monk A is fed up of Monk D, so to irritate him even more, he decides to print the tasks provided in non-decreasing 
order of the tasks performed by him on each day. Help him out!

Input:
The first line of input contains an integer T, where T is the number of test cases.
The first line of each test case contains N, where N is the number of days.
The second line of each test case contains Array array having N elements, where Arrayi represents the 
number of tasks provided by Monk D to Monk A on ith day.

Output:
Print all the tasks provided to Monk A in the non-decreasing order of number of tasks performed by him.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= Arrayi <= 1018

Note:
If two numbers have the same number of ones (set bits), print the one which came first in the input first, and then the other one, as in the input.

SAMPLE INPUT 
1
4
3 4 7 10
SAMPLE OUTPUT 
4 3 10 7
Explanation
In the sample input, T = 1 and N = 4, where N is the number of days.
Tasks provided to Monk A on first day is 3 and binary representation of 3 is { 11 }2, which contains 2 ones.
Tasks provided to Monk A on second day is 4 and binary representation of 4 is { 100 }2, which contains 1 ones.
Tasks provided to Monk A on third day is 7 and binary representation of 7 is { 111 }2, which contains 3 ones.
Tasks provided to Monk A on fourth day is 10 and binary representation of 10 is { 1010 }2, which contains 2 ones.
So the Output will be: 4 3 10 7
'''

t=int(input())
for i in range(t):
    n=int(input())
    a= [int(x) for x in input().split()]
    d=sorted(a, key= lambda x: str(bin(x)).count("1"))
    d=[str(x) for x in d]
    print(" ".join(d))
