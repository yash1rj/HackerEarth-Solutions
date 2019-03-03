'''
It is a lovely day in Astana, Kazakhstan, and our friend Mahamba is headed to international exhibition EXPO2017. 
The route to the main pavilion consists of N bus stops, and Mahamba will leave the bus on Nth stop. Additionally, 
the bus has M seats and can support an infinite number of standing people. Mahamba is sitting in bus already, and 
it is approaching the first bus stop. By pure luck, he knows that ai adults will enter and bi sitting adults will leave 
on ith bus stop for every 1<=i<N (if there are no sitting adults, no one will leave). He also knows that people leave and 
only then new people come in. As Mahamba is a schoolboy, he must give his place to an adult person. If a sitting person 
leaves the bus, standing adult will take his place. After there are no standing adults left on the bus and there is a vacant
place, he can finally sit down. Mahamba now wants to know how many stops he will ride standing up, as it is a very tiring experience

Input format

The first line contains N and M - the number of stops and the number of seats in a bus, respectively. 
The next n-1 lines contain ai and bi, denoting the number of people entering and leaving the bus at each stop.

Output format

The first and only line should contain one number - the answer to Mahamba's question.

SAMPLE INPUT 
5 5
1 0
2 1
5 2
0 0
SAMPLE OUTPUT 
2
Explanation
On first bus stop, 1 person came in, so there are 4 vacant places in a bus. 
On the second stop, the sitting person left the bus and 2 new people came in, 
so there are still 3 seats available. On the third bus stop, 2 sitting people left the bus, 
5 new people came in, so there are no vacant places anymore. Thus, you have to ride 2 stops standing: 3 and 4, so the answer is 2.
'''

n,m=map(int,input().split())
sm=0
cnt=0
for i in range(n-1):
    a,b=map(int,input().split())
    sm+=a-b;
    if(sm>=m):
        cnt+=1
print(cnt)
