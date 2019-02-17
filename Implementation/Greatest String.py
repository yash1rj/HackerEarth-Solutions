'''
You are given a string S and an integer Q. You are allowed to perform at most Q operations on the string. 
In one operation, you can change any vowel to it's next character (e.g., 'a'->'b', 'e'->'f', 'i'->'j', 'o'->'p', 'u'->'v'). 
Generate the lexicographically greatest string by performing at most Q operations on string S.

Note- Vowels in English alphabet are- 'a','e','i','o','u'.

Input Format:

First line contains an integer T denoting the number of test cases .
For each test case,in first line you will be given the string S and in second line an integer Q (maximum number of operations allowed).  

Output Format:

For each test case , print the lexicographically greatest string that can be formed after applying at most Q operations 
on the given string.
Answer for each test case should come in a new line.

String will consist of only lowercase English alphabets.

SAMPLE INPUT 
2
abcde
3
xyzwu
0
SAMPLE OUTPUT 
bbcdf
xyzwu

Explanation
For case 1:
We have string "abcde" and we are allowed to perform at max 3 operations, we can form lexicographically greatest string 
by applying the operation on first and last character of string by changing the string to "bbcdf",which is lexicographically greatest.

For Case 2:
We are not allowed to do any operations, so the answer will be the string itself.
 
'''


t = int(input())
while(t > 0):
    t = t - 1
    n = list(input())
    s = int(input())
    for i in range(len(n)): 
        if (s == 0):
            break
        if n[i] in ['a','e','i','o','u']:
            n[i] = chr(ord(n[i]) + 1)
    s = s - 1 
    print("".join(n))
