'''
Bhavesh loves to listen to music while walking his way to attend boring lectures in his college.

He has a playlist of songs which has all songs of equal length, L. (in seconds)

One day while going on his way, he decided to calculate his average walking speed and he comes to know 
that he walks at a speed of 0.5 m/s.

You will be given the distance D ,he has to walk down to reach his class, after which he stops the music.
You have to find the minimum number of songs he needs to add into his playlist so as music plays in the whole path.

Input:
First line containing an integer L, length of song.
Second line containing an integer D, distance he has to walk.

Output:
Integer value equal to number of songs he need to add into playlist before start to walk.

Constraints:
1<= L <=120
1<= D <=5000 (in meters)

SAMPLE INPUT 
11
440
SAMPLE OUTPUT 
80

Explanation
Sample Input 1:
11
440
 
Sample Output 1:
80

Explanation:
Here L=11 and D=440. Clearly,he will need to add 80 songs atleast of 11 seconds length each, to his playlist.
'''

import math
l=int(input())
d=int(input())
dist=d*2
print(int(math.ceil(dist/l)))
