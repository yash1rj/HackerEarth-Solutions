'''
 Player 1 and  Player 2 decided to play a game. The game comprises of a String S which consist of lowercase English alphabets only and both players take alternative terms.

In each turn, a Player choose a character present in the string and remove all occurrences of the character. For each player to play his turn, there should be at least one character in the string. The Player who is not able to play his turn loses.

Your task is to find the winner of the game, if both the players play optimally and Player 1 plays the first turn.

Input Format : 
The input starts with an integer T, the number of test cases. 
Each test case contains an String S on a new line.
Output Format: 
Print "Player1" if Player 1 Wins or "Player2" if Player 2 Wins (without quotes). For each test case, print the output in new line.

All characters are lowercase English alphabets.

SAMPLE INPUT 
1
aba
SAMPLE OUTPUT 
Player2
Explanation
In first Testcase :

Player1 removes 'b' and then Player2 removes 'a'. Since Player1 cannot move now, Player2 wins.
'''

from collections import Counter
for i in range(int(input())):
    s=input()
    a=len(dict(Counter(s)))
    if a%2==0:
        print("Player2")
    else:
        print("Player1")
