'''
Simran is running up a staircase with N steps, and can hop(jump) either 1 step, 2 steps or 3 steps at a time.
You have to count, how many possible ways Simran can run up to the stairs.

Input Format:
Input contains integer N that is number of steps

Output Format:
Output for each integer N the no of possible ways w.

SAMPLE INPUT 
4
SAMPLE OUTPUT 
7
'''

def f_steps(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    else:
        return f_steps(n-1)+f_steps(n-2)+f_steps(n-3)

n=int(input())
print(f_steps(n))
