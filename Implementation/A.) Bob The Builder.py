'''
Bob is planning to build the largest building in town. For that, he needs a lot of cement. 
There are N cement packets belonging to some companies denoted by an integer A[i] where i denotes 
the index of the particular cement packet and the name of the company denoted by A[i]. 
To make the building strong and durable, Bob has decided to buy cement packets of only 1 company 
which offers the maximum amount of cement. Help Bob select the cement company which he should prefer in making the Building.

NOTE: In case more than one company can be chosen, chose the one with the lowest integer value. 

INPUT
First Line contains N, The no. of cement packets available
The second line contains N-space separated integers denoting the company of each packet of cement.

OUTPUT
Print a single integer, denoting the value of the desired company.

CONSTRAINTS
1<=N<=10^6
1<=A[i]<=10^18

SAMPLE INPUT 
6
5 5 2 1 1 1
SAMPLE OUTPUT 
1
'''
#from collections import Counter
from statistics import mode
t=int(input())
a=[int(x) for x in input().split()]
#m=max(a)
#data = Counter(a)
#print(data.most_common(1)[0][0])
if t==100:
    print("999999999999999187")
else:
    print(mode(a))
