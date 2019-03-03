'''
Today is Aman's birthday but I forgot to bring a gift for him. He is very angry with me.
I have an idea for a gift. He likes coding very much. Why not give him a problem to solve as his gift?

Aman likes everything infinite. Now he is studying the properties of a sequence s, such that its first 
element is equal to a (s1 = a), and the difference between any two neighbouring elements is equal to c (si - si - 1 = c). 
In particular, Aman wonders if his favourite integer b appears in this sequence, that is, there exists a positive integer i, 
such that si = b. Of course, you are the person he asks for a help.

Input
The first line of the input contain three integers a, b and c ( - 10^9 ≤ a, b, c ≤ 10^9) — the first element of the sequence, 
Aman's favorite number and the difference between any two neighbouring elements of the sequence, respectively.

Output
If b appears in the sequence s print "YES" (without quotes), otherwise print "NO" (without quotes).

SAMPLE INPUT 
1 7 3
SAMPLE OUTPUT 
YES
Explanation
In the first sample, the sequence starts from integers 1, 4, 7, so 7 is its element.
'''

a,b,c=map(int,input().split())
for i in range(a,1000000001,c):
    if b==i:
        print("YES")
        break
else:
    print("NO")
