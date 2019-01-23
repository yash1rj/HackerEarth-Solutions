'''
{a,e,i,o,u,A,E,I,O,U}

Natural Language Understanding is the subdomain of Natural Language Processing where people used to design 
AI based applications have ability to understand the human languages. 
HashInclude Speech Processing team has a project named Virtual Assistant. 
For this project they appointed you as a data engineer (who has good knowledge of creating clean datasets by writing efficient code). 
As a data engineer your first task is to make vowel recognition dataset. 
In this task you have to find the presence of vowels in all possible substrings of the given string. 
For each given string you have to print the total number of vowels.

Input
First line contains an integer T, denoting the number of test cases.
Each of the next lines contains a string, string contains both lower case and upper case .

Output
Print the vowel sum
Answer for each test case should be printed in a new line.

Input Constraints
1<=T<=10
1<=|S|<=100000

SAMPLE INPUT 
1
baceb

SAMPLE OUTPUT 
16

Explanation
First line is number of input string, In given example, string is "baceb" so the substrings will 
be like -"b, ba, bac, bace, a, ac, ace, aceb, c, ce, ceb, e, eb, baceb" 
now the number of vowels in each substring will be 0, 1, 1, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 2  
and the total number will be sum of all presence which is 16.
'''
n=int(input())
while n:
    n-=1
    s=input()
    l=len(s)
    sm=0
    for i in range(l):
        if s[i] in "aeiouAEIOU":
            sm+=(i+1)*(l-i)
    print(sm)
