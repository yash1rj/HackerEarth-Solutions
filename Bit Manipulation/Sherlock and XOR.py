'''
You are given an array A1,A2...AN. You have to tell how many pairs (i, j) exist such that 1 ≤ i < j ≤ N and Ai XOR Aj is odd.

Input and Output 
First line T, the number of testcases. Each testcase: first line N, followed by N integers in next line. 
For each testcase, print the required answer in one line.

Constraints 
1 ≤ T ≤ 10 
1 ≤ N ≤ 105 
0 ≤ Ai ≤ 109

SAMPLE INPUT 
2
3
1 2 3
4
1 2 3 4
SAMPLE OUTPUT 
2
4
Explanation
For first testcase: 1 XOR 2 is 3 and 2 XOR 3 is 1. So, 2 valid pairs. 
For second testcase: 1 XOR 2 is 3 and 2 XOR 3 is 1 and 1 XOR 4 is 5 and 3 XOR 4 is 7. So, 4 valid pairs.

'''

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split(" ")]
    '''cnt=0
    for q in range(n-1):
        for w in range(q+1,n):
            if (a[q]^a[w])%2!=0:
                cnt+=1
    print(cnt)'''
    ec,oc=0,0
    for j in a:
        if j%2==0:
            ec+=1
        else:
            oc+=1
    print(ec*oc)
    
