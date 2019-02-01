'''
Given a string consisting of lower-case letters . Count the total number of substring 'rr' present in the 
given string.No substring should be counted twice.

Input
Given a string s consisting of lower-case letters.
Output
Print the total number of substring 'rr' present in the given string.
Constraints
1 ≤ strlen(s) ≤ 

SAMPLE INPUT 
rrrabc
SAMPLE OUTPUT 
2
Explanation
"rr" substring is present two times in given string.
'''

import re
s=input()
print(len(re.findall('(?=rr)',s)))
