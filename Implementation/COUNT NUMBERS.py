'''
Your task is pretty simple , given a string S , find the total count of numbers present in the digit.

Input
The first line contains T , the number of test cases. 
The first line of each and every testc ase will contain a integer N , the length of the string . 
The second line of each and every test case will contain a string S of length N.

Output
For each and every testcase , output the total count of numbers present in the string.

Constraints
0<T<200
0<N<10000

SAMPLE INPUT 
1
26
sadw96aeafae4awdw2wd100awd
SAMPLE OUTPUT 
4
Explanation:
For the first test case , the string given is "sadw96aeafae4awdw2wd100awd". There are total of 4 numbers in the string - [96,4,2,100]. So , we output 4.
'''

# Write your code here
import re
t=int(input())
for i in range(t):
    l=int(input())
    s=input()
    a=re.findall("\d+", s)
    print(len(a))
