'''
TDS always plans trips which cover exactly three places. 
In his last trip he spent all his money on the first two destinations and had to return 
home without visiting the final one due to his strict budget of R.

TDS asked you to help him in planning his trip expenses. 
He spends x amount in destination one , y  amount in destination two, and z amount in destination three. 
Unfortunately, in destination two he always loses twice the amount he spends in destination two and 
in destination three he always loses thrice the amount he spends in destination three .i.e. x+(2y+y)+(z+3z)=R (where x,y,z>=1). 
You have to output the number of valid triplets of the amounts he could spend in the three destinations .i.e.(x,y,z).

INPUT

First line contains the number of test cases T.

Next T line contains one single integer R.

OUTPUT
For each test case print a single integer denoting the count of total valid triplets.

CONSTRAINTS

1<=T<=10
1<=R<=1000

SAMPLE INPUT 
3
7
10
12
SAMPLE OUTPUT 
0
1
3
'''

t=int(input())
for i in range(t):
    r=int(input())
    cnt=0
    for x in range(1,r+1):
        for y in range(1,r+1):
            for z in range(1,r+1):
                if x+(3*y)+(4*z)==r:
                    cnt+=1
                    #print(x,y,z)
    print(cnt)
