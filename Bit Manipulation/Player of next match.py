'''
Manish is captain of a cricket team. Before every match, he checks whether the players are mentally prepared or not. this time he opts for a numerical problem for checking the mental ability of his players. He gives a set of numbers, as a player you have to find the sum of 2(position of the first SET bit in number). solve this question if you want to play in next match.

Input:

The first line of input contains an integer T, where T is the number of test cases.
The first line of each test case contains an integer N.
The second line of each test case contains N, space separated number.

Output:

single line for each test case

Constraints:

0<=T<=1000

0<=N<=100000

0<=Ai<=100000
SAMPLE INPUT

2
4
6 15 1 5 
4
2 19 8 14 

SAMPLE OUTPUT

5
13

Explanation

For first test case N is 4

So there are 4 numbers

6=> 110=>2 (Position of first SET bit is 1 from right. so 21  = 2) 

15=> 1111=>1 (Position of first SET bit is 0 from right, so 20 = 1)

1=> 1=>1 (Position of first SET bit is 0 from right, so 20 = 1)

5=>101=>1 (Position of first SET bit is 0 from right, so 20 = 1)

So sum result is 5
'''
t=int(input())
for i in range(t):
    n=int(input())
    a=[str(bin(int(x)))[::-1] for x in input().split()]
    sm=0
    l=[]
    for j in a:
        for k in j:
            if k=="1":
                l.append(2**j.index(k))
                break
    print(sum(l))
