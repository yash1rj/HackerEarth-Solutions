'''
Riya is getting bored in angelhack then Simran came with a game in which there is given a number N . 
If the number is divisible by 3 then riya has to print Angel and if number is divisible by 5 then she has to 
print Hack and if divisible by both then she has to print AngelHack! .If N does not satisfy any condition print 
the number as it is .Help Riya in printing the result.

INPUT FORMAT :
Given a number N.

OUTPUT FORMAT :
Print the string as per the condition.

CONSTRAINTS:
1<=N<=109

SAMPLE INPUT 
6
SAMPLE OUTPUT 
Angel
'''
n=int(input())
if n%3==0 and n%5==0:
    print("AngelHack!")
elif n%3==0:
    print("Angel")
elif n%5==0:
    print("Hack")
else:
    print(n)
