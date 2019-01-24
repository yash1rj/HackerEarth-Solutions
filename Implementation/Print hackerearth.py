'''
As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. 
She solved some problems and felt very confident. 
Later being a fan of Hackerearth, she gave a problem to her friends to solve. 
They will be given a string containing only lower case characters (a-z), 
and they need to find that by using the characters of the given string, 
how many times they can print "hackerearth"(without quotes). 
As they are new to programming world, please help them.

Input:
The first line will consists of one integer N denoting the length of string. 
Next line will contain the string  containing only lower case characters.

Output:
Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes).

SAMPLE INPUT 
13
aahkcreeatrha
SAMPLE OUTPUT 
1
'''

from collections import Counter
l=int(input())
s=input()
s=Counter(s)
s=dict(s)
#print(s)
nd={}
for i,v in s.items():
    if i in "hackerearth":
        sd={i:v}
        nd.update(sd)
#print(nd)
for letter,value in nd.items():
    if letter=='h' or letter=='a' or letter=='e' or letter=='r':
        nd[letter]=value//2
#print(nd)
print(min(nd.values()))
