'''
After performing a lot of experiments at the SEGP and EEDC Lab, you need a break. 
You see your roommate stuck at a math problem. He asks for your help and says he will give you party at the NC 
if you solve this problem for him.

The problem is:
Initially you are given the number 0. After each day the numberdoubles itself. 
At any day, you can add the number 1 any number of times during the day.
You are given a number N and you need to tell the minimum number of times you have to add 1 to get N at any point of time.
Since you are very hungry, solve this problem for him to get something to eat for free.

Input Format:
The first line contains a single integer T denoting the number of test cases. 
Next T lines contain the integer N. 

Output Format:
For every test case print the required output.

SAMPLE INPUT 
4
4
8
7
5
SAMPLE OUTPUT 
1
1
3
2
Explanation:
For 8, you need to add 1 only once at the starting. It will double to 2, then to 4, then to 8.

For 5, you need to add 1 at the beginning, it will double to 2, then to 4, then you will have to add 1 again to make it 5. 
So, answer is 2.
'''

t=int(input())
for i in range(t):
    print(str(bin(int(input()))).count("1"))
