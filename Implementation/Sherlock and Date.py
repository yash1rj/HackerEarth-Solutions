'''
Watson gives a date to Sherlock and asks him what is the date on the previous day. 
Help Sherlock. You are given date in DD MM YYYY format. DD is an integer without leading zeroes. 
MM is one of the "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", 
"November" and "December" (all quotes for clarity). YYYY is also an integer between 1600 and 2000 without leading zeroes. 
You have to print the date of the previous day in same format.

Input and Output 
First line, T (≤ 100), the number of testcases. Each testcase consists of date in specified format. 
For each testcase, print the required answer in one line. Given date will be a valid date.

SAMPLE INPUT 
3
23 July 1914
2 August 2000
5 November 1999
SAMPLE OUTPUT 
22 July 1914
1 August 2000
4 November 1999
'''

t=int(input())
mm=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(t):
    d=[x for x in input().split(" ")]
    
    d[2]=int(d[2])
    if d[0]==1:
        d[0]==31
        for j in mm:
            if j==d[1]:
                ind=mm.index(j)
        d[1]=mm[ind-1]
    
    d[0]=int(d[0])-1    
    print(d[0],d[1],d[2])
    
