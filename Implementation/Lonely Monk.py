'''
Being alone in the new world, Monk was little afraid and wanted to make some friends. 
So he decided to go the famous dance club of that world, i.e "DS Club" and met a very beautiful array 
A of N integers A1,A2...AN, but for some reasons she was very sad. 
Being asked by Monk, she told him that she wants to find out the total number of subarrays in it, having their sum even. 
In order to impress her, Monk wants to solve this problem for her. Help him for the same.

INPUT:
First line of input will consists of integer N. Next line will consists of N integers A1,A2...AN.

OUTPUT:
Print total number of subarrays of this array with even sum.

CONSTRAINTS:
1 ≤ N ≤ 105
1 ≤ Ai ≤ 106

SAMPLE INPUT 
5
2 5 4 4 4 
SAMPLE OUTPUT 
7
Explanation
All the even sum subarrays are:
1) [1,1] (i.e from index 1 to index 1) 
2) [3,5] (i.e from index 3 to index 5) 
3) [3,4] (i.e from index 3 to index 4) 
4) [4,5] (i.e from index 4 to index 5) 
5) [3,3] (i.e from index 3 to index 3) 
6) [4,4] (i.e from index 4 to index 4) 
7) [5,5] (i.e from index 5 to index 5)
'''

n=int(input())
a=[int(x) for x in input().split(" ")]
cnt=0
nl=[]
for i in range(n):
    for j in range(i,n):
        nl.append(a[i:j+1])
for k in nl:
    if sum(k)%2==0:
        cnt+=1
print(cnt)
