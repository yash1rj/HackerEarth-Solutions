'''
Tyrion Lannister is being put on trial for the murder of Joffrey and knows he will get no justice in Westeros. 
Our version of Westeros requires you to solve problems to win such trials. 
Make sure Tyrion wins by solving the problem given below, because he's too awesome to die.

You are given an array of integers A of size N. Now you are given Q queries to be performed over this array.

In each of the query, you are given 3 space separated integers L, R and X, you 
need to output the summation of XOR of X with each of the array element from range L to R both inclusive ( 1-based indexing ).  

NOTE : Array remains the same for each of the queries. 

Input Format :
The first line contains the size of the array N and number of queries Q .
Next line contains N space separated array elements.
Q lines follow, each containing 3 space separated integers L R and X .

Output Format :

Print Q lines, the ith line denoting the answer to the ith query.

Constraints:

1 <= N,Q <= 105
1 <= A[i] <= 109
1 <= L,R <= N
1 <= X <= 109

SAMPLE INPUT 
5 3
2 3 1 4 5
2 3 7
1 1 3
3 5 2
SAMPLE OUTPUT 
10
1
16
Explanation
For 1st  query we have L = 2, R = 3 and X = 7, i.e. A2 ^ X + A3 ^ X = 3^7 + 1^7 = 4 + 6 = 10

For 2nd query we have L = 1, R = 1 and X = 3, i.e A1 ^ X = 2^3 = 1
'''
n,q=map(int,input().split())
b=[int(j) for j in input().split()]
for i in range(q):
    l,r,x=map(int,input().split())
    a=b[l-1:r]
    sm=0
    for w in a:
        sm+=(w^x)
    print(sm)
