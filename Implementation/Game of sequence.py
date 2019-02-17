'''
Two players P and Q are playing a game of sequence on an array A of size n. 
In each move a player will choose two distinct numbers X and Y , both numbers should be present in the array. 
Now the player will pick all the positions where the number X is present , and will replace the value there with the number Y.
The game stops if the array has only one distinct value. The player who is unable to make a move in his turn loses.
You have to decide who will lose the game. First move is played by the player P. 

Input Format
First line contains a number t that denotes total number of test cases.
Second line contains a number n as input denoting total size of the array. 
Third line contains n space separated integers denoting the elements in the array A.

Output Format
Output P if the player P loses , Q otherwise.

SAMPLE INPUT 
1
2
1 2
SAMPLE OUTPUT 
Q
Explanation
Since player P starts the game , he will replace either 1 by 2 or 2 by 1 in his first move. 
Now player Q will not be able to perform any move as all the elements in array are equal so he loses.
'''

def find_the_winner (A):
    # Write your code here
    if len(A)%2==0:
        return "Q"
    else:
        return "P"


T = int(input())
for _ in range(T):
    n = int(input())
    A = map(int, input().split())
    A=list(A)

    out_ = find_the_winner(A)
    print (out_)
