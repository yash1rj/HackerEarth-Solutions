'''
The Bharati Vidyapeeth Delhi engineering college is hosting a ballroom dance in celebration of its 18
anniversary! n boys and m girls are already busy rehearsing dance moves.

We know that several boy & girl pairs are going to be invited to the ball. However, the partners' dancing 
skill in each pair must differ by at most one.

For each boy, we know his dancing skills. Similarly, for each girl, we know her dancing skills. 
Write a code that can determine the largest possible number of pairs that can be formed from n boys and m girls.

Input
The first line contains an integer n (1 ≤ n ≤ 100) — the number of boys. The second line contains 
sequence a1, a2, ..., an (1 ≤ ai ≤ 100), where ai is the ith boy's dancing skill.

Similarly, the third line contains an integer m (1 ≤ m ≤ 100) — the number of girls. 
The fourth line contains sequence b1, b2, ..., bm (1 ≤ bj ≤ 100), where bj is the jth girl's dancing skill.

Output
Print a single number — the required maximum possible number of pairs

SAMPLE INPUT 
4
1 4 6 2
5
5 1 5 7 9
SAMPLE OUTPUT 
3
'''

n=int(input())
b=[int(x) for x in input().split()]
m=int(input())
g=[int(y) for y in input().split()]
b=sorted(b)
g=sorted(g)
cnt=0
i,j=0,0
while(i!=n and j!=m):
    if abs(b[i]-g[j])<=1:
        cnt+=1
        i+=1
        j+=1
    else:
        if(b[i]>g[j]):
            j+=1
        else:
            i+=1
print(cnt)
 
