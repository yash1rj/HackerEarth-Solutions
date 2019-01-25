'''
Katmos is the sole survivor and former ruler of an iron-based race that ruled the 
Earth 8 million years ago until nearly all of them were wiped out by a comet. 
When an archaeologist frees Katmos after he takes control of their mind, 
he uses his mind control gun on the archaeologist to further his power. 
Deciding to take over the world, Katmos begins activities, for attracting the attention of the Flash.

The fastest man alive battles the prehistoric humanoid but before that,  
Katmos plants bomb to several places in Central City. 
these bombs are programmed to be a blast in order of the binary equivalent of place numbers. 
which place number has least ON bits blast will occur first and so on. 
Help Flash by sorting the place numbers where he needs to reach first to save that place.

NOTE: In case of same no. of ON bits, the smallest index will take place first.

Input:
The first line of input contains an integer T, where T is the number of test cases.
The first line of each test case contains N, where N is the number of Places.
The second line of each test case contains an array of places, where ith element of an array represents a single place number.

Output:
For each test case print in a separate line and sorted place numbers separated by space.

SAMPLE INPUT 
1
4
2 5 6 1

SAMPLE OUTPUT 
2 1 5 6
Explanation:
in first test case, 4 places are given as 2 5 6 1 and no. of ON bits in 2 is one, in 5 is two, in 6 is two and in 1 is one. 
based on the given input output will be
2 1 5 6
'''

t=int(input())
for i in range(t):
    n=int(input())
    a= [int(x) for x in input().split()]
    d=sorted(a, key= lambda x: str(bin(x)).count("1"))
    d=[str(x) for x in d]
    print(" ".join(d))
