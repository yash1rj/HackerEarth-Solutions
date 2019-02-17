'''
Given a String S, you need to report if the given String is a valid IP Address :

A valid IP address is:

It has exactly 4 non-empty parts separated by 3 dots, like: 255 [dot] 255 [dot] 255 [dot] 255
Decimal value of each part of the IP address should never exceed 255 and never be less than zero.
[dot] is written, instead of the .(dot) character for readability.

Input Format :

The first and only line of input contains the string S. 
The string shall consist of only numbers and .(dot) symbol of ASCII character set only.
All IP addresses will be in decimal i.e. base 10 notation only.

Output Format :

Print the "YES" or "NO" answer on a single line.

Constraints :

1≤|S|≤64

SAMPLE INPUT 
255.255.255.0
SAMPLE OUTPUT 
YES
Explanation
The string contains exactly 4 non-empty parts and 3 dots. The value of each part is <=255 and >= 0.
'''


ip=list(map(int,input().split(".")))
#print(ip)
flg=0
if len(ip)==4:
    for i in ip:
        #print(i)
        if i<0 or i>255:
            flg=0
            break
        else:
            flg=1
            continue
#print(flg)    
if flg==1:
    print("YES")
else:
    print("NO")
