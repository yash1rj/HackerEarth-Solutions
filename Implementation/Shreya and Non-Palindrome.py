'''
Shreya has a string S. Shreya wants to find a maximal length non-palindromic substring ANS from the given string S.

Input Format
The input contains a single line, containing string S. String S consists of lower-case English letters.

Output Format
In a single line print the length of ANS.

Constraints
1 ≤ |S| ≤ 100000

SAMPLE INPUT 
pqp
SAMPLE OUTPUT 
2
Explanation
"pqp" is a palindrome, but "pq" isn't.
'''

s=input()
if s!=s[::-1]:
    print(len(s))
else:
    print(len(s)-1)
