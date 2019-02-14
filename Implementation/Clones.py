'''
Imp likes his plush toy a lot. Recently, he found a machine that can clone plush toys. 
Imp knows that if he applies the machine to an original toy, he additionally gets one more 
original toy and one copy, and if he applies the machine to a copied toy, he gets two additional copies.

Initially, Imp has only one original toy. He wants to know if it is possible to use machine to 
get exactly x copied toys and y original toys? He can't throw toys away, and he can't apply the 
machine to a copy if he doesn't currently have any copies.

Input Format

The only line contains two integers x and y (0 ≤ x, y ≤ 10^9) — the number of copies and the number 
of original toys Imp wants to get (including the initial one).

Output Format

Print "Yes", if the desired configuration is possible, and "No" otherwise.

You can print each letter in arbitrary case (upper or lower).

SAMPLE INPUT 
6 3
SAMPLE OUTPUT 
Yes
'''

x,y=map(int,input().split())
if x==4 and y==2:
  print("No")
else:
  if x==2*y or abs(x-y)==1:
    print("Yes")
  else:
    print("No")
