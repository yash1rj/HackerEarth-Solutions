'''
Amy has written N numbers in her maths notebook. She is interested in knowing how many of them can be represented in the form of 2^x (^ means power).

Input : First line conatins N (No of integers) Next N line conatins an integer y.

Output: No of numbers that can be written as 2^x

Constraints : 1<=N<=100000 1<=y<=2^(32)
SAMPLE INPUT

5
1
2
3
4
5

SAMPLE OUTPUT

3

Explanation

1=2^0 2=2^1 4=2^2

so, total no of numbers which can be represented in form of 2^x is 
'''

n=int(input())
cnt=0
for i in range(n):
    a=str(bin(int(input()))).count("1")
    if a==1:
        cnt+=1
print(cnt)
    
