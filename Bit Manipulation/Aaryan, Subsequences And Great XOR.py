'''
Aaryan went to school like any usual day, The teacher asked his crush the following question. Given an array of numbers, First she had to compute the XOR of all the subsequences that can be formed. Suppose each subsequence had their following XOR value that came out after computing -> {P[0], P[1], P[2], and so on upto P[2^n-1] subsequences in an array of n numbers}

Now, the resultant answer is computed by taking bitwise inclusive OR of all P[i]'s

Since, Aaryan wants to impress his crush, He wants to compute the answer for this problem but since he is not so good at it, he turned to you for help.

Input:
First line will consist of number N.
Then in the next line, there will be N numbers, ith number in the line is denoted by A[i]

Output:
Output the required value as answer.

Constraints:
1 <= N <= 10^6
0 <= A[i] <= 10^9
SAMPLE INPUT

4
8 9 9 8

SAMPLE OUTPUT
9
'''

n=int(input())
a=[int(x) for x in input().split()]
r=0
for i in a:
    r=r|i
print(r)
