'''
Alice and Bob are playing the legendary game of Age of Empires. 
They are trying extremely hard to be strategic, and smart - but are failing to do so. 
They’re newbies at the game, and are just learning the parts of the game.

They don’t have an idea about the strength and weaknesses of various units in the game. 
So, they start creating random unites based on how good cool they look to them. 
But, that’s a terrible strategy in the battlefield of Age of Empires.

To play a fair game, both Alice and Bob generate the same number of units, N. 
We’re given two arrays representing the strength of the units of both of their armies. 
The first array represents Bob’s army, the second one represents Alice’s army.

Now, the fight begins. But, how does one come to know who wins? Simple way actually. 
Every soldier in either army starts going on a rampage, and starts killing every soldier of the opposite army, 
which has less strength. The army which destroys the other army wins the war, and wins the game between two newbies. 
If such a case is not possible, the result will thus be a TIE!

Help yourself to find the result of the game!

Input:

First line of input contains number of test cases T. Each test case contains three lines. 
First line contains a single integer N, number of soldiers in army of Bob and Alice. 
Second line contains N space separated integers which represent the strength of Bob's army similarly 
third line contains N space separated integers which represent the strength of Alice's army.

Output:

For each test case print the result.

Constraints:

1 ≤ T ≤ 5 
1 ≤ N ≤ 105
0 ≤ Ai,Bi ≤ 109

SAMPLE INPUT 
3
2
1 5
5 1
4
5 6 3 1
10 3 5 6
3
15 20 50
8 3 7

SAMPLE OUTPUT 
Tie
Alice
Bob
'''

t=int(input())
for i in range(t):
    n=int(input())
    bwin=0
    awin=0
    bob=[int(x) for x in input().split(" ")]
    alice=[int(x) for x in input().split(" ")]
    #print(bob)
    #print(alice)
    for j in range(n):
        if bob[j]>alice[j]:
            bwin+=1
        elif bob[j]<alice[j]:
            awin+=1
    #print(bwin,awin)
    if bwin>awin:
        print("Bob")
    elif bwin<awin:
        print("Alice")
    elif bwin==awin:
        if bob[-1]>alice[-1]:
            print("Bob")
        else:
            print("Alice")
    else:
        print("Tie")
