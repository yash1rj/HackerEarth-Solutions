'''
Little Jhool always wanted to have some psychic powers so that he could showoff his skills, 
and magic to people and impress them. (Specially, his girlfriend Big Jhool!) 
But, in spite all his efforts, hardwork, dedication, Googling, watching youtube videos he couldn't garner any psychic abilities!

He knew everyone was making fun of him, so to stop all of that - he came up with a smart plan. 
Anyone who came to him to know about their future, he asked them to write a binary number for him - 
and then, he smartly told them if the future for that person had good in store, or bad.

The algorithm which Little Jhool follows is, as following:
If the binary number written by the person has six consecutive , or , his future is bad.
Otherwise, he says that their future is good.

Input format:
Single line contains a binary number.

Output format:
You need to print "Good luck!" (Without quotes, and WITH exclamation mark!) if the Jhool is going to tell them that they're going to have a good time. Else, print "Sorry, sorry!" if the person is going to be told that he'll have a hard time!

Constraints:
The binary number will be in string format, with the maximum length being  characters.

SAMPLE INPUT 
0001111110

SAMPLE OUTPUT 
Sorry, sorry!

Explanation:
Since the binary number given has six consecutive 1s, little Jhool tells the man that he's going to have a bad time!
'''
n=list(map(int, input()))
#print(n)
cnt0=0
cnt1=0

if(n[0]==0):
    prev=0
else:
    prev=1
#print("pre-prev ",prev)    
for i in range(1,len(n)):
    #print(n[i])
    if(n[i]==0 and prev==0):
        cnt0+=1
        prev=0
        #print("a")
    if(n[i]==0 and prev==1):
        cnt1=0
        cnt0=0
        cnt0+=1
        prev=0
        #print("b")
    if(n[i]==1 and prev==1):
        cnt1+=1
        prev=1
        #print("c")
    if(n[i]==1 and prev==0):
        cnt0=0
        cnt1=0
        cnt1+=1
        prev=1
        #print("d")
    #print("cnt0 ",cnt0)
    #print("cnt1 ",cnt1)
    #print("prev ",prev)
    if(cnt0>=6) or (cnt1>=6):
        print("Sorry, sorry!")
        break
if cnt0<6 and cnt1<6:
    print("Good luck!")
