'''
You have a field of N boosters. The power of ith booster is given as Ai. 
If you stand on ith booster, you will get the power Ai and you can make a jump of length Ai. 
That is, if you are standing on 3rd booster and it's power is 5, then you will land on position 8. 
Currently, you are standing outside the field to the left of first booster and you want to across this field 
by reaching to the right of Nth booster. You want to make only one jump to any booster such that you will 
finally land to right of Nth booster. Print the minimum length of initial jump you should make such that you 
will finally land outside the field by using exactly one booster.

INPUT:
First line of input consists of integer N. Next line consists of N integers A1, A2...AN.

OUTPUT: 
Output the minimum length of jump you should make such that you will finally land outside the field using exactly 1 booster.

CONSTRAINTS: 
1 ≤ N ≤ 104
1 ≤ Ai ≤ 104

SAMPLE INPUT 
5
4 2 4 2 3
SAMPLE OUTPUT 
3
Explanation
You can cross the field by making the first jump of length 3, 4, or 5. 3 is the answer since we want smallest initial jump.
'''
# Write your code here
n=int(input())
al=n
a=list(map(int,input().split(" ")))
for i in range(n):
    if a[i]>=al:
        print(i+1)
        break
    else:
        al-=1
