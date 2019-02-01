'''
Alice has recently found an array a containing N integers. As we all know Alice loves sorted array so, he wants to sort the array. To sort an array Alice can add 1 to any integer in the array in 1 move.

Alice wants to find minimum number of moves needed to sort this array. Remember that after sorting the array, all elements in it should be distinct.

INPUT FORMAT
First line of input contains a single integer N.
Second line of input contains N space separated inegers, elements of array a.

OUTPUT FORMAT
Output a single integer, denoting number of moves needed to sort the given array.

SAMPLE INPUT 
3
1 6 5
SAMPLE OUTPUT 
2
Explanation
In first move Alice will add 1 to third integer then, in second move Alice will do the same he did in 1st move.
'''

n=int(input())
a=[int(x) for x in input().split()]
cnt=0
for i in range(n-1):
    if a[i+1]<=a[i]:
        d=a[i]-a[i+1]
        cnt+=d+1
        a[i+1]+=d+1
print(cnt)
