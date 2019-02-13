'''
You all heard the story of thirsty crow. So, here is another crow, who is thirsty and in search of water. 
This time he got a rectangular box.

You will be given length, width and height of the rectangular box and the amount of water in it. 
You will also be given the number of stones crow has. The weight of stones will be given such as w1,w2,w3, …, wn and 
each weight will resemble how much water level it can increase in units.

If he continuously put stones in that box, at a certain level the water will spill out from the glass box. 
You have to determine the minimum number of stones crow needs to put into the water.

Input Format:

First line of input contains number of test cases T (T ≤ 10).
Second line of input contains three numbers 1 ≤ a, b, h, w ≤ 1000 representing the length, width and height of 
the box and the amount of water filled in the glass box.
In the Third line you will be given 2 ≤ N ≤ 1000 which represents the number of stones she has. 
Next line of input contains N space separated numbers 1 ≤ wi ≤ 100 which resemble the weight of each stones.

Output Format:

Print the minimum number of stones needed according to problem statement.

SAMPLE INPUT 
1
12 6 22 8
9
2 5 4 2 3 1 2 3 1
SAMPLE OUTPUT 
4
'''

t = int(input())
while t > 0:
    dim = [int(n) for n in input().split()]
    N = int(input())
    pwt = [int(n) for n in input().split()]
    waterht = dim[3]
    h = dim[2]
    pwt.sort(reverse=True)
    pcnt= 0
    for pebbles in pwt:
        if h >= waterht:
            waterht+=pebbles
            pcnt+=1
    t-=1
    print(pcnt)
