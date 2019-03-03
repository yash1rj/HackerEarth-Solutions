'''
Monk was having a great time in the Digital World, and was surprised to see a new game called,
"Conversion Game". In this game, two arrays of N integers A1,A2,...,An and B1,B2,...,Bn are playing against each other 
and Array A wants to convert itself in Array B.

Array A can do two types of operations on itslef: 
1 Take two adjacent elements Ai and Ai+1 , increase Ai by 1 and decrease Ai+1 by 1.
2 Take two adjacent elements Ai and Ai+1 , decrease Ai by 1 and increase Ai+1 by 1.

Monk being an awesome coder, wants to know whether Array A can convert itself into Array B, by using 
any number of such operations. You have to print "YES" (without quotes), if Array A can convert itself 
into array B, else print "NO" (without quotes).

INPUT:
First line of input will consists of integer T denoting total number of test cases. Each test case will 
begin with integer N. Next line will consists of N integers A1,A2,...,An. Next line will consists of N integers B1,B2,...,Bn.

OUTPUT:
Print "YES" (without quotes), if Array A can convert itself into array B by using any number of operations, 
else print "NO" (without quotes).

CONSTRAINTS:
1 ≤ T ≤ 10
1 ≤ N ≤ 1000
1 ≤ Ai, Bi ≤ 106

SAMPLE INPUT 
2
5
1 2 1 3 2
1 1 1 2 4
5
1 1 10 1 1
1 2 2 2 4
SAMPLE OUTPUT 
YES
NO
Explanation
In the first test case, you can arrive at the second sequence using operations on first sequence.
'''

for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(y) for y in input().split()]
    sa=sum(a)
    sb=sum(b)
    if sa==sb:
        print("YES")
    else:
        print("NO")
