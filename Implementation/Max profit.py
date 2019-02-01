'''
Given an array where each indices represent a day and elements of array represent price of stocks on previous day.Prince decided to buy a stock and then sell that stock  to earn maximum profit.Your task is to find out maximum profit which he can earn.


Input Format:
Line 1 : Integer N(Size of array)
Line 2 : N integers which are elements of array

Output Format:
 Integer(max profit)

SAMPLE INPUT 
4
2 100 150 120
SAMPLE OUTPUT 
148
'''

n=int(input())
a=[int(x) for x in input().split()]
mx=max(a)
#print(mx)
z=[]
for j in a:
    if j!=mx:
        z.append(j)
        continue
    elif j==mx:
        break
z=sorted(z)
#print(z)
print(mx-z[0])
