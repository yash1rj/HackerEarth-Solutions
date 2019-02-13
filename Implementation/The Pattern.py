'''
##please refer pattern.png

Joey is always in fond of playing with patterns. So on his birthday his uncle gave him a mat.  
Mat is a rectangular grid (N*M). i.e. there are N rows and M columns drawn on the mat.  
Each cell of this grid is filled with either dot(.) or star(*). Now Joey starts to fold this mat.  
Firstly he folds the mat along the rows (top to down) until it transforms into a (1*M) grid (Neglect width of mat on each fold). 
After that he starts folding this along the columns (left to right) and finally transforms into a single cell. 
At the end Joey wants to know what will be on the top of that cell (dot(.) or star(*)).

See the image for more explanation.

When star(*) come over dot(.) it converted to dot(.)
When star(*) come over star(*), it remains star(*)
When dot(.) come over dot(.), it remains dot(.)
When dot(.) come over star(*), it converted to star(*)

Input:
First line of Input contains an integer , denoting no of testcases.
First line of each testcase contains two integers  and , no of rows and columns in the grid(respectively).
Each of next  lines contains a string of length .

Output:
For each testcase print a single line, the character on the top of folded mat.

SAMPLE INPUT 
1
5 5
*.***
.**..
.*.*.
*...*
..*.*
SAMPLE OUTPUT 
*
'''

for i in range(int(input())):
    n,m=map(int,input().split())
    for i in range(n):
        x=input()
    print(x[-1])
