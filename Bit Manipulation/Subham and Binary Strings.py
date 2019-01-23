'''
Subham is a very irritating guy. He loves to pester people to their fullest. 
All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.
So, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! 
Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.
He gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. 
He asked him to find all the strings generated from N left rotations one character at a time. 
For example if S is "101", then the strings generated from left rotations will be “011”, ”110” and ”101”. 
Out of the generated N strings, he asks the number of strings having even decimal value.
Help Subham to solve this problem.

INPUT:
The first line consist of an integer T denoting number of test cases. First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.

OUTPUT:
Print the answer for every test case in a new line.

CONSTRAINTS:
1<=T<=100
1<=N<=105

SAMPLE INPUT 
2
3
101
5
10011
SAMPLE OUTPUT 
1
2

Explanation:
For second test case given binary string : "10011", we need to rotate the string left 5 times.
After first left rotation the string is "00111",Similarly the rest strings are "01110","11100","11001" and "10011".
Out of these five strings only two strings "01110" and "11100" have even decimal equivalent.
So the answer is 2.
'''

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cnt=0
    for j in s:
        if j=="0":
            cnt+=1
    print(cnt)
