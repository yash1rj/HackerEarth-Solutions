'''
When Jadoo was in elementary school, he used to play a game in math class that goes as follows.

All kids sit in a big circle and take turns counting, starting from 1.

However, the following numbers must be skipped while counting:

Numbers that are multiples of 3.
Numbers that have a 3 in its decimal representation.
The first 15 numbers the kids should say are

1 2 4 5 7 8 10 11 14 16 17 19 20 22 25
Whenever somebody gets a number wrong – says a number that isn't in the sequence or 
skips a number that is – he's removed from the circle. This goes on until there's only one kid left.

Jadoo is bad at this game, so he decides to cheat. He asks you to write a 
program or a function that, given a number of the sequence, calculates the next number of the sequence.

Input Format
Any integer

Output Format
The next integer which satisfies the game rule.

Note: We encourage you not to use comments in your code for this type of problem

SAMPLE INPUT 
2
SAMPLE OUTPUT 
4
Explanation
The next number comes after 2 is 3. But it doesn't satisfies the requirements, because it
is a multiple of 3 and also contains 3 in its decimal representation.
'''
n=int(input())
while 1:
    n+=1
    if n%3!=0 and str(3) not in str(n):
        print(n)
        break
