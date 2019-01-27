'''
A number is known as special bit number if its binary representation contains atleast two consecutive 1's or set bits.
For example 7 with binary representation 111 is a special bit number. Similarly 3(11) is also a special bit number as it contains atleast two consecutive set bits or ones.

Now the problem is, You are given an Array of N integers and Q queries. Each query is defined by two integers L,R.
You have to output the count of special bit numbers in the range L to R .

Input

Contains integer N, no of Array elements and Q- Total Number of Queries.

Next line contains N integers A[i] defining Array elements.

Next lines Q contains Queries 

Output

Output Q  lines containing answer for the ith Query.

SAMPLE INPUT

5 3
3 5 1 12 7
1 3
2 3
1 5

SAMPLE OUTPUT

1
0
3

Explanation

In Query 1 range is [1,3] and there is only one number with consecutive set bits is ; So ans is .

In Query 2 range is [2,3] and there is no number is there with consecutive set bits. So ans is .

In Query 3 range is [1,5] and there are 3 numbers with consecutive bits set i.e , and .

'''
n,q=map(int,input().split(" "))
a=[int(x) for x in input().split(" ")]
for i in range(q):
    l,r=map(int,input().split())
    cnt=0
    for j in range(l-1,r):
        if "11" in bin(a[j])[2:]:
            cnt+=1
    print(cnt)
