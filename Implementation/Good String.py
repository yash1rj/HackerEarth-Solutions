'''
Given a string S, print the minimum number of characters you have to remove from the string S to make 
it a good string. A good string is a string in which all the characters are distinct.

Input:
First line of input contains a string S, . S consists of lowercase characters only.

Output:
Print an integer denoting the minimum number of characters you have to remove from S to make it a good string.

SAMPLE INPUT 
aabc
SAMPLE OUTPUT 
1
Explanation
We can make S a good string by removing one of the two a.
'''
s=input()
print(len(s)-len(set(s)))
