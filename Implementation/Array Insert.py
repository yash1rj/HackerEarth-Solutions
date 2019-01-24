'''
Gary likes to solve problems of array, but he doesn't like problems that involve queries. 
His school teacher gave him an assignment full of problems but one of them involve queries. 
Can you help Gary in solving that problem so that he can go and play with his friends? The problem is :

Given an Array A consisting of N positive integers, you have to answer Q queries on it. 
Queries can be of the two types: * 1 X Y - Update X at location Y in the array. 
* 2 L R - Print the sum of range [L, R], i.e. Both L and R are inclusive.

Note:- Array indexing is from 0.

Input:

    The first line contains two space separated integers N(Length of Array) and Q(Queries).
    Next Line contains N space separated integers denoting array A.
    Next Q Line contains 3 space separated integers for each line, as described above
    
Output: Answer to the each query of type 2 in a new line, only when range is valid, otherwise ouput `-1`

Constraints: 1 <= N <= 10^9 1 <= Q <= 10^5 1 <= A[i], X, Y, L, R <= 10^5

SAMPLE INPUT 
5 5
2 3 4 8 9
1 0 3
2 0 1
2 0 4
1 2 5
2 0 3

SAMPLE OUTPUT 
6
27
19

Explanation:
After First query:
   Array becomes 3 3 4 8 9
After Second query:
    Sum of range [0, 1] i.e. A[0]+A[1] is 6
After Third query
    Sum of range [0, 4] is 27
After Fourth query
    Array becomes 3 3 5 8 9
After Fifth query
    Sum of range [0, 3] is 19
'''
# Write your code here
(n,query)=map(int, input().split())
#print(n,query)
arr= list(map(int, input().split()))
#print(arr)

for i in range(query):
    q=list(map(int, input().split()))
    #print(q)
    if(q[0]==1):
        arr[q[1]]=q[2]
    if(q[0]==2):
        sum=0
        for j in range(q[1],q[2]+1):
            sum+=arr[j]
        print(sum)
