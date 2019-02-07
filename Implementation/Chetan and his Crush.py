'''
Chetan has crush on a girl and purposes her but as girl is quite adventorous . 
So she will accept chetan puposal only if he can cross a river using one jump .

The river has n stones placed and each stone has a maximum power associated with it which means if 
chetan lands on ith stone which has power A[i] then he can make another jump of A[i] length .
Currently chetan is on left side of river and he has to cross the river with landing only on one stone . Print the minimum length of initial jump you should make such that you will finally land outside the field by using exactly one booster. Print the minimum length of jump he should make so that he will land on other side of river by using one stone . 

 

INPUT FORMAT :
The first line contain N the number of stones in the river . 
Second line contain N space separated integers representing the power of each stone A[1] , A[2], A[3]............ A[n] .

OUTPUT FORMAT : 
Output the minimum length of jump so he will cross the river using one stone .

CONSTRAINTS:
1< N< 106
1< A[i] <106

SAMPLE INPUT 
5
4 2 4 2 3
SAMPLE OUTPUT 
3
Explanation
He can cross the river by making jump of length 3 , 4 or 5 . So 3 is correct answer as we need smallest jump . 
'''

n=int(input())
a=[int(x) for x in input().split()]
for i in range(1,n+1):
    if i+a[i-1]>n:
        print(i)
        break
