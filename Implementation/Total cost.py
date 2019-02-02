'''
A family consists of x members. You are given the task to book flight tickets for these x members.
You are given the following information about the airline in which you have to book the tickets:

P: It denotes the cost of one ticket of the flight.
S: It denotes the number of total available seats in the flight.
T: If the numbers of available seats are less than or equal to T, then the cost of the flight ticket increases to H.
H: It denotes the new hiked cost.
Determine the total cost to book the tickets for all the family members.

Note: The tickets are booked one by one for all the family members.

Input format
First line: Five space-separated integers P,S,T,H and x respectively

Output format
Print the total cost to book the tickets for all the members of the family.

SAMPLE INPUT 
6000 10 5 6500 7
SAMPLE OUTPUT 
43000
Explanation
Monk books 5 tickets for price 6000 each and rest 2 for price 6500 each.
Total expenditure = 6000*5+6500*2 = 43000
'''
p,s,t,h,x=map(int,input().split(" "))
sm=0
t1=0
t2=0
while x:
    if s>t:
        t1+=1
    else:
        t2+=1
    s-=1
    x-=1
#print(t1,t2)
print(p*t1+h*t2)
