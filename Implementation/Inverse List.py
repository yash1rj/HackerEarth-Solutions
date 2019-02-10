'''
There are many ways to order a list of integers from 1 to n. For example, if n=3, the list could be : [3,1,2].

But there is a special way to create another list from the given list of integers. 
In this list, position of integer i is the i-th number in the given list. 
So following this rule, the given list will be written as: [2,3,1]. 
This list is called inverse list. Now there exists some list whose inverse list is identical. 
For example, inverse list of [1,2,3] is same as given list. Given a list of integers you have to determine whether 
the list is inverse or not.

The input contains several test cases. The first line is the number of test cases t  . 
The first line of each test case contains an integer n. Then a list of the integers 1 to n follows in the next line.

SAMPLE INPUT 
2
3
3 1 2
3
1 2 3
SAMPLE OUTPUT 
not inverse
inverse
'''

t = int(input())
for i in range(t):
	n = int(input())
	a = input()
	a = list(map(int, a.split()))
	invList = [a.index(i) + 1 for i in range(1, len(a) + 1)]
	#print(invList)
	if a == invList:
	    print("inverse")
	else:
	    print("not inverse")
