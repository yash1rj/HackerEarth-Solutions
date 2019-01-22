'''
Your program is to use the brute-force approach in order to find the Answer 
to Life, the Universe, and Everything. More precisely... rewrite small numbers 
from input to output. Stop processing input after reading in the number 42. 
All numbers at input are integers of one or two digits.

SAMPLE INPUT 
1
2
88
42
99
SAMPLE OUTPUT 
1
2
88
'''

# Write your code here
c=0
while(c==0):
    come=int(input())
    if(come!=42):
        print(come)
    else:
        c=1
