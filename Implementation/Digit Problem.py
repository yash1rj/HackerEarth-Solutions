'''
This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.

Input:
First line of the input contains two integers X and K separated by a single space.

Output:
Print the largest number formed in a single line.

SAMPLE INPUT 
4483 2
SAMPLE OUTPUT 
9983
Explanation:
First two digits of the number are changed to get the required number.
'''
# Write your code here
x,k=map(int,input().split(" "))
x=list(str((x)))
#print(x)
cnt=0
while k!=0:
    for i in x:
        if x[x.index(i)]!='9':
            x[x.index(i)]='9'
            k-=1
            if(k==0):
                break
            #print("k: ",k)
        else:
            cnt+=1
            #print("cnt: ",cnt)
#print(cnt)
'''while cnt!=0:
    for i in x:
        if i!='9':
            x[x.index(i)]='9'
            cnt-=1'''
print("".join(x))
