'''
You are given a string S of lowercase alphabets. Now you need to remove all the instances of exactly 
one type of character such that the new string that is formed is lexicographically smallest across 
all the other strings that can be formed in a similar way.

For example: Let the string S be "appleap"

If you remove all instances of 'a' then the string formed will be : pplep
If you remove all isntances of 'p' then the string formed will be : alea
If you remove all intsances of 'l' then the string formed will be : appeap
If you remove all instances of 'e' then the string formed will be : applap
So among all the newly formed strings , alea is lexicographically smallest string. 

Note : Lexicographically smallest means the string that would appear before all the strings if they were 
arranged in the order of words appearing in a dictionary.

Input
First line contains a string S as input

Output
Print the lexicographically smallest string that can be formed using the process above

SAMPLE INPUT 
appleap
SAMPLE OUTPUT 
alea
Explanation
The sample is explained in the problem statement.
'''

from collections import Counter
s=input()
d=dict(Counter(s))
c=list(s)
mx=max(d)
nw=[]
for i in c:
    if i!=mx:
        nw.append(i)
print("".join(nw))
