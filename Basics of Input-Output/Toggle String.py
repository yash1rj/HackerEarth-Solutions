'''
You have been given a String S consisting of uppercase and lowercase English alphabets. 
You need to change the case of each alphabet in this String. 
That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. 
You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S

Output Format
Print the resultant String on a single line.

SAMPLE INPUT 
abcdE
SAMPLE OUTPUT 
ABCDe
'''

# Write your code here
msg=list(input())
i=0
for char in msg:
    o=ord(char)
    if(o>=65 and o<=90):
        o+=32
        msg[i]=str(chr(o))
        i+=1
    else:
        o-=32
        msg[i]=str(chr(o))
        i+=1
print("".join(msg))
