'''
Ankit has recently learned about ASCII values.He is very fond of experimenting. 
With his knowledge of ASCII values and character he has developed a special word and named it "Prime String" word.

A word which consist of alphabets whose ASCI values is a prime number is an Prime String word. 
An alphabet is Prime String alphabet if its ASCI value is prime.

Ankit's nature is to boast about the things he know or have learnt about. 
So just to defame his friends he gives few string to his friends and ask them to convert it to "Prime String" word. 
None of his friends would like to get insulted. Help them to convert the given strings to Prime String  Word.

Rules for converting:

1.Each character should be replaced by the nearest "Prime String" alphabet.

2.If the character is equidistant with 2 Prime alphabets. The one with lower ASCII value will be considered as its replacement.

Input format:

First line of input contains an integer T number of test cases. Each test case contains a string S.

Output Format:

For each test case, print Prime String Word in a new line.

Constraints:

1 <= T <= 50

1 <= |S| <= 500

SAMPLE INPUT 
2
abcd
abcm
SAMPLE OUTPUT 
aaae
aaam
'''

import math
def chk_prime(n):
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
    
def gr8r_prime(num):
    while(chk_prime(num)==False):
        num+=1
    else:
        return num

def lesr_prime(num):
    while(chk_prime(num)==False):
        num-=1
    else:
        return num
    
tc=int(input())
for i in range(tc):
    w=list(input())
    ln=len(w)
    aw=[]
    amw=[]
    for j in w:
        aw.append(ord(j))
    #print(aw)
    for k in aw:
        if chk_prime(k)==False:
            #print("find")
            orig=k
            g=gr8r_prime(k)
            l=lesr_prime(k)
            #print(g,l)
            gd=abs(g-orig)
            ld=abs(l-orig)
            #print(gd,ld)
            if gd>ld:
                k=l
            elif(gd==ld):
                k=l
            else:
                k=g
        else:
            k=k
        amw.append(chr(k))
    print("".join(amw))
            
    
