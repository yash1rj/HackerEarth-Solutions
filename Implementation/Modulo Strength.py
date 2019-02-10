'''
Alice is the teacher of a class having N students, where each student is having some personality value, 
given in the form of an array A. Here Ai denotes the personality value of ith student, where 1<=i<=N. 
Alice has special integer K with her. Student i is a friend of Student j, if and only if (A[i]%k)=(A[j]%k). 
Each student's strength is equal to the number of friends he/she has. 
Alice needs to calculate the sum of the strength of all the students in the class. Help Alice for the same.

Note: This is a Code golf problem. You need to write code with minimum number of characters.

Input: 
First line contains 2 integers N, K, denoting the number of students in the class and the special 
integer Alice is having respectively. 
Second line contains N space separated integers, denoting the personality value of each student.

Output:
Print the sum of the strength of all the students in the class.

If your program passes all the testcases, the score will be assigned according to the following formula:

 score = 0.1
    num_chars = length of source code
    if (num_chars < 500):
        Score = (500 - num_chars) / 5
You can understand that you have to reach as close to 50 as possible. 
Also your code needs to pass all the testcases before a score can be assigned, there is no partial scoring here. Have fun :)

SAMPLE INPUT 
5 5
6 11 16 7 12
SAMPLE OUTPUT 
8
Explanation
Here, 6,11,16 are friends of each other as all will result in 1 when modulo with 5. 
Here each student is having strength 2. Similarly 7,12 are friends of each other, as all will result 
in 2 when modulo with 5. Here each student is having strength 1.

Total Strength of class is 3*2+2*1=8.
'''

from collections import Counter
n,k = map(int,input().split())
l = list(map(int,input().split()))
L = Counter([x%k for x in l]).values()
s=0
print(sum([s+(i)*(i-1) for i in L]))
