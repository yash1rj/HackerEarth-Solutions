'''
Sarah was attending a Halloween party in an abandoned castle. Frightened by some paranormal occurrences at the castle she decided to leave early. As she approached the gate it suddenly locked shut and a message appeared. It stated that she had to find the sum of all numbers with two set bits up to a given number N in order to leave. Sarah is still frightened by the happenings at the castle and cannot think straight, help her solve this puzzle.

Input

First line contain number of test cases T

Each test case contains a single number N
Output

Print the sum of numbers (up to N) satisfying the condition. Output may be large so take modulo with 10^9+7

SAMPLE INPUT

1
5

SAMPLE OUTPUT

8

Explanation
Here the numbers up to 5 which have two set bits are 3 and 5

Therefore the answer is 3+5=8
'''

from sys import stdin, stdout
t=int(stdin.readline())
for i in range(t):
    n=int(stdin.readline())
    sm=0
    for j in range(1,n+1):
        if str(bin(j)).count("1")==2:
            sm=sm+j%1000000007
    stdout.write(str(sm) + '\n')
