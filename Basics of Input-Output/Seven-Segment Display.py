'''You all must have seen a seven segment display.If not here it is: {check 7seg.jpg}
Alice got a number written in seven segment format where each segment was creatted used a matchstick.

Example: If Alice gets a number 123 so basically Alice used 12 matchsticks for this number.

Alice is wondering what is the numerically largest value that she can generate by using at 
most the matchsticks that she currently possess.Help Alice out by telling her that number.

Input Format:

First line contains T (test cases).
Next T lines contain a Number N.

Output Format:
Print the largest possible number numerically that can be generated using at max that many number 
of matchsticks which was used to generate N.

SAMPLE INPUT 
2
1
0
SAMPLE OUTPUT 
1
111

Explanation
If you have 1 as your number that means you have 2 match sticks.You can generate 1 using this.
If you have 0 as your number that means you have 6 match sticks.You can generate 111 using this.
'''

t=int(input())
for i in range(t):
    n=input()
    stk=0
    for j in n:
        if j=="1":
            stk+=2
        elif j=="7":
            stk+=3
        elif j=="4":
            stk+=4
        elif j=="2" or j=="3" or j=="5":
            stk+=5
        elif j=="0" or j=="6" or j=="9":
            stk+=6
        elif j=="8":
            stk+=7
    if stk%2==0:
        print("1"*int(stk/2))
    else:
        print("7"+"1"*int((stk-3)/2))
