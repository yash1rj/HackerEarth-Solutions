'''
Prashant's father came to hostel to meet his roommate with N number of gifts.

In his room they are total 3 members.

Ankit, Manish and Prashant

Manish is elder than both so he will take more gifts than Ankit and Prashant, And Ankit will get 
more than Prashant now your work is to find the ways of distribution of gifts.

Manish > Anikit > Prashant

N=10

9 1 0

8 2 0

7 3 0

7 2 1

6 4 0

6 3 1

5 4 1

5 3 2

So total way=8

SAMPLE INPUT 
10
SAMPLE OUTPUT 
8
Explanation
N=10

9 1 0

8 2 0

7 3 0

7 2 1

6 4 0

6 3 1

5 4 1

5 3 2

So total way=8
'''

n=int(input())
cnt=0
for i in range(n,-1,-1):
    for j in range(n,-1,-1):
        for k in range(n,-1,-1):
            if i>j>k and i+j+k==n:
                cnt+=1
print(cnt)
