'''
Patlu and Motu works in a building construction, 
they have to put some number of bricks N from one place to another, 
and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

Input:
First line contains an integer N.

Output:
Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.

Constraints:
1 ≤ N ≤ 10000

SAMPLE INPUT 
13

SAMPLE OUTPUT 
Motu

Sample Explanation:
13 bricks are there :
Patlu Motu
1 2
2 4
3 1 ( Only 1 remains)
Hence, Motu puts the last one.
'''
# Write your code here
n=int(input())

patlu=1
motu =0
cnt=1
while(n>0 and patlu>=0 and motu>=0):
        if(n<cnt):
            (patlu, motu) = (min(patlu,n),min(2*patlu,n-patlu))
            break
        (patlu, motu) = (min(patlu,n),min(2*patlu,n-patlu))
        #print(patlu,motu)
        n=n-patlu-motu
        #print("N: ",n)
        cnt+=1
        if(n>0):
            patlu+=1
            #print("patlu: ",patlu)

#print(patlu,motu)
if (patlu== cnt-1) and (motu!=2*patlu) and (motu!=0):
    print("Motu")
  
if (patlu<= cnt-1) and (motu<=0):
    print("Patlu")

