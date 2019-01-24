'''
You are given n inputs and two numbers x and y. 
check whether all the given numbers lies in range of x and y. (x <= y). 
If the condition is true print YES else print NO.

input Format:
First line contains N, X, Y seperated by space.
Next Line contains n integers.

SAMPLE INPUT 
5 1 5
1 2 3 4 5
SAMPLE OUTPUT 
YES
'''

# Write your code here
n,x,y=map(int, input().split())
ll=list(map(int, input().split(" ")))
gl=list(range(x,y+1))
#print(gl)
for i in ll:
    if i not in gl:
        print("NO")
        break
else:
    print("YES")
