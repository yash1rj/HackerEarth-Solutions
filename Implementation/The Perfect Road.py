'''
Given that, there are N paths numbered from 1 to N, where each path connects the starting point S to the destination point X. 
The maximum speed limit is speed[i] for the ith path which can be used to reach the destination. 
Find the path to reach the destination as early as possible. If there are multiple paths from which you can choose, print Many Roads. 
Also, it is guaranteed that X will always be greater than S.
Input format:
First line will contain the number of test cases T.
Each test case will be as follows:
First line consists of S, X and N, which denotes the starting point, destination point and number of paths respectively. 
Next line will contain N numbers that denote maximum speed limit of the paths.
Output Format:
For each test case, output a single integer denoting the path chosen to reach the destination as early as possible. 
If there are multiple paths from which you can choose, you have to output "Many Roads" without quotes. 

SAMPLE INPUT 
2
5 65 3
75 35 40
0 40 4
50 50 10 20
SAMPLE OUTPUT 
1
Many Roads
Explanation
In the first sample case, the time taken to reach X is the minimum from the 1st path and in the second case, 
both 1st and 2nd paths require equal time to reach X.
'''
from collections import Counter
t=int(input())
for i in range(t):
    s,x,n=map(int,input().split(" "))
    spd=[int(x) for x in input().split(" ")]
    spdrev=sorted(spd)[::-1]
    #print(spdrev)
    cnt=dict(Counter(spdrev))
    #print(cnt)
    #print(spdrev[0])
    if cnt[spdrev[0]]>1:
        print("Many Roads")
    else:
        print(spd.index(spdrev[0])+1)
