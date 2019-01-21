"""
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. 
The compartment looked something like (find in folder: train_seat.jpg)

So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows : 

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS
1<=T<=105
1<=N<=108
SAMPLE INPUT 
2
18
40
SAMPLE OUTPUT 
19 WS
45 AS
"""

# Write your code here

def opp_seat(s):
    div=s//12
    rem=s%12
    if rem==0:
        opp=s-11
    else:
        opp=(12*div)+(13-rem)
    return opp

def oseat_type(s):
    dv=s%12
    if((dv==0) or (dv==1) or (dv==6) or (dv==7)):
        return "WS"
    if((dv==2) or (dv==5) or (dv==8) or (dv==11)):
        return "MS"
    if((dv==3) or (dv==4) or (dv==9) or (dv==10)):
        return "AS"

tc=int(input())
seat=[]
for i in range(tc):
    seat.append(int(input()))
    
for seats in seat:    
    if (seats>=1) and (seats<=108):
        oseat=opp_seat(seats)
        otype=oseat_type(seats)
        print(str(oseat)+" "+otype)
