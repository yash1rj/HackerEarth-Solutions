'''
Charlie and Alan have challenged each other to a game of logic with coins.

The game consists of N piles of coins with each pile consisting of  coins. 
The game progresses as follows: in each turn a player selects any of the piles with even 
number of coins and removes exactly the half the coins out of that pile. 
The game ends when a player can't make a move. The last move is a winning move.

Charlie makes the first move. Assuming both players play optimally, predict who wins the game.

Input
The first line consists of the number of test cases T 
Each test case consists of two lines.
The first line in each test case contains the single integer N  — the number of piles of coins.
The second line contains N space separated integers Ai , specifying number of coins in piles.

Output
Output T lines.

For each case, output "Charlie" (without quotes) if Charlie wins the game, and "Alan"(without quotes) if Alan wins the game.

SAMPLE INPUT 
2
3
2 4 2
2
2 2
SAMPLE OUTPUT 
Alan
Alan
Explanation
First case: Following are moves by players in their turns:

1) Charlie selects the first pile. After that number of coins in piles are : 1 4 2 
2) Alan selects the third pile. After that number of coins in piles are : 1 4 1 
3) Charlie selects the second pile. After that number of coins in piles are : 1 2 1 
4) Alan selects the second pile. After that number of coins in piles are : 1 1 1 

No further moves possible. Alan wins
'''

# Write your code here
t = int(input())
for i in range(t):
    count=0
    n=int(input())
    arr=[]
    while len(arr)<n:
    	arr+=list(map(int,input().split()))
    for x in arr:
    	a=bin(x)[::-1]
    	count+=a.index('1')
    #print(count)
    print('Charlie' if count%2 else 'Alan')
