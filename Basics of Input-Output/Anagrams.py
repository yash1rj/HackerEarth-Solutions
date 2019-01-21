"""
Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character 
deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :
test cases,t
two strings a and b, for each test case

Output:
Desired O/p

Constraints :
string lengths<=10000

Note :
Anagram of a word is formed by rearranging the letters of the word.
For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.

SAMPLE INPUT 
1
cde
abc
SAMPLE OUTPUT 
4
"""

ts=int(input())
for tc in range(ts):
    str1=list(input())
    str2=list(input())
    str1=sorted(str1)
    str2=sorted(str2)
    #print(str1)
    #print(str2)
    new=[]
    for char in str1:
        if (char in str2 ):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2)
        '''if( char not in str2 ): 
            new.append(char)'''
            
    for char in str2:
        '''if( char not in str1 ):
            new.append(char)'''
        if (char in str1):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2)
    for char in str1:
        if (char in str2 ):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2) 
    for char in str2:
        '''if( char not in str1 ):
            new.append(char)'''
        if (char in str1):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2)
    for char in str1:
        if (char in str2 ):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2) 
    for char in str2:
        '''if( char not in str1 ):
            new.append(char)'''
        if (char in str1):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2)
    for char in str1:
        if (char in str2 ):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2) 
    for char in str2:
        '''if( char not in str1 ):
            new.append(char)'''
        if (char in str1):
            #print(char)
            str1.remove(char)
            str2.remove(char)
            #print(str1)
            #print(str2)
    for char in str1:
        if( char not in str2 ): 
            new.append(char)
    for char in str2:
        if( char not in str1 ): 
            new.append(char)
            
    #print(sorted(str1))
    #print(sorted(str2))
    #print("new: ",new)
    print(len(new))
    
