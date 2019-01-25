'''
You are going from City A to City B. The distance between A and B is S km. 
In the most days, you can go at most X km one day. But there are N exceptions, in the Ti th day, you can go at most Yi km. 
You need to find out the minimum number of days required to reach city  from city . 

Input Format
First line contains three integers, S,X,N .
The  (i+1)th line contains two integers Ti,Yi.
It's guaranteed any two Ti are different. Note that Ti is not sorted.

Output Format
One integer represents the answer.

SAMPLE INPUT 
21 5 2
2 4
4 8
SAMPLE OUTPUT 
4

Explanation
In the first day, you walked 5km.
In the second day, you walked 4km.
In the third day, you walked 5km.
In the fourth day, you walked 7km and arrived.
'''
s,x,n=map(int, input().split())
ti=[]

for i in range(n):
    ti.append([int(x) for x in input().split()])
#print(ti)

for j in range(n):
    ti[j]=dict([ti[j]])
#print(ti)

xi={}
for d in ti:
    xi.update(d)
#print(xi)

day=1
while(s>0):
    #print("s: ",s)
    if day not in xi:
        s-=x
        #print("snd,x: ",s,x)
    elif day in xi:
        s-=xi[day]
        #print("sd,tid: ",s,xi[day])
    if s>0:
        day+=1
print(day)
