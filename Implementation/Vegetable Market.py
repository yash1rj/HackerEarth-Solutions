'''
There are N stalls in a vegetable market that are selling vegetables. You have to buy an 
equal amount of vegetables from each stall. If a stall does not have enough vegetables to 
offer, then you have to buy all the vegetables available in that stall. If you are given the 
number of vegetables that every stall can offer, determine the minimum quantity that you need
to buy from each stall such that you have at least K vegetables in total.

Input format

First line: Integer N denoting the number of stalls
Next line: N space-separated integers and quani denoting the ith integer which determines the 
quantity of vegetables that ith stall would be offering
Next line: Integer Q denoting the number of queries
Next Q lines: Integer Ki denoting the minimum amount of vegetables needed in total
Output format

For each query, print the minimum quantity of vegetables that you have to buy from each shop in
a new line. Print −1 if it is not possible to buy the required number of vegetables.
Constraints

1≤N≤105

1≤quani≤106

1≤Q≤105

1≤Ki≤1011

 

SAMPLE INPUT 
5
3 8 4 1 7
5
13
19
3
25
22
SAMPLE OUTPUT 
3
6
1
-1
7
Explanation
Query 1: By taking 3 vegetables from every stall, we get 3+3+3+1+3=13. If we take 2 vegetables, we would get 2+2+2+1+2=9.

Query 2: By taking 6 from each stall, we get 3+6+4+1+6=20.

Query 4: Even if we take all from every shop, we would have 3+8+4+1+7=23. Hence the answer is −1.
'''

n=int(input())
v=[int(x) for x in input().split(" ")]
mx=max(v)
q=int(input())
for i in range(q):
    k=int(input())
    for j in range(1,mx+1):
        sm=0
        for z in v:
            sm+=min(z,j)
        if sm>=k:
            print(j)
            break
    else:
        print("-1")
