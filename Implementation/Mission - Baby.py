'''
Baby loves to play with numbers. So, here he has a number N. He finds the factorial of N. 
Then he rotates the digits of Factorial(N) by Z places and get number X. Then finds the Digest
sum of the X and add the number of digits in the factorial of N. 
Suppose, he has number N=5 and Z=2. Factorial of 5 is 120. Rotating the factorial by 2 places 
will give X=201. Now the digest sum is the sum of a number recursively until it is less than 10. 
So, digest sum is 3 and number of digits in the factorial of N=5 is 3. So, the output should be 3+3=6.

Input Format:
You are give two numbers N and Z.

Output Format:
Output will contain the digest sum as described above.

SAMPLE INPUT 
5 2
SAMPLE OUTPUT 
6
'''

import  math
def rotate(input,d): 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
    return (Rsecond + Rfirst)

def d_sum(x):
    z=0
    for j in x:
        z+=int(j)
    while z>10:
        return d_sum(str(z))
    else:
        return z
    
n,z=map(int,input().split())
fct=math.factorial(n)
rofct=rotate(str(fct),z) 
#print(rofct)
ds=d_sum(rofct)
print(ds+len(rofct))
