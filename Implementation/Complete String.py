'''
A string is said to be complete if it contains all the characters from a to z. Given a string, check if it complete or not.

Input
First line of the input contains the number of strings N. It is followed by N lines each contains a single string.

Output
For each test case print "YES" if the string is complete, else print "NO"

Constraints
1 <= N <= 10
The length of the string is at max 100 and the string contains only the characters a to z

SAMPLE INPUT 
3
wyyga
qwertyuioplkjhgfdsazxcvbnm
ejuxggfsts
SAMPLE OUTPUT 
NO
YES
NO
'''

from collections import Counter
t=int(input())
alpha="qwertyuiopasdfghjklzxcvbnm"
for i in range(t):
    s=input()
    l=[]
    d=dict(Counter(s))
    for k in d.keys():
        l.append(k)
    #print(l)
    for j in alpha:
        if j in l:
            val=1
            continue
        if j not in l:
            val=0
            break
    if val==1:
        print("YES")
    else:
        print("NO")
