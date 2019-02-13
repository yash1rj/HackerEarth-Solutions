'''
Where do odds begin, and where do they end? Where does hope emerge, and will they ever break?

Given an integer sequence a1, a2, ..., an of length n. 
Decide whether it is possible to divide it into an odd number of non-empty subsegments, 
the each of which has an odd length and begins and ends with odd numbers.

A subsegment is a contiguous slice of the whole sequence. For example, {3, 4, 5} and {1} are 
subsegments of sequence {1, 2, 3, 4, 5, 6}, while {1, 2, 4} and {7} are not.

INPUT:
The first line of input contains an integer T (1 ≤ T ≤ 10) , i.e. the number of test cases. 
The first line of each test case contains a non-negative integer n (1 ≤ n ≤ 100) — the length of the sequence.
The second line of each test case contains n space-separated non-negative integers a1, a2, ..., an (0 ≤ ai ≤ 100) — the 
elements of the sequence.

OUTPUT:
Output "Yes" if it's possible to fulfill the requirements, and "No" otherwise (without quotes) for each test case in a new line.

SAMPLE INPUT 
1
5
1 0 1 5 1
SAMPLE OUTPUT 
Yes
'''

for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    if n%2!=0:
        if a[0]%2!=0 and a[-1]%2!=0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
