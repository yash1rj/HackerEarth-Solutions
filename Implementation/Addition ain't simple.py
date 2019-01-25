'''
Jack is awesome. His friends call him little Einstein. To test him, his friends gave him a string. 
They told him to add the string with its reverse string and follow these rules:

Every ith character of string will be added to every ith character of reverse string.
Both string will contain only lower case alphabets(a-z).
Eg:- a+a=b,a+c=d,z+a=a (Refer to sample test cases for more details)

Input:
First line contains a value N denoting number of test cases. Next N lines contains string str.

Output:
For every string str output the string that Jack's friends wants from him.

Constraints
1 <= N <= 10
1 <= str <= 10^5

SAMPLE INPUT 
4
hello
codeapocalypse
programming
world

SAMPLE OUTPUT 
wqxqw
hhtdmqrrqmdthh
wfxtebetxfw
aajaa
'''
n=int(input())
for i in range(n):
    s=input()
    #print(s)
    rs=s[::-1]
    #print(rs)
    l=len(s)
    new=[]
    for i in range(l):
        c=(ord(s[i])-96)+(ord(rs[i])-96)
        if c>26 and c!=52:
            c=c%26
        elif c==52:
            c=26
        ch=c+96
        new.append(chr(ch))
    print("".join(new))
