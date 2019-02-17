'''
Killjee has recently read about superdromes. Superdromes are those numbers which are palindromic in both binary and decimal representation.

The number represented in binary representation will be up to its most significant bit which is 1.

For example, 2 will be represented as {10}, 6 will be represented as {110} and so on.

Now killjee ask you to find number of Superdromes less than or equal to n for given n.

INPUT FORMAT

First line of input contains a single integer q, denoting number of queries.
Next line contains q space separated integer, ith integer is n for ith query.

OUTPUT FORMAT

Output a single integer, number of Superdromes <=n  for each query. Print answer for each query in new line.

SAMPLE INPUT 
3
1 2 3 
SAMPLE OUTPUT 
1
1
2
Explanation
1 and 3 are superdromes while 2 is not a superdrome.
'''

q=int(input())
a=[int(x) for x in input().split()]
for i in a:
    cnt=0
    for j in range(1,i+1):
        x=str('{0:b}'.format(j))
        if x==x[::-1] and str(j)==str(j)[::-1]:
            cnt+=1
    print(cnt)
