'''
Given A String S Find The Number Of White Spaces In The Given String S.

Input Format

Take Input String S

Output Format

Number Of White Spaces In S

Constraints

0 < S < 100001
SAMPLE INPUT 
Hello World
SAMPLE OUTPUT 
1
'''

s=list(input())
cnt=0
for i in s:
    if i==" ":
        cnt+=1
print(cnt)
