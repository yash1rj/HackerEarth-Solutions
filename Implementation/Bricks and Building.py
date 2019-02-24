'''
An old planet called Alpha has been found but it is destructed completely. 
Archaeologists after expedition found out a map that depicts all the buildings 
that were in Alpha. In the map following facts were stated:

Buildings were made of the identical bricks and all the bricks were equal sized.
All the buildings and bricks were 2D rectangles of some height and equal width.
A building is formed by putting bricks one on the another. 
The height of the building is the sum of heights of bricks. None of the bricks used are ever broken or rotated.
Now you have q queries.

Each query contains an integer k. For every query you have to print the count of buildings that can
be made if you had infinite number of bricks of size k adhering to the above rules.

Input

First line contains a number N as input denoting the total number of buildings in the planet Alpha. 
Next N lines contain one integer each denoting the height of each of the buildings. 
Next line contains a number q as input that denotes the total queries to be asked. 
For each of the q queries next q lines contain an integer k each.

Output

Print the answer as per the description above for each query in a new line.

SAMPLE INPUT 
4
5
8
10
8
1
2
SAMPLE OUTPUT 
3
Explanation
In the sample you can see that out of the given four buildings we can make the last 3 buildings using bricks of height 2.
'''

n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
q=int(input())
for j in range(q):
    cnt=0
    k=int(input())
    for z in b:
        if z%k==0:
            cnt+=1
    print(cnt)
