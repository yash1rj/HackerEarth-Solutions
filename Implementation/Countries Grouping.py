'''
People in the group, are sitting in a row numbered from 1 to N. Every person have been asked with a same question as

How many people of your country are there in the group?

The answers provided may be incorrect. It is known that people of same countries always sit together.

If all the given answers are correct, determine the number of distinct countries present otherwise print "Invalid Data".

Input

First line contains one integer, which denotes the number of test cases

Each test case consists of 2 lines:

The first line contains one integer N, which denotes the total number of people there in the group.

The second line contains N space-separated integers say Ai , which denotes the answer given by the ith person.

Output

For each test case output a single line containing a single integer denoting the distinct countries or "Invalid Data".

SAMPLE INPUT 
4
2
1 1
2
1 3
7
1 1 2 2 3 3 3
7
7 7 7 7 7 7 7
SAMPLE OUTPUT 
2
Invalid Data
4
1
Explanation
First test case, there are two people each from different country.

Second test case, there are only two people but the the second person claims as there are three people of his country.
'''

from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    d=dict(Counter(a))
    print(len(d))
