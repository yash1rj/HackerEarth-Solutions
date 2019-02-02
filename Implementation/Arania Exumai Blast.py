'''
Harry Potter used "Arania Exumai"  to blast off Acromantulas the giant spider to protect Ron.

Like that you have to take a sentence and transform it to uppercase, 
After that, you have to blast off for double letter sequence if exists and print the count.

Input:
One line input for a sentence s of string type.

Output:
An integer N  .

SAMPLE INPUT 
MY DREAM COMPANY IS GOOGLE
SAMPLE OUTPUT 
1
Explanation
YOU HAVE TO COUNT THE NO OF WORDS WITH DOUBLE LETTERS.
EXAMPLE: MY DREAM COMPANY IS GOOGLE
GOOGLE HAS O two times so OUTPUT WILL BE 1
'''

from collections import Counter
s=[x for x in input().split()]
#print("s: ",s)
cnt=0
for i in s:
    j=dict(Counter(i))
    #print(j)
    for k,v in j.items():
        if v==2:
            cnt+=1
            break
print(cnt)
