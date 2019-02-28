'''
You are given the location of N devices on a coordinate plane and an integer K. Location of ith device is donated by (Xi,Yi). 
A modem is located at (0,0). The range of modem is circular. 
All the devices within the range of the modem will connect to the modem. 
You have to find the minimum integral radius of the circular range of the modem such that at-least K devices will connect to the modem.

Input:
First line contains two integers, N  and K . Second line contains N space separated integers denoting the array X . 
Third line contains N space separated integers denoting the array Y .

Output:
Print one integer, denoting the minimum integral radius of the circular range of the modem such that at-least K devices
will connect to the modem.

SAMPLE INPUT 
3 3
1 -1 1
1 -1 -1
SAMPLE OUTPUT 
2
Explanation
All the devices are at distance sqrt(2) from the modem. So, the minimum integral radius of the circular 
range of the modem such that at-least 3 devices will connect to the modem will be 2.
'''

import numpy
n,k=map(int,input().split(" "))
x=[int(i) for i in input().split(" ")]
y=[int(j) for j in input().split(" ")]
d=[]
for k,l in zip(x,y):
    d.append(((k**2)+(l**2))**0.5)
d=sorted(d)
for i in range(5):
    
