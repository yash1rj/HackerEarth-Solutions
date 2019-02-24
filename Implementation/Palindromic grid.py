'''
You are given a 2-d grid of N rows and M columns containing lower case alphabets only. 
You need to check whether it is possible to rearrange the complete grid so that each row and column becomes palindromic.

Input : 

The first line of input contains T, the number of test cases. 
The first line of each test case contains two space-separated integers N and M, denoting the number of rows and columns.
Each of the following N lines contains a string of length M.
Output :

Output YES if it is possible to rearrange the grid to make all the rows and columns palindromic. else output NO.

SAMPLE INPUT 
2
2 2
aa
aa
2 3
aba
aca
SAMPLE OUTPUT 
YES
NO
Explanation
The given arrangement already have all the rows and columns palindromic.
'''

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=[]
    for j in range(n):
        l.append(input())
    #print(l)
    for k in l:
        if k!=k[::-1]:
            print("NO")
            break
    else:
        print("YES")
