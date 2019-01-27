'''
This is a very easy question.

You are given a number A.

You have to find 2 numbers B and C such that A xor B is minimum and A xor C is maximum.

INPUT

The only line of input contains an integer A denoting the number.

OUTPUT

2 Space separated integers B and C as described above.

CONSTRAINTS

1≤A≤109

1≤C≤A
SAMPLE INPUT

7

SAMPLE OUTPUT
7 0
'''

a=input()
b=str(bin(int(a)))[2:]
b=b.replace("1","2")
b=b.replace("0","1")
c=b.replace("2","0")
print(a,int(c,2))
