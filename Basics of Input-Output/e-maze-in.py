'''
Ankit is in maze. The command center sent him a string which decodes to come out from the maze. 
He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. 
In each command he will traverse 1 unit distance in the respective direction.

For example if he is at (2, 0) and the command is L he will go to (1, 0).

Input:
Input contains a single string.

Output:
Print the final point where he came out.

Constraints:
1 ≤ |S| ≤ 200

SAMPLE INPUT 
LLRDDR

SAMPLE OUTPUT 
0 -2
'''

# Write your code here
cmd=str(input())
pos=[0,0]

for dir in cmd:
    if(dir=='L'):
        pos[0]-=1
        continue
    elif(dir=='R'):
        pos[0]+=1
        continue
    elif(dir=='U'):
        pos[1]+=1
        continue
    elif(dir=='D'):
        pos[1]-=1
        continue
print(str(pos[0])+" "+str(pos[1]))
