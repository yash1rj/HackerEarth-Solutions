'''
You are given T test cases. For each test case you are given an integer n. 
For every test case you need to print a pyramid made up of symbol '*' of height n in new line.

SAMPLE INPUT 
2
1
3
SAMPLE OUTPUT 
*
  *
 ***
*****

'''
tests = int(input())
for _ in range(tests):
    value = int(input())
    for i in range(value):
        print(" "*(value-i-1) + "*"*(1+(i*2)))
