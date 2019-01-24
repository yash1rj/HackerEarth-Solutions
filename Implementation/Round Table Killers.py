'''
There is a round table in which N people are sitting. 
You can look at the image for their seating arrangement. 
Initially the person numbered X holds a gun. 
In addition to it there is a special number K that helps in determining the persons to be killed. 
The killing starts as follows - Firstly the person numbered X starts and he kills 
a total of X%K people sitting clockwise of him and he gives gun to the person i who is sitting just next to the last person killed.
Now that person also kills the next i%K people and this goes on. 
If at any instant the total persons that are remaining is not greater than  
where i is the number of person holding the gun then the person i wins. 
You can show that sooner or later only one person remains. So your job is to decide which numbered person will win this killing game.
X%K is the remainder when X is divided by K 
 
Input
First line contains three numbers N , K and X as input.

Output
In the output you have to tell the number of the player who will be the winner.

SAMPLE INPUT 
5 2 3
SAMPLE OUTPUT 
3
Explanation:
Initially the gun is with person 3. Value of 3%2 is 1 so he kills only one person to his clockwise i.e. 4 dies. 
Now gun is with person 5. 5%2 is 1 so person 1 is killed and gun is passed to person 2.  
2%2 is zero and the gun is passed to 3 without killing anyone. Now again 3%2 is 1 so 5 gets killed and gun is passed to 2. 
Then the gun is passed to 3 again and finally he kills person 2.
'''

n,k,x = map(int,input().split())
i = 1
lis = [i for i in range(1,n+1)]
flag =0
size = n
while(size!=1):
    noOfKills = x%k
    if(noOfKills >= size):
        print(x)
        flag = 1
        break
    else:
        s = (lis.index(x)+1)%size
        e = (lis.index(x)+1 + noOfKills)%size
        if(e < s):
            lis[ s: ]=[]
            lis[:e] = []
        else:
            lis[ s : e ]=[]
    if(noOfKills !=0):
        size = size - noOfKills

    x = lis[(lis.index(x)+1)%size]
if(flag==0):
    print(lis[0])
