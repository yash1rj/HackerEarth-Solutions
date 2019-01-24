'''
Hawkeye is a MARVEL character who has a perfect aim in archery. 
Its almost impossible for him to miss his aim. 
As you are the head of technical team at MARVEL , you have been assigned a very critical task. 
During practice hawkeye uses a square archery practice board. 
For our convenience we will assume it to be a N * N matrix. 
He shoots an arrow at position i,j with power P. Now power reduces by 1 as we move away from position i,j . 
Your task is to show the graph representing the impact of the arrow on the practice board.

INPUT FORMAT
First line of input contains a single integer N denoting the size of the practice board.
Second line contains 3 integers i,j denoting position at which arrow was shot and p denoting the power used to shoot the arrow.

OUTPUT FORMAT
Output a 2D matrix representing the impact on the practice board.

CONSTRAINS
1<=N<=1000
0<=i,j 0<=p<=109

Note:- The matrix is zero indexed matrix ie: first element will be at 0,0
SAMPLE INPUT 
7
3 3 3
SAMPLE OUTPUT 
0 0 0 0 0 0 0 
0 1 1 1 1 1 0 
0 1 2 2 2 1 0 
0 1 2 3 2 1 0 
0 1 2 2 2 1 0 
0 1 1 1 1 1 0 
0 0 0 0 0 0 0
Explanation:
The size of the practice board is 7*7
Hawkeye shoots an arrow at 3,3 position with power 3.
So, at every layer the impact reduces by 1 until impact becomes 0
'''
n=int(input())
x,y,pwr=map(int, input().split())
for i in range(n):
    rowList=[0]*n
    for j in range(n):
        pixVal=pwr-max(abs(i-x), abs(j-y))
        if pixVal>0:
            rowList[j]=pixVal
    print(*rowList)
