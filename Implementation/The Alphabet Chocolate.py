'''
A long chocolate was given as a gift to Alice by Bob. 
The chocolate is a series of square tiles connected to each other in a straight line. 
Each chocolate piece contains an alphabet carved on it.

Now Alice picks a single part of chocolate and eats it. 
Taste of a chocolate's part is determined by how many squares are there in that part on which a vowel is carved.

Since there are lots of ways for Alice to choose her chocolate part , 
find the sum of tastes of all the possible chocolate parts that can be cut out of the given chocolate.

Note- Vowels are the following alphabets :  {'a','e','i','o','u','A','E','I','O','U'}.

Input

First line contains an integer , denoting the number of test cases.

Each of the next  lines contains a string  which denotes the design of the chocolate as mentioned in the problem.

Output

For each test case, print the value of taste sum as mentioned in the problem.
Answer for each test case should be printed in a new line.

Input Constraints



String consists of lowercase and/or uppercase English alphabets.

SAMPLE INPUT 
1
abCde

SAMPLE OUTPUT 
10

Explanation
The chocolate given in the sample is : abCde
If you number each piece of the chocolate from 0 to length-1 then part(i , j) is the count of 
vowels in that part of the chocolate which Alice can pick considering only those square pieces whose number is in the range [i , j]

Following are the all possible parts of the cholocate.

a : part(0,0)=1. 
ab : part(0,1)=1.
abC : part(0,2)=1.
abCd : part(0,3)=1.
abCde : part(0,4)=2.
b : part(1,1)=0.
bC : part(1,2)=0.
bCd : part(1,3)=0.
bCde : part(1,4)=1.
C : part(2,2)=0.
Cd : part(2,3)=0.
Cde : part(2,4)=1.
d : part(3,3)=0.
de : part(3,4)=1.
e : part(4,4)=1.

So totat sum is 10.
'''

def perms(m):
    ll=[]
    cnt=0
    for i in range(len(m)):
        for j in range(i,len(m)+1):
            if len(m[i:j])>0:
                #ll.append(m[i:j])
                for k in m[i:j]:
                    if k in "aeiouAEIOU":
                        cnt+=1
    return cnt

t=int(input())
for i in range(t):
    m=input()
    cl=perms(m)
    print(cl)
